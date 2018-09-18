
new_location_x = 1
new_location_y = 1

allowTravel_North = True
allowTravel_South = False
allowTravel_East = False
allowTravel_West = False

print("You can travel: (N)orth.")
while True:

    #print("Previous location : {},{}".format(new_location_x,new_location_y))
    direction = input("Direction: ")

    if direction in "wW" and allowTravel_West == True:
        if new_location_x > 1 and new_location_x <= 3:
            new_location_x -= 1
        else:
            print("Not a valid direction!")
            continue
    elif direction in "wW" and allowTravel_West == False:
        print("Not a valid direction!")
        continue

    if direction in "eE" and allowTravel_East == True:
        if new_location_x >= 1 and new_location_x < 3:
            new_location_x += 1
        else:
            print("Not a valid direction!")
            continue
    elif direction in "eE" and allowTravel_East == False:
        print("Not a valid direction!")
        continue

    if direction in "nN" and allowTravel_North == True:
        if new_location_y >= 1 and new_location_y < 3:
            new_location_y += 1
        else:
            print("Not a valid direction!")
            continue
    elif direction in "nN" and allowTravel_North == False:
        print("Not a valid direction!")
        continue

    if direction in "sS" and allowTravel_South == True:
        if new_location_y > 1 and new_location_y <= 3:
            new_location_y -= 1
        else:
            print("Not a valid direction!")
            continue
    elif direction in "sS" and allowTravel_South == False:
        print("Not a valid direction!")
        continue

    ##################################################3
    if(new_location_x == 1 and new_location_y == 1):
        print("You can travel: (N)orth.")
        allowTravel_North = True
        allowTravel_South = False
        allowTravel_East = False
        allowTravel_West = False
    if(new_location_x == 1 and new_location_y == 2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        allowTravel_North = True
        allowTravel_South = True
        allowTravel_East = True
        allowTravel_West = False
    if(new_location_x == 1 and new_location_y == 3):
        print("You can travel: (E)ast or (S)outh.")
        allowTravel_North = False
        allowTravel_South = True
        allowTravel_East = True
        allowTravel_West = False
    if(new_location_x == 2 and new_location_y == 1):
        print("You can travel: (N)orth.")
        allowTravel_North = True
        allowTravel_South = False
        allowTravel_East = False
        allowTravel_West = False
    if(new_location_x == 2 and new_location_y == 2):
        print("You can travel: (S)outh or (W)est.")
        allowTravel_North = False
        allowTravel_South = True
        allowTravel_East = False
        allowTravel_West = True
    if(new_location_x == 2 and new_location_y == 3):
        print("You can travel: (E)ast or (W)est.")
        allowTravel_North = False
        allowTravel_South = False
        allowTravel_East = True
        allowTravel_West = True
    if(new_location_x == 3 and new_location_y == 1):
        print("Victory!")
        break
    if(new_location_x == 3 and new_location_y == 2):
        print("You can travel: (N)orth or (S)outh.")
        allowTravel_North = True
        allowTravel_South = True
        allowTravel_East = False
        allowTravel_West = False
    if(new_location_x == 3 and new_location_y == 3):
        print("You can travel: (S)outh or (W)est.")
        allowTravel_North = False
        allowTravel_South = True
        allowTravel_East = False
        allowTravel_West = True