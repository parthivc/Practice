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





example = [(0, 0, 'a'), (0, 1, 'c'), (0, 3, 'a'), (0, 0, 'b'), (5, 3, 'a'), (10, 2, 'c')]
example2 = "one fish, two fish"

def decode(encodings):
    result = ''
    for offset, length, char in encodings:
        result += result[offset: offset + length] + char
    return result

print(decode(example) == "aacaacabcababac")

def encode(string):
    offset, length= 1, 1
    encodings = [(0, 0, string[0])]
    result = string[0]
    while len(result) < len(string):
        while offset + length <= len(string) and string[offset: offset + length] in result:
            length += 1
        length -= 1
        i = result.find(string[offset: offset + length])
        if offset + length == len(string):
            length -= 1
        encodings.append((i, length, string[offset + length]))
        result += result[i: i + length] + string[offset + length]
        offset += length + 1
        length = 1
    return encodings

print(encode("aacaacabcababac"))
print(encode(example2))
print(decode(encode(example2)))