# Given a list of jobs, their gain value, and their deadline
# Design a job scheduler that maximizes gain and schedules as many meetings as possible
# Time starts at 0, jobs each take one unit of time to complete and cannot be scheduled concurrently

# Job | Gain | Deadline
#
#  a  |  1   |    2
#  b  |  1   |    2
#  c  |  2   |    3
#  d  |  3   |    3
#  e  |  2   |    4

# The input is not ordered by deadline or gain
# The answer to this example is [a, c, d, e] and the gain is 8
# a and b can be used interchangeably and c and d can be in different orders

import heapq

def pop(heap, schedule, gain, currentDeadline, deadline):
    popCount = currentDeadline - deadline
    gain = 0
    for _ in range(popCount):
        if len(heap) == 0:
            break
        popGain, popID, _ = heapq.heappop(heap)
        schedule.append(popID)
        gain += popGain * -1  # Undo inversion for maxheap functionality
    currentDeadline = deadline
    return gain

def jobScheduler(jobs):
    jobs.sort(reverse=True, key=lambda x: x[2])  # Sorts jobs by deadline descending 
    gain = 0
    heap = []
    schedule = []
    currentDeadline = jobs[0][2]
    # Use a maxheap to build up list of possible jobs, pop off
    for jobID, jobGain, deadline in jobs:
        if deadline != currentDeadline:
            gain += pop(heap, schedule, gain, currentDeadline, deadline)
        heapq.heappush(heap, (jobGain * -1, jobID, deadline))  # Multiplying gain by -1 for maxHeap functionality
    return schedule[::-1], gain


def main():
    # Job ID, gain, deadline
    jobs = [('a', 1, 2), ('b', 1, 2), ('c', 2, 3), ('d', 3, 3), ('e', 2, 4)]
    schedule, gain = jobScheduler(jobs)
    print("\nSchedule: {}\nGain: {}\n".format(schedule, gain))


if __name__ == "__main__":
    main()
