import random

TYPE = [
    "R",
    "S",
    "P",
]


def r_s_p():
    p1 = input("ENter your choice: ")
    p2 = random.choice(["P", "R", "S"])

    if p1 == "R":
        if p2 == "S":
            print("P1 wins")
        elif p2 == "P":
            print("P2 wins")
        else:
            print("Tie")
    elif p1 == "S":
        if p2 == "P":
            print("P1 wins")
        elif p2 == "R":
            print("P2 wins")
        else:
            print("Tie")
    elif p1 == "P":
        if p2 == "R":
            print("P1 wins")
        elif p2 == "S":
            print("P2 wins")
        else:
            print("Tie")
    else:
        print("Invalid input")

r_s_p()