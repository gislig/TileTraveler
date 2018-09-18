
#You can travel: (N)orth or (E)ast or (S)outh or (W)est..
#Victory!

new_location_x = 1
new_location_y = 1

print("You can travel: (N)orth.")
while True:

    direction = input("Direction: ")
    if direction in "wW":
        if new_location_x > 1:
            new_location_x -= 1
            print(str(new_location_x))
        else:
            print("Not a valid direction!")
    if direction in "eE":
        if new_location_x < 3:
            new_location_x += 1
            print(str(new_location_x))
        else:
            print("Not a valid direction!")
    if direction in "nN":
        if new_location_y > 1:
            new_location_y -= 1
            print(str(new_location_y))
        else:
            print("Not a valid direction!")
    if direction in "sS":
        if new_location_y < 3:
            new_location_y += 1
            print(str(new_location_y))
        else:
            print("Not a valid direction!")