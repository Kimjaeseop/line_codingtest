def solution(inp_str):
	answer = []
	if (len(inp_str) < 8 or len(inp_str) > 15):
		answer.append(1)

	check = [0, 0, 0, 0]
	for c in inp_str:
		if 2 not in answer and c.isalpha() == False and c.isdigit() == False and (c not in "~!@#$%^&*"):
			answer.append(2);
		else:
			if c.isupper():
				check[0] = 1
			if c.islower():
				check[1] = 1
			if c.isdigit():
				check[2] = 1
			if c in "~!@#$%^&*":
				check[3] = 1

	if check.count(1) < 3:
		answer.append(3)

	count = 0
	for i in range(len(inp_str)):
		if i == 0:
			continue
		
		if inp_str[i] == inp_str[i-1]:
			count+=1

	if count >= 3:
		answer.append(4)

	for c in inp_str:
		if inp_str.count(c) >= 5:
			answer.append(5)
			break

	if len(answer) == 0:
		answer.append(0)

	return sorted(answer)

print(solution("AaTa+!12-3"))
print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))
print(solution("ZzZz9Z824"))
