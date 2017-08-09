num = int(raw_input("Enter place upto "))
i = 1
a = 0
while (i <= num) :
    temp = i
    b = 1
    while (temp != 0):
        b = b * 10
        temp = temp / 10
    a = (a * b) + i
    i += 1
print a
