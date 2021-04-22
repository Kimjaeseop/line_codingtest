def solution(table, languages, preference):
	arr = []
	score = [0, 0, 0, 0, 0]
	for i in range(5):
		arr.append(table[i].split(' '))

	for i in range(5):
		for j in range(len(languages)):
			if languages[j] in arr[i]:
				score[i] += (preference[j] * (6 - arr[i].index(languages[j])))

	count = 0
	answer = []
	for idx, i in enumerate(score):
		if i == max(score):
			answer.append(arr[idx][0])
			count+=1

	return sorted(answer)[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
