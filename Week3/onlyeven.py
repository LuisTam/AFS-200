def userNumber():
    while True:
        #Asking user for input
        userInput = input("Please enter positive number: ")
        #Checks to see if input is number if so it stores it as an interger
        if userInput.isdigit():
            number = int(userInput)
            #If input is Postive number is calculates and prints even numbers
            evens = [number for number in range(number) if number % 2 == 0]
            print(evens)
            #Checks to see if it is a positive number
            if number > 0:
                return number
        #Error if no positive number was entered 
        else:
            print("ERROR!!!!")

userNumber()
