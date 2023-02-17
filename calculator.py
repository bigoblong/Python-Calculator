import time
import sys
running = True
while running:
    op = input("Operator? (X, /, +, -): ")
    if op != "X":
        if op != "/":
            if op != "+":
                if op != "-":
                    continue
    sum1 = input("Number 1: ")
    try:
        floatsum1 = float(sum1)
    except ValueError:
        print("MUST BE A NUMBER")
        continue
    
    sum2 = input("Number 2: ")
    try:
        floatsum2 = float(sum2)
    except ValueError:
        print("MUST BE A NUMBER")
        continue   

    if op == "X":
        print(floatsum1, 'x', floatsum2, '=', floatsum1*floatsum2)

    if op == "/":
        print(floatsum1, '/', sum2, '=', floatsum1/floatsum2)

    if op == "+":
        print(floatsum1, '+', sum2, '=', floatsum1+floatsum2)

    if op == "-":
        print(floatsum1, '-', sum2, '=', floatsum1-floatsum2)

    repeat = input("Do you want to do another sum? (Y/N) ")
    if repeat == 'Y':
        continue

    elif repeat != 'Y':
        break
