
#You can travel: (N)orth or (E)ast or (S)outh or (W)est..
#Victory!

new_location_x = 1
new_location_y = 1

old_location_x = 1
old_location_y = 1

print("You can travel: (N)orth.")
while True:

    old_location_x = new_location_x
    old_location_y = new_location_y

    direction = input("Direction: ")
    if direction in "wW":
        if new_location_x > 1:
            new_location_x -= 1
        else:
            print("Not a valid direction!")
    if direction in "eE":
        if new_location_x < 3:
            new_location_x += 1
        else:
            print("Not a valid direction!")
    if direction in "nN":
        if new_location_y > 1:
            new_location_y -= 1
        else:
            print("Not a valid direction!")
    if direction in "sS":
        if new_location_y < 3:
            new_location_y += 1
        else:
            print("Not a valid direction!")

    if(new_location_x == 1 and new_location_y == 1):
        print("You can travel: (N)orth.")
    if(new_location_x == 1 and new_location_y == 2):
        print("You can travel: (N)orth (S)outh (E)ast.")
    if(new_location_x == 1 and new_location_y == 3):
        print("You can travel: (S)outh (E)ast.")
    if(new_location_x == 2 and new_location_y == 1):
        print("You can travel: (N)orth.")
    if(new_location_x == 2 and new_location_y == 2):
        print("You can travel: (W)est (S)outh.")
    if(new_location_x == 2 and new_location_y == 3):
        print("You can travel: (W)est (E)ast.")
    if(new_location_x == 3 and new_location_y == 1):
        print("Victory!")
        break
    if(new_location_x == 3 and new_location_y == 2):
        print("You can travel: (N)orth (S)outh.")
    if(new_location_x == 3 and new_location_y == 3):
        print("You can travel: (W)est (S)outh.")