import time, sys

indent = 0 #How many spaces to indent
indentIncreasing = True #Whether the indents are increasing or not

try:
    while True: # The main loop of the program
        print(" " * indent, end=" ") # space*indent = number of spaces to print
        print("$$$$$$$$$$")
        time.sleep(0.1) #Pasue for 1/10 of a second

        if indentIncreasing:
            indent += 1 #increase the number of spaces
            if indent == 20:
                indentIncreasing = False #Change Direction

        else:
            indent -= 1 #Decrease the number of spaces
            if indent == 0:
                indentIncreasing = True #Change Direction
except KeyboardInterrupt:
    sys.exit()
