# Job Scheduling Problem using Greedy Approach

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

"""
The Job Scheduling Problem, often referred to as the Job Sequencing Problem, is a classic optimization problem in the field of computer science and operations research. The problem can be defined as follows:

**Problem Statement:**
Given a set of jobs, each with a specified deadline, a processing time, and an associated profit (or cost), the objective is to schedule the jobs in a way that maximizes the total profit while ensuring that each job is completed within its deadline.

**Key Components:**
- **Jobs:** There are N jobs, each labeled with a unique identifier.
- **Deadline:** Each job has a deadline by which it must be completed.
- **Processing Time:** Each job requires a certain amount of time for execution.
- **Profit or Cost:** Each job is associated with a profit (in case of profit maximization) or cost (in case of cost minimization).

**Constraints:**
- A job must be scheduled and completed within its specified deadline.
- Once a job is started, it cannot be interrupted, meaning it must be executed in a contiguous time interval.

**Objective:**
The primary objective is to maximize the total profit by choosing which jobs to schedule and in what order. The goal is to select a subset of jobs to schedule in such a way that the total profit is maximized while adhering to the deadline constraints.

**Variants of Job Scheduling Problem:**
1. **Single Machine Scheduling:** In this variant, there is only one machine available to process the jobs, and the goal is to schedule the jobs on this machine efficiently.
2. **Parallel Machine Scheduling:** Multiple machines are available for processing, and the objective is to allocate jobs to machines to optimize the schedule.
3. **Preemptive Scheduling:** Jobs can be interrupted and resumed, and the goal is to maximize the total profit while adhering to deadlines.
4. **Job Scheduling with Time Windows:** Jobs can only be scheduled within certain time windows.

**Approaches:**
There are various algorithms and approaches to solving the Job Scheduling Problem, including:
- Greedy Algorithms: Often used for finding an approximate solution, such as sorting jobs by profit-to-deadline ratio and selecting jobs in a greedy manner.
- Dynamic Programming: Used for solving certain variants with more complex constraints.
- Integer Linear Programming: Formulating the problem as an optimization model and solving it using linear programming techniques.

The Job Scheduling Problem has applications in various domains, including project management, manufacturing, task scheduling, and more. Depending on the specific constraints and objectives, different variants of the problem may arise, leading to the development of specialized algorithms and techniques for solving them.
"""
