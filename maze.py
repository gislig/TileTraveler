
#You can travel: (N)orth or (E)ast or (S)outh or (W)est..
#Victory!

location = 1,1

print("You can travel: (N)orth.")
while True:
    
    direction = input("Direction: ")
    if direction in "wW":
        print("Going West")
    if direction in "nN":
        print("Going North")
    if direction in "sS":
        print("Going South")
    if direction in "eE":
        print("Going East")