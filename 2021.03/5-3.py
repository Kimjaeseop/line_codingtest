# 옵션에 대한 인자가 맞는지 체크
def cmdCheck(opt, args, rules):
# alias 인 경우 기존의 이름으로 치환
	if (rules[opt])[0] == '-':
		opt = rules[opt]

# (STRING, INT) 인자 개수가 두 개 이상이거나 조건에 맞지 않으면 False
	if rules[opt] == "STRING" and (len(args) > 1 or args[0].isdigit() == True):
		return False

	if rules[opt] == "NUMBER" and (len(args) > 1 or args[0].isdigit() != True):
		return False

	if rules[opt] == "NUMBERS":
		for arg in args:
			if arg.isdigit() != True:
				return False

	if rules[opt] == "STRINGS":
		for arg in args:
			if arg.isdigit() == True:
				return False

	if rules[opt] == "NULL" and len(args) > 0: # NULL인경우는 맨 끝이 아니라면 args에 아무 것도 없어야 함
		return False

	return True

def solution(program, flag_rules, commands):
	answer = []
	cmds = []
	rules = {}
	alias = []
	dup_alias = False

# rules to dict
	for s in flag_rules:
		if len(s.split(' ')) == 3: # alias 인 경우
			rules[s.split(' ')[0]] = s.split(' ')[2]
			alias.append([s.split(' ')[0], s.split(' ')[2]])
		else: # alias 아닌 경우
			rules[s.split(' ')[0]] = s.split(' ')[1]
	for s in commands: # tokenize commands
		cmds.append(s.split(' '))
# 각 명령어 체크

	for cmd in cmds:
		dup_alias = False
# 한 명령어에 alias와 기존 명령어가 동시에 존재하는지 검사
		for a in alias:
			if a[0] in cmd and a[1] in cmd:
				answer.append(False)
				dup_alias = True
				break

		if dup_alias == True:
			continue

		if cmd[0] != program: # command로 입력된 프로그램명과 조건으로 제시된 프로그램명 비교
			answer.append(False)
			continue
# 각 명령어에서 옵션과 인자가 조건에 일치하는지 여부를 체크하기 위한 리스트
		check = [False for _ in range(len(cmd))]
# 이 단계까지 넘어온 명령어는 위에서 체크한 프로그램명 일치여부를 통과했으므로 True 대입
		check[0] = True

# 이미 비교한 프로그램명을 제외한 나머지 옵션과 인자를 비교하기 위한 반복문
		for i in range(1, len(cmd)):
			if check[i] == True: # 이미 체크했다면 continue
				continue
# 맨 뒤의 인자가 -e이거나 조건에 부합하지 않는 옵션인 경우를 위해 체크하는 조건문
			elif i == len(cmd)-1 and check[-1] == False:
# 조건에 주어지지 않은 옵션이거나 주어졌더라도 NULL이 아니라면 False 
# 마지막까지 체크되지 않은 옵션은 주어지지 않은 옵션이거나 -e인 경우밖에 없다
				if cmd[-1] not in rules or (cmd[-1] in rules and rules[cmd[-1]] != "NULL"):
					answer.append(False)
				else:
# 체크되지 않았다면 True
					check[-1] = True
			elif cmd[i][0] == '-': # 옵션이라면
# 옵션 뒤에 따라오는 인자 저장
				j = i + 1
				args = []

				while j < len(cmd) and cmd[j][0] != '-':
					args.append(cmd[j])
					j += 1

				if cmdCheck(cmd[i], args, rules) == False:
					answer.append(False)
					check[i] = False
					break
				else:
					check[i] = True
					for j in range(len(args)):
						check[i + j + 1] = True
# 비교가 끝나고 check 리스트에 False가 없다면 True
		if False not in check:
				answer.append(True)
			
	return answer

print(solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))
