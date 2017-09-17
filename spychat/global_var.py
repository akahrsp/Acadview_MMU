from add_friend import spy_add
status = ['too busy', 'Available', 'At mission']
def select_friend():
    counter = 1
    x = 0
    while x < len(spy_add) :
        print str(x+1) + ". "+ spy_add[x].name
        counter += 1
        x += 1

    choice = int(raw_input("Choose the friend from the list : "))
    if choice <= counter:
        return choice - 1
    else:
        print "Wrong choice"
        exit(0)
def ty() :
    print "thank you!!! \n project crated by :- Anup Kumar Aditya 3rd year"