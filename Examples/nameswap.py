name = raw_input("what is your name ")
num = len(name)
name1 = list(name)
i = 1
while (i <= num/2) :
    temp = name1 [i - 1]
    name1 [i - 1] = name1 [num - i]
    name1 [num - i] = temp
    i = i + 1
name = ''.join(name1)
print name