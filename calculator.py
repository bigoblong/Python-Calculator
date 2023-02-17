import math
import time
running = True
while running:
    op = input("Operator? (X, /, +, -, %, SR, SQ): ")
    if op.upper() != "X":
        if op.upper() != "/":
            if op.upper() != "+":
                if op.upper() != "-":
                    if op.upper() != "%":
                        if op.upper() != "SR":
                            if op.upper() != "SQ":
                                continue
    
    if op == "SR":
        sum1 = input("Number: ")
        try:
            sum1float = float(sum1)
            if op == "SR":
                print("The square root of ",sum1float, "=", math.sqrt(sum1float))
                repeat = input("Do you want to do another sum? (Y/N) ")
                if repeat.upper() == 'Y':
                    continue
                else:
                    exit()
                    
                        
        except ValueError:
            print("MUST BE A NUMBER")
            continue

    if op == "SQ":
        sum1 = input("Number: ")
        try:
            sum1float = float(sum1)
            if op == "SQ":
                print(sum1float, "squared " "=", sum1float*sum1float)
                repeat = input("Do you want to do another sum? (Y/N) ")
                if repeat.upper() == 'Y':
                    continue
                else:
                    exit()
                    
                        
        except ValueError:
            print("MUST BE A NUMBER")
            continue



    var1 = True
    while var1:
        sum1 = input("Number 1: ")
        try:
            sum1float = float(sum1)
            break
        except ValueError:
            print("MUST BE A NUMBER")
            continue
    
    var2 = True
    while var2:
        sum2 = input("Number 2: ")
        try:
            sum2float = float(sum2)
            break
        except ValueError:
            print("MUST BE A NUMBER") 
            continue

    if op == "X":
        print(sum1float, 'x', sum2float, '=', sum1float*sum2float)

    if op == "/":
        print(sum1float, '/', sum2float, '=', sum1float/sum2float)

    if op == "+":
        print(sum1float, '+', sum2float, '=', sum1float+sum2float)

    if op == "-":
        print(sum1float, '-', sum2float, '=', sum1float-sum2float)

    if op == "%":
        print(sum1float, "percent of", sum2float, '=', sum1float*(sum2float/100))

    repeat = input("Do you want to do another sum? (Y/N) ")
    if repeat.upper() == 'Y':
        continue

    elif repeat != 'Y':
        break
