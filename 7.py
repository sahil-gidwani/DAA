def printJobScheduling(arr, t):
	n = len(arr)

	# bubble sort all jobs according to decreasing order of profit
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# to keep track of free time slots
	result = [False] * t

	# to store result (sequence of jobs)
	job = ['-1'] * t

	# iterate through all given jobs
	for i in range(n):
		# find a free slot for this job
		# (note that we start from the last possible slot)
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
			# free slot found
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	print(job)

# [jobID, deadline, profit]
arr = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]

print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)

# Time Complexity: O(n^2)
# Auxiliary Space: O(t)
