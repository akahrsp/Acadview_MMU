num = int(raw_input("Enter the decimal no to convert into hexadecimal : - "))
i = 0
hex = []
while (num != 0) :
    rem = num % 16
    if rem < 10 :
        hex.insert( i, str(rem))
    elif rem == 10 :
        hex.insert(i, "A")
    elif rem == 11 :
        hex.insert(i, "B")
    elif rem == 12 :
        hex.insert(i, "C")
    elif rem == 13 :
        hex.insert(i, "D")
    elif rem == 14 :
        hex.insert(i, "E")
    elif rem == 15 :
        hex.insert(i, "F")
    i += 1
    num = num / 16
hex = reversed(hex)
number = "".join(hex)
print number