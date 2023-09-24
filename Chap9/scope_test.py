def scope_test():
    print("Starting scope_test()")
    def do_local():
        spam = "local spam"#this is in the local scope of this function
        print("Tried, in a local scope, to set spam to local spam")

    def do_nonlocal():
        nonlocal spam#this is the only one that will affect the value of spam in scope_test() scope
        spam = "nonlocal spam"

    def do_global():
        global spam#this will set the value of spam in the module scope only
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment, spam value is still ", spam, " didn't affect value in the scope_test() scope")
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    #print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
