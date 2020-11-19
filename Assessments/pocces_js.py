'''
q1: Run length encoding:

"aaabbaa" -> [(a,3), (b,2), (a,2)]


q2: run length segment encoding:
Instead of one string, you receive a datastream of 'segments'

ab -> [(a,1)]
bcc -> [(b,2)]
cddd -> [(c,3)]
ef -> [(d,4), (e,1)]


q3 same as q2, except the segments can come "out of order"
maybe sort of similar to drw 2020 q1?

1 bcc -> []
2 cdddd -> []
0 ab -> [(a,1), (b,2), (c,3)]
3 ef -> [(d,4), (e,1)]

2 cdddd -> []
1 bcc -> []
0 ab -> [(a,1), (b,2), (c,3)]
3 ef -> [(d,4), (e,1)]
'''

from collections import defaultdict
from heapq import heappush, heappop

class SegmentReceiver():
    def __init__(self):
        self.prev = "" # q2
        self.count = 1 # q2

		# q3
        self.table = {}
        self.active_num = 0
        self.prev_res = []

    # q3
    def on_unordered_segment_received(self, num, s):
        res = self.prev_res
        if(self.active_num not in self.table):
            self.table[num] = self.encode(s, 1, stream=False)[0]
        while(self.active_num in self.table):
            res = self.merge_lists(res, self.table[self.active_num])
            self.active_num+=1
            if(self.active_num not in self.table):
                val = res.pop()
                self.prev_res = [val]
        return res

    # q2
    def on_segment_received(self, s):
        c_count = 1
        l = []
        if(s[0] == self.prev):
            c_count = self.count+1
        elif(s[0] != self.prev and self.prev != ""):
            l.append((self.prev, self.count))
        l2, self.prev, self.count = self.encode(s, c_count)
        for i in range(len(l2)):
            l.append(l2[i])
        return l

    # q1 if curr_count = 1 and stream = False
    # q2 if curr_count = c_count and stream = True
    def encode(self, s, curr_count, stream=True):
        l = []
        if(len(s) == 0):
            return l
        prev = s[0]
        count = curr_count
        for i in range(1, len(s)):
            if(s[i] == s[i-1]):
                count+=1
            else:
                l.append((prev, count))
                prev = s[i]
                count = 1
        if(not stream):
            l.append((prev, count))

        # returns encoding in l, the last character received, and the count of the last character (for use in a potential next string)
        return l, s[-1], count

    # helps with q3
    def merge_lists(self, s1, s2):
        l = []
        if(not s2):
            return s1
        if(not s1):
            return s2
        start = 0
        for i in range(len(s1)-1):
            l.append(s1[i])
        if(s1[-1][0] == s2[0][0]):
            start = 1
            new_val = (s1[-1][0], s1[-1][1]+s2[0][1])
            l.append(new_val)
        else:
            l.append(s1[-1])
        for i in range(start, len(s2)):
            l.append(s2[i])
        return l


if __name__ == "__main__":
    sr = SegmentReceiver()
    # q1
    table = [
        ["aaaabbaa", [("a",4), ("b",2), ("a", 2)]],
    ]
    for i in table:
        assert i[1] == sr.encode(i[0], 1, stream=False)[0]

    #q2
    table = [
        [["ab", "bcc", "cdddd", "ef"], [('a', 1)], [('b', 2)], [('c', 3)], [('d', 4), ('e', 1)]],
        [["ab", "bcc", "cdddd", "ef", "ffffg"], [('a', 1)], [('b', 2)], [('c', 3)], [('d', 4), ('e', 1)], [('f', 5)]],
    ]
    for i in table:
        srX = SegmentReceiver()
        segments = i[0]
        for j in range(len(segments)):
            assert i[j+1] == srX.on_segment_received(segments[j])
    

    # q3
    table = [
        [[ (1, "bcc"), (2, "cdddd"), (0, "ab"), (3, "ef") ], [], [], [('a', 1), ('b', 2), ('c', 3)], [('d',4), ('e',1)]], 
        [[ (2, "cdddd"), (1, "bcc"), (0, "ab"), (3, "ef") ], [], [], [('a', 1), ('b', 2), ('c', 3)], [('d',4), ('e',1)]],
        [[ (3, "ef"), (2, "cdddd"), (1, "bcc"), (0, "ab") ], [], [], [], [('a', 1), ('b', 2), ('c', 3), ('d',4), ('e',1)]],
    ]

    for i in table:
        srX = SegmentReceiver()
        segments = i[0]
        for j in range(len(segments)):
            assert i[j+1] == srX.on_unordered_segment_received(segments[j][0], segments[j][1])
