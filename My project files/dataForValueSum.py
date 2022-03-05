"""
I got this data by taking a screenshot of a winning state of this guy program

https://ovolve.github.io/2048-AI/

I ran his program 25 times , and it succeeded 23 times
this means that the accuracy of his program is 92%

"""

data = []
data.append(2+2+2+4+16+32+2048)
data.append(2+2+2+4+4+8+8+8+2048)
data.append(2+2+2+4+4+8+8+16+128+2048)
data.append(4+4+4+4+4+16+64+2048)
data.append(2+2+2+4+16+16+32+2048)

data.append(2+4+4+8+8+16+2048)
data.append(2+2+2+4+8+8+32+2048)
data.append(2+2+4+4+8+8+16+64+2048)
data.append(2+2+4+4+8+8+2048)

data.append(2+2+4+4+8+16+16+2048)
data.append(2+4+4+4+4+8+64+2048)
data.append(2+2+4+4+8+8+16+16+2048)
data.append(2+2+2+4+4+16+16+2048)

data.append(2+2+4+4+4+4+8+16+16+2048)
data.append(2+2+4+4+4+4+8+8+16+2048)
data.append(2+2+2+4+4+4+8+8+16+16+2048)
data.append(2+4+4+4+4+8+32+2048)
data.append(2+2+2+2+2+4+8+8+8+2048)

data.append(2+2+2+2+2+4+4+8+32+32+2048)
data.append(2+4+4+4+8+8+8+16+128+2048)
data.append(2+2+2+4+4+4+8+32+32+2048)
data.append(2+2+2+4+4+8+8+16+2048)
data.append(2+2+4+8+16+16+32+64+2048)

print(data)
print(sum(data)/len(data))#this is the average used in sum_of_values evaluation
