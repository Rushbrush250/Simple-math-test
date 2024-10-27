S = 0
print("Let's do a math test")

Pa = input("If 15x = 75, what is x? ")
if int(Pa) == 5:
    print("Correct")
    S += 1
else:
    print("Wrong")

Pb = input("If you have 30 apples and 2 oranges, what is the ratio of apples to oranges? ")
if int(Pb) == 15:
    print("Correct")
    S += 1
else:
    print("Wrong")

Pc = input("What is 10 + 3 times 4? ")
if int(Pc) == 22:
    print("Correct")
    S += 1
else:
    print("Wrong")

print(f"You're done with the test. You scored {S} out of 3.")
