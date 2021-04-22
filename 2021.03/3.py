ef solution(enter, leave):
	answer = []
	arr = []

	for i in range(len(enter)):
		answer.append(0)
	
	top = 0
	for i in enter:
		arr.append(i)

		if len(arr) >= 2:
			for j in arr:
				answer[j-1] += 1

			if len(arr) > 2:
				answer[i-1] += len(arr)-2

		top = leave[0]

		while top in arr:
			arr.remove(top)
			leave.pop(0)
			
			if len(arr) == 0:
				break

			top = leave[0]
		
	return answer

print(solution([1,3,2],[1,2,3]))
print(solution([1,4,2,3],[2,1,3,4]))
print(solution([3,2,1],[2,1,3]))
print(solution([3,2,1],[1,3,2]))
print(solution([1,4,2,3],[2,1,4,3]))
