#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'We recommend'


number = int(input("What number would you like to input?"))

# go to a number of 4
if number == 1:
    message = message + ' Harry Potter because it is a great series!'
elif number == 2:
    message = message + ' The Hobbit because it is magical!'
elif number == 3:
    message = message + ' Narnia because of Aslan'
elif number == 4:
    message = message + ' Indiana jones if you like adventure'
else:
    message = message + ' something else'
print(message)













