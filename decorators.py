def announce(x):
    def some_wrapper():
        print("Should print some function")
        x()
        print("Prints function x")
    return some_wrapper

    #function takes a function, tweeks and modifies it and gives us back an output

@announce
def goodevening():
    print("Good evening")

#announces this function to the decorator

goodevening()


