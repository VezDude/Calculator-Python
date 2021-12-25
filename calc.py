import time

def add():
    n1 = int(input("Enter First Number: "))
    print()
    n2 = int(input("Enter Second Number: "))
    print()
    n3 = int(input("Enter Third Number [IF NONE, TYPE '0']: "))
    print()
    n4 = int(input("Enter Fourth Number [IF NONE, TYPE '0']: "))
    print()
    n5 = int(input("Enter Fifth Number [IF NONE, TYPE '0']: "))
    print()
    n6 = int(input("Enter Sixth Number [IF NONE, TYPE '0']: "))
    print()
    n7 = int(input("Enter Seventh Number [IF NONE, TYPE '0']: "))
    print()
    n8 = int(input("Enter Eighth Number [IF NONE, TYPE '0']: "))
    print()
    n9 = int(input("Enter NinethNumber [IF NONE, TYPE '0']: "))
    print()
    n10 = int(input("Enter Tenth Number [IF NONE, TYPE '0']: "))
    print()
    n11 = int(input("Enter Eleventh Number [IF NONE, TYPE '0']: "))
    print()
    n12 = int(input("Enter Twelveth Number [IF NONE, TYPE '0']: "))
    print()
    time.sleep(2)
    ans1 = n1 + n2 + n3 + n4 + n5 + n6 +n7 + n8 + n9 + n10 + n11 + n12
    print(ans1)

def sub():
    n1 = int(input("Enter First Number: "))
    print()
    n2 = int(input("Enter Second Number: "))
    print()
    n3 = int(input("Enter Third Number [IF NONE, TYPE '0']: "))
    print()
    n4 = int(input("Enter Fourth Number [IF NONE, TYPE '0']: "))
    print()
    n5 = int(input("Enter Fifth Number [IF NONE, TYPE '0']: "))
    print()
    n6 = int(input("Enter Sixth Number [IF NONE, TYPE '0']: "))
    print()
    n7 = int(input("Enter Seventh Number [IF NONE, TYPE '0']: "))
    print()
    n8 = int(input("Enter Eighth Number [IF NONE, TYPE '0']: "))
    print()
    n9 = int(input("Enter NinethNumber [IF NONE, TYPE '0']: "))
    print()
    n10 = int(input("Enter Tenth Number [IF NONE, TYPE '0']: "))
    print()
    n11 = int(input("Enter Eleventh Number [IF NONE, TYPE '0']: "))
    print()
    n12 = int(input("Enter Twelveth Number [IF NONE, TYPE '0']: "))
    print()
    ans2 = n1 - n2 - n3 - n4 - n5 - n6 - n7 - n8 - n9 - n10 - n11 - n12
    print(ans2)

def mul():
    n1 = int(input("Enter First Number: "))
    print()
    n2 = int(input("Enter Second Number: "))
    print()
    ans3 = n1 * n2
    print(ans3)

def div():
    n1 = int(input("Enter First Number: "))
    print()
    n2 = int(input("Enter Second Number: "))
    print()
    ans4 = n1 / n2
    print(ans4)


head = '''
CALCULATOR
'''
time.sleep(1)
print(head)
print()
print("Choose an Operator -\n[1] = Add\n[2] = Subtract\n[3] = Multiply\n[4] = Divide\n\n")
ch = input("")
if ch == "1":
    add()
elif ch == "2":
    sub()
elif ch == "3":
    mul()
elif ch == "4":
    div()
else:
    print()
    print("WTF ?")
    time.sleep(2)
    quit()
