def SetSteps(current_step, add_or_remove_step):
    valid_step = True
    if add_or_remove_step in "nNeE" and current_step+1 > 1 and current_step+1 <= 3:
        current_step += 1
    elif add_or_remove_step in "sSwW" and current_step-1 >= 1 and current_step-1 <= 3:
        current_step -= 1
    else:
        print("Not a valid direction!")
        valid_step = False

    return current_step, valid_step

new_location_x = 1
new_location_y = 1
valid_direction = False

allowTravel_North = True
allowTravel_South = False
allowTravel_East = False
allowTravel_West = False

print("You can travel: (N)orth.")
while True:
    direction = input("Direction: ")
    if direction in 'nN' and allowTravel_North == True:
        new_location_y, valid_direction = SetSteps(new_location_y, direction)
    elif direction in 'nN' and allowTravel_North == False:
        print("Not a valid direction!")
        continue

    if direction in 'eE' and allowTravel_East == True:
        new_location_x, valid_direction = SetSteps(new_location_x, direction)
    elif direction in 'eE' and allowTravel_East == False:
        print("Not a valid direction!")
        continue

    if direction in 'sS' and allowTravel_South == True:
        new_location_y, valid_direction = SetSteps(new_location_y, direction)
    elif direction in 'sS' and allowTravel_South == False:
        print("Not a valid direction!")
        continue

    if direction in 'wW' and allowTravel_West == True:
        new_location_x, valid_direction = SetSteps(new_location_x, direction)
    elif direction in 'wW' and allowTravel_West == False:
        print("Not a valid direction!")
        continue
    
    #print("Previous location : {},{}".format(new_location_x,new_location_y))

    if valid_direction == False:
        continue

    ##################################################
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