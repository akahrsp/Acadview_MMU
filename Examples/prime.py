def get_number() :
    return int(raw_input("Enter a no to check it is prime or not "))
num = get_number()
i = 1
a = 0
while (i <= num):
    if num % i == 0 :
        a += 1
    i += 1
if a == 2 :
    print "%d is a prime number" % (num)
else :
    print "%d is a non prime number " % (num)




