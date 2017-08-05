def add (first , second):
    return first + second

num = int(raw_input("Enter how many fibonacci no you want "))
sec = 1
fir = 0
i = 1
while (i <= num ) :
    print '%d ' % (sec)
    temp = sec
    sec = add(sec , fir)
    fir = temp
    i = i + 1