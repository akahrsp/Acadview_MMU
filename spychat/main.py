print 'Let\'s get Started...'
spy_name = raw_input('What is you Name ? : ')
if len(spy_name) > 0 :
    #logic will be here if condition is true
    spy_salutation = raw_input('What should we call you?')
    spy_name = spy_salutation + ' ' + spy_name
    print 'Welcome ' + spy_name + ' Glad to have you back with us.'
