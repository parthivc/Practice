# Naive V1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
Input
-----
voters -
Voter arrival data (array of strings) sorted by arrival timestamp
Format of each entry - "<arrivalTimestamp>,<votingTime>,<numChildren>,<toleranceTime>"
 
numMachines -
Number of voting machines
 
queueSize -
Size of the polling place's queue

Output
------
Return an array of integers of size `numMachines+1` where the 0-th index represents the total number of voters who successfully cast votes and indices 1 to `numMachines` represent the number of votes cast at each voting machine.
"""

import heapq

def solution(voters, numMachines, queueSize):
    result = [0 for _ in range(numMachines + 1)]
    # Could use a segment tree for representing open voting machines
        # Will use a bool array for now
        # Counter for the size of the current queue
    # Priority queue for order of events that need to be processed
    # Use LRU cache system for the queue itself (for tolerance removal)
    
    
    ###############################################################################
    # prototype
    q = []
    qSize = 0
    process = []  # Events that need to be processed
    heapq.heapify(process)
    openMachines = [0 for _ in range(numMachines)]  # Available machines
    atMachine = dict()  # True if at machine, false if in the queue
    # Linear search for now, will improve performance later
    for i in range(len(voters)):
        data = list(map(int, voters[i].split(',')))
        # If something needs to be done before this voter is processed
        while process and process[0][0] <= data[0]:
            current, inQueue, index = heapq.heappop(process)
            if not inQueue:  # They need to be moved out of a voting machine
                # atMachine.pop(voterID)
                if q:  # Someone replaces the person leaving
                    newVoterIndex = q.pop(0)
                    newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                    openMachines[index] = newVoterIndex + 1
                    qSize -= 1 + newVoterData[2]
                    atMachine[newVoterIndex] = index + 1
                    result[0] += 1
                    result[index + 1] += 1
                    heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
                else:  # No one replaces the person leaving
                    openMachines[index] = 0
            else:  # Tolerance time was reached but the person may already be at a machine
                if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                    voterData = list(map(int, voters[index].split(',')))
                    q.remove(index)
                    atMachine.pop(index)
                    qSize -= 1 + voterData[2]
        # If the voting machiens are full and they need to go to the queue
        if all(openMachines):
            print(i, openMachines)
            if qSize + 1 + data[2] > queueSize:  # If there isn't any space in the queue
                continue
            else:  # If there is space in the queue
                qSize += 1 + data[2]  # Update queue size
                q.append(i)  # Add to queue
                # Process time, 1 if added in queue, 0 if added straight to machine, key for reaccess of data (index)
                heapq.heappush(process, (data[0] + data[3], 1, i))
                atMachine[i] = False  # Add to dict of current status
        # If there is an open voting machine
        else:
            for o in range(len(openMachines)):  # Find the open voting machine
                if not openMachines[o]:
                    print(o, i)
                    openMachines[o] = i + 1
                    result[0] += 1
                    result[o + 1] += 1
                    atMachine[i] = o + 1
                    heapq.heappush(process, (data[0] + data[1], 0, o))
                    break
        print(i, openMachines, q, atMachine, process)
    # Go through remaining process entries if there are any
    while process:
        current, inQueue, index = heapq.heappop(process)
        if not inQueue:  # They need to be moved out of a voting machine
            # atMachine.pop(voterID)
            if q:  # Someone replaces the person leaving
                newVoterIndex = q.pop(0)
                newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                openMachines[index] = newVoterIndex + 1
                qSize -= 1 + newVoterData[2]
                atMachine[newVoterIndex] = index + 1
                result[0] += 1
                result[index + 1] += 1
                heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
            else:  # No one replaces the person leaving
                openMachines[index] = 0
        else:  # Tolerance time was reached but the person may already be at a machine
            if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                voterData = list(map(int, voters[index].split(',')))
                q.remove(index)
                atMachine.pop(index)
                qSize -= 1 + voterData[2]
    print(result)
    return result


#####################################################################

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
Input
-----
voters -
Voter arrival data (array of strings) sorted by arrival timestamp
Format of each entry - "<arrivalTimestamp>,<votingTime>,<numChildren>,<toleranceTime>"
 
numMachines -
Number of voting machines
 
queueSize -
Size of the polling place's queue

Output
------
Return an array of integers of size `numMachines+1` where the 0-th index represents the total number of voters who successfully cast votes and indices 1 to `numMachines` represent the number of votes cast at each voting machine.
"""

import heapq

class queueNode:  # A doubly linked list node for queue representation and O(1) tolerance eviction
    
    def __init__(self, voterID, tail=None, head=None):
        self.value = voterID
        self.prev = tail
        self.next = head
        
class voterQueue:  # A doubly linked list + hashmap for queue representation and O(1) tolerance eviction
    
    def __init__(self):
        self.voters = 0  # Number of voters
        self.map = dict()
        self.head = queueNode(-1)
        self.tail = queueNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, voterID):  # Add voters to the back of the queue
        self.voters += 1
        node = queueNode(voterID)
        self.map[voterID] = node
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node

    def pop(self):  # Remove voters from the front of the queue
        node = self.head.next
        voterID = node.value
        self.voters -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        self.map.pop(voterID)
        return voterID
        
    def remove(self, voterID):  # Remove voters from within the queue when their tolerance is reached
        node = self.map[voterID]
        self.map.pop(voterID)
        self.voters -= 1
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

def solution(voters, numMachines, queueSize):
    result = [0 for _ in range(numMachines + 1)]
    # Could use a segment tree for representing open voting machines
        # Will use a bool array for now
        # Counter for the size of the current queue
    # Priority queue for order of events that need to be processed
    # Use LRU cache system for the queue itself (for tolerance removal)
    
    
    ###############################################################################
    # prototype
    q = voterQueue()
    qSize = 0
    process = []  # Events that need to be processed
    heapq.heapify(process)
    openMachines = [0 for _ in range(numMachines)]  # Available machines
    atMachine = dict()  # True if at machine, false if in the queue
    # Linear search for now, will improve performance later
    for i in range(len(voters)):
        data = list(map(int, voters[i].split(',')))
        # If something needs to be done before this voter is processed
        while process and process[0][0] <= data[0]:
            current, inQueue, index = heapq.heappop(process)
            if not inQueue:  # They need to be moved out of a voting machine
                # atMachine.pop(voterID)
                if q.voters:  # Someone replaces the person leaving
                    newVoterIndex = q.pop()
                    newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                    openMachines[index] = newVoterIndex + 1
                    qSize -= 1 + newVoterData[2]
                    atMachine[newVoterIndex] = index + 1
                    result[0] += 1
                    result[index + 1] += 1
                    heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
                else:  # No one replaces the person leaving
                    openMachines[index] = 0
            else:  # Tolerance time was reached but the person may already be at a machine
                if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                    voterData = list(map(int, voters[index].split(',')))
                    q.remove(index)
                    atMachine.pop(index)
                    qSize -= 1 + voterData[2]
        # If the voting machiens are full and they need to go to the queue
        if all(openMachines):
            if qSize + 1 + data[2] > queueSize:  # If there isn't any space in the queue
                continue
            else:  # If there is space in the queue
                qSize += 1 + data[2]  # Update queue size
                q.add(i)  # Add to queue
                # Process time, 1 if added in queue, 0 if added straight to machine, key for reaccess of data (index)
                heapq.heappush(process, (data[0] + data[3], 1, i))
                atMachine[i] = False  # Add to dict of current status
        # If there is an open voting machine
        else:
            for o in range(len(openMachines)):  # Find the open voting machine
                if not openMachines[o]:
                    openMachines[o] = i + 1
                    result[0] += 1
                    result[o + 1] += 1
                    atMachine[i] = o + 1
                    heapq.heappush(process, (data[0] + data[1], 0, o))
                    break
    # Go through remaining process entries if there are any
    while process:
        current, inQueue, index = heapq.heappop(process)
        if not inQueue:  # They need to be moved out of a voting machine
            # atMachine.pop(voterID)
            if q.voters:  # Someone replaces the person leaving
                newVoterIndex = q.pop()
                newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                openMachines[index] = newVoterIndex + 1
                qSize -= 1 + newVoterData[2]
                atMachine[newVoterIndex] = index + 1
                result[0] += 1
                result[index + 1] += 1
                heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
            else:  # No one replaces the person leaving
                openMachines[index] = 0
        else:  # Tolerance time was reached but the person may already be at a machine
            if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                voterData = list(map(int, voters[index].split(',')))
                q.remove(index)
                atMachine.pop(index)
                qSize -= 1 + voterData[2]
    return result

#################################################################

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
Input
-----
voters -
Voter arrival data (array of strings) sorted by arrival timestamp
Format of each entry - "<arrivalTimestamp>,<votingTime>,<numChildren>,<toleranceTime>"
 
numMachines -
Number of voting machines
 
queueSize -
Size of the polling place's queue

Output
------
Return an array of integers of size `numMachines+1` where the 0-th index represents the total number of voters who successfully cast votes and indices 1 to `numMachines` represent the number of votes cast at each voting machine.
"""

import heapq

# class openMachines:  # A log(n) implementation of finding the best voting machine to use with a segment tree

#     def __init__

class queueNode:  # A doubly linked list node for queue representation and O(1) tolerance eviction
    
    def __init__(self, voterID, tail=None, head=None):
        self.value = voterID
        self.prev = tail
        self.next = head
        
class voterQueue:  # A doubly linked list + hashmap for queue representation and O(1) tolerance eviction
    
    def __init__(self):
        self.voters = 0  # Number of voters
        self.map = dict()
        self.head = queueNode(-1)
        self.tail = queueNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, voterID):  # Add voters to the back of the queue
        self.voters += 1
        node = queueNode(voterID)
        self.map[voterID] = node
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node

    def pop(self):  # Remove voters from the front of the queue
        node = self.head.next
        voterID = node.value
        self.voters -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        self.map.pop(voterID)
        return voterID
        
    def remove(self, voterID):  # Remove voters from within the queue when their tolerance is reached
        node = self.map[voterID]
        self.map.pop(voterID)
        self.voters -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

def solution(voters, numMachines, queueSize):
    result = [0 for _ in range(numMachines + 1)]
    # Could use a segment tree for representing open voting machines
        # Will use a bool array for now
        # Counter for the size of the current queue
    # Priority queue for order of events that need to be processed
    # Use LRU cache system for the queue itself (for tolerance removal)
    
    
    ###############################################################################
    # prototype
    q = voterQueue()
    qSize = 0
    process = []  # Events that need to be processed
    heapq.heapify(process)
    openMachines = [0 for _ in range(numMachines)]  # Available machines
    atMachine = dict()  # True if at machine, false if in the queue
    # Linear search for now, will improve performance later
    for i in range(len(voters)):
        data = list(map(int, voters[i].split(',')))
        # If something needs to be done before this voter is processed
        while process and process[0][0] <= data[0]:
            current, inQueue, index = heapq.heappop(process)
            if not inQueue:  # They need to be moved out of a voting machine
                # atMachine.pop(voterID)
                if q.voters:  # Someone replaces the person leaving
                    newVoterIndex = q.pop()
                    newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                    openMachines[index] = newVoterIndex + 1
                    qSize -= 1 + newVoterData[2]
                    atMachine[newVoterIndex] = index + 1
                    result[0] += 1
                    result[index + 1] += 1
                    heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
                else:  # No one replaces the person leaving
                    openMachines[index] = 0
            else:  # Tolerance time was reached but the person may already be at a machine
                if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                    voterData = list(map(int, voters[index].split(',')))
                    q.remove(index)
                    atMachine.pop(index)
                    qSize -= 1 + voterData[2]
        # If the voting machiens are full and they need to go to the queue
        if all(openMachines):
            if qSize + 1 + data[2] > queueSize:  # If there isn't any space in the queue
                continue
            else:  # If there is space in the queue
                qSize += 1 + data[2]  # Update queue size
                q.add(i)  # Add to queue
                # Process time, 1 if added in queue, 0 if added straight to machine, key for reaccess of data (index)
                heapq.heappush(process, (data[0] + data[3], 1, i))
                atMachine[i] = False  # Add to dict of current status
        # If there is an open voting machine
        else:
            for o in range(len(openMachines)):  # Find the open voting machine
                if not openMachines[o]:
                    openMachines[o] = i + 1
                    result[0] += 1
                    result[o + 1] += 1
                    atMachine[i] = o + 1
                    heapq.heappush(process, (data[0] + data[1], 0, o))
                    break
    # Go through remaining process entries if there are any
    while process:
        current, inQueue, index = heapq.heappop(process)
        if not inQueue:  # They need to be moved out of a voting machine
            # atMachine.pop(voterID)
            if q.voters:  # Someone replaces the person leaving
                newVoterIndex = q.pop()
                newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                openMachines[index] = newVoterIndex + 1
                qSize -= 1 + newVoterData[2]
                atMachine[newVoterIndex] = index + 1
                result[0] += 1
                result[index + 1] += 1
                heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
            else:  # No one replaces the person leaving
                openMachines[index] = 0
        else:  # Tolerance time was reached but the person may already be at a machine
            if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                voterData = list(map(int, voters[index].split(',')))
                q.remove(index)
                atMachine.pop(index)
                qSize -= 1 + voterData[2]
    return result

#####################################################################

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
Input
-----
voters -
Voter arrival data (array of strings) sorted by arrival timestamp
Format of each entry - "<arrivalTimestamp>,<votingTime>,<numChildren>,<toleranceTime>"
 
numMachines -
Number of voting machines
 
queueSize -
Size of the polling place's queue

Output
------
Return an array of integers of size `numMachines+1` where the 0-th index represents the total number of voters who successfully cast votes and indices 1 to `numMachines` represent the number of votes cast at each voting machine.
"""

import heapq, array

class machines:  # A log(n) implementation of finding the best voting machine to use with a segment tree

    def __init__(self, size):
        self.size = size
        self.available = size
        self.full = (self.available == 0)
        self.tree = array.array('i', [0 for _ in range(size * 2 + 2)])
        
    def left(self, index):
        return (index << 1)
        
    def right(self, index):
        return (index << 1) + 1
    
    def updateTree(self, index, left, right, value, target):
        if left == right:
            self.tree[index] = value
            return
        elif (left + right) // 2 >= target:
            self.updateTree(self.left(index), left, (left + right) // 2, value, target)
        else:
            self.updateTree(self.right(index), (left + right) // 2 + 1, right, value, target)
        self.tree[index] = self.tree[self.left(index)] and self.tree[self.right(index)]
    
    def getOpenMachine(self, index, left, right):
        if left == right:
            return right
        elif not self.tree[self.left(index)]:
            return self.getOpenMachine(self.left(index), left, (left + right) // 2)
        elif not self.tree[self.right(index)]:
            return self.getOpenMachine(self.right(index), (left + right) // 2 + 1, right)
            
    def addVoter(self):
        target = self.getOpenMachine(1, 0, self.size)
        self.updateTree(1, 0, self.size, 1, target)
        self.available -= 1
        self.full = (self.available == 0)
        return target
        
    def removeVoter(self, target):
        self.updateTree(1, 0, self.size, 0, target)
        self.available += 1
        self.full = False
        

class queueNode:  # A doubly linked list node for queue representation and O(1) tolerance eviction
    
    def __init__(self, voterID, tail=None, head=None):
        self.value = voterID
        self.prev = tail
        self.next = head
        
class voterQueue:  # A doubly linked list + hashmap for queue representation and O(1) tolerance eviction
    
    def __init__(self):
        self.voters = 0  # Number of voters
        self.map = dict()
        self.head = queueNode(-1)
        self.tail = queueNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, voterID):  # Add voters to the back of the queue
        self.voters += 1
        node = queueNode(voterID)
        self.map[voterID] = node
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node

    def pop(self):  # Remove voters from the front of the queue
        node = self.head.next
        voterID = node.value
        self.voters -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        self.map.pop(voterID)
        return voterID
        
    def remove(self, voterID):  # Remove voters from within the queue when their tolerance is reached
        node = self.map[voterID]
        self.map.pop(voterID)
        self.voters -= 1
        node.prev.next = node.next
        node.next.prev = node.prev


def solution(voters, numMachines, queueSize):
    result = [0 for _ in range(numMachines + 1)]
    # Could use a segment tree for representing open voting machines
    # Priority queue for order of events that need to be processed
    # Use LRU cache system for the queue itself (for tolerance removal)
    
    
    q = voterQueue()
    qSize = 0
    process = []  # Events that need to be processed
    heapq.heapify(process)
    openMachines = machines(numMachines)  # Available machines
    atMachine = dict()  # True if at machine, false if in the queue
    for i in range(len(voters)):
        data = list(map(int, voters[i].split(',')))
        # If something needs to be done before this voter is processed
        while process and process[0][0] <= data[0]:
            current, inQueue, index = heapq.heappop(process)
            if not inQueue:  # They need to be moved out of a voting machine
                if q.voters:  # Someone replaces the person leaving
                    newVoterIndex = q.pop()
                    newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                    qSize -= 1 + newVoterData[2]
                    atMachine[newVoterIndex] = index + 1
                    result[0] += 1
                    result[index + 1] += 1
                    heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
                else:  # No one replaces the person leaving
                    openMachines.removeVoter(index)
            else:  # Tolerance time was reached but the person may already be at a machine
                if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                    voterData = list(map(int, voters[index].split(',')))
                    q.remove(index)
                    atMachine.pop(index)
                    qSize -= 1 + voterData[2]
        # If the voting machiens are full and they need to go to the queue
        if openMachines.full:
            if qSize + 1 + data[2] > queueSize:  # If there isn't any space in the queue
                continue
            else:  # If there is space in the queue
                qSize += 1 + data[2]  # Update queue size
                q.add(i)  # Add to queue
                # Process time, 1 if added in queue, 0 if added straight to machine, key for reaccess of data (index)
                heapq.heappush(process, (data[0] + data[3], 1, i))
                atMachine[i] = False  # Add to dict of current status
        # If there is an open voting machine
        else:
            o = openMachines.addVoter()
            result[0] += 1
            result[o + 1] += 1
            atMachine[i] = o + 1
            heapq.heappush(process, (data[0] + data[1], 0, o))
    # Go through remaining process entries if there are any
    while process:
        current, inQueue, index = heapq.heappop(process)
        if not inQueue:  # They need to be moved out of a voting machine
            if q.voters:  # Someone replaces the person leaving
                newVoterIndex = q.pop()
                newVoterData = list(map(int, voters[newVoterIndex].split(',')))
                qSize -= 1 + newVoterData[2]
                atMachine[newVoterIndex] = index + 1
                result[0] += 1
                result[index + 1] += 1
                heapq.heappush(process, (newVoterData[0] + newVoterData[1], 0, index))
            else:  # No one replaces the person leaving
                openMachines.removeVoter(index)
        else:  # Tolerance time was reached but the person may already be at a machine
            if index in atMachine and not atMachine[index]:  # Person hasn't gone to or been through a machine yet
                voterData = list(map(int, voters[index].split(',')))
                q.remove(index)
                atMachine.pop(index)
                qSize -= 1 + voterData[2]
    return result