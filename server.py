from functools import reduce

numberOfTasks, time = [int(i) for i in input().split()]
tasks = [int(i) for i in input().split()]

solution = []
for task in tasks:
	if solution == [] and tasks[0] <= time:
		solution.append(task)
	elif solution != [] and reduce(lambda x, y: x + y, solution) + task <= int(time):
		solution.append(task)
	else:
		break
		
print(len(solution))