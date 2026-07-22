# Program prints a prime number and asks the user if they would like the next one, stops when the user says no.

# Initial value of the looping number, increments by 1 and checks if its a prime number.
currentValue = 0
keepLoop = True

# Need to figure this out, I know somethings wrong with the first couple of lines at least lol
for keepLoop in True:
    if not keepLoop:
        print("Program complete")
        break
    else:
        currentValue += 1
        for i in range(2,currentValue):
            if (currentValue%i==0):
                answer = input(currentValue + " is a prime number, would you like the next one?: ")
                if answer.lower() == "yes":
                    continue
                else:
                    keepLoop = False