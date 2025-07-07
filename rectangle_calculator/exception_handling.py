'''
try: 
    # print(x)
except NameError:
    # print("Variable 'x' is not defined")
finally:
    # print("Everything went wrong")
'''

try: 
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' block is complete")

x= -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

