import random

ch = "y"
i = 0
num = random.randint(1,9)
while (ch != "n") :
    guess = int(raw_input("Enter no from 1 to 9 : "))
    if( guess > 0 and guess < num) :
        print " your guess is too low"
    elif (guess > num and guess < 10) :
        print " your guess is too high "
    elif (guess == num ) :
        print " your guess is right "
    else :
        print "wrong input"
        break
    i = i + 1
    print "no of tries = %d" % (i)
    ch = raw_input("you wanna play or exit (y/n): - ")
