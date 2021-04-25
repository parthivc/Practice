"""

q1: RLE

=============================================================

q2: run length segment encoding:
Instead of one string, you receive a datastream of 'segments'
ab -> [(a,1)]
bcc -> [(b,2)]
cddd -> [(c,3)]
ef -> [(d,4), (e,1)]

=============================================================

q3: run length segment encoding:

The following messages are formatted:
time received, segment #, value

1 1 bcc --> []
2 2 cdddd --> []
3 0 ab --> [(a,1), (b,2), (c,3)]
4 4 ef --> [(d,4), (e,1)] 

=============================================================

Followup: Cache RLE segments already encoded

"""



class jsRLE:

    def __init__(self):
        self.segments = dict()
        self.current = []
        self.segment = 0
        self.char = ""
        self.count = 0

    def reset(self):
        print()
        self.segments = dict()
        self.current = []
        self.segment = 0
        self.char = ""
        self.count = 0

    def process(self, segment, full=False):
        self.current = []
        if segment:
            char, count = self.char, self.count
            for current in segment:
                if current == char:
                    count += 1
                else:
                    if char:
                        self.current.append((char, count))
                    char = current
                    count = 1
            if full:
                self.current.append((char, count))
            self.char, self.count = char, count
        return self.current

    def q3(self, segmentID, segment):
        self.current = []
        self.segments[segmentID] = segment
        if segmentID == self.segment and not (segmentID == 0 and 1 not in self.segments):  # segment that is needed to continue
            result = []
            while self.segment in self.segments:
                result += self.process(self.segments[self.segment])
                self.segment += 1
            self.current = result
        return self.current


def main():
    rle = jsRLE()
    test1 = "wwwwaaadexxxxxxywww"
    test2 = ["ab", "bcc", "cdddd", "ef"]
    test3 = [(1, "bcc"), (2, "cdddd"), (0, "ab"), (3, "ef")]
    rle.reset()
    print(rle.process(test1, True))
    rle.reset()
    for elem in test2:
        print(rle.process(elem))
    rle.reset()
    for count, segment in test3:
        print(rle.q3(count, segment))
    rle.reset()


if __name__ == "__main__":
    main()
