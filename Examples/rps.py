p = 'y'
while (p == 'y') :
    choice1 = int(raw_input("First Player \nEnter your Choice \n1. For rock\n2. For paper \n3. For scissors  "))
    choice2 = int(raw_input("Second Player \nEnter your Choice \n1. For rock\n2. For paper \n3. For scissors  "))
    if choice2 == choice1 + 1 :
        print 'Player 2 wins'
    elif choice1 == choice2 + 1 :
        print 'Player 1 wins'
    elif choice2 == choice1 + 2 :
        print 'Player 2 wins'
    elif choice1 == choice2 + 2 :
        print 'Player 1 wins'
    else :
        print 'its a tie'
    p = raw_input("Wanna play more (y/n)")

print 'Thank you'