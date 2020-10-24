# 
# Your previous Plain Text content is preserved below:
# 
# LZ77
# string -> [(offset, length, char)]
# 
# one fish, two fish
#    ^^^^
# 
# (3, 4, 'h')
# 
# aacaacabcababac
# 
# aaa


#  K point 
# Chess game 
# Backend API for tasks 





example = [(0,0,'a'),(0,1,'c'),(0,3,'a'),(0,0,'b'),(5,3,'a'),(10,2,'c')]
example2 = "one fish, two fish"
# 
def decode(encodings):
    currStr = ''
    for offset, length, char in encodings:
        currStr += currStr[offset:offset+length]+char
    return currStr

print(decode(example) == "aacaacabcababac")

def encode(string):
    # currStr =''
    offset,length=1,1
    # currSearch=''
    encodings = [(0,0,string[0])]
    # encodings.append((0,0,string[offset]))
    currStr = string[0]
    # offset+=1

    while len(currStr) < len(string):
        while offset+length <= len(string) and string[offset:offset+length] in currStr:
            length+=1
        length-=1
        idx = currStr.find(string[offset:offset+length])
        # print(f'{currStr} and {offset} and {length} and {idx}')
        # print(f'found string is {string[offset:offset+length-1]}')
        # if idx == -1:
        #     encodings.append((0,0,string[offset]))
        #     currStr += string[offset]
        #     offset+=1
        # else:
        if offset+length == len(string):
            encodings.append((idx,length-1,string[offset+length-1]))
            currStr += currStr[idx:idx+length-1]+string[offset+length-1]
            offset+=length
        else:
            encodings.append((idx,length,string[offset+length]))
            currStr += currStr[idx:idx+length]+string[offset+length]
            offset+=length+1
        length=1
    return encodings

print(encode("aacaacabcababac"))
print(encode(example2))
print(decode(encode(example2)))