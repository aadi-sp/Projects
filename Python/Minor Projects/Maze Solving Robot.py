#This is the code to solve the maze challenge on the website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    for i in range(3):
        turn_left() #This function is pre-declared in the website
def turn_around():
    for i in range(2):
        turn_left()


while not at_goal(): #This function is pre-declared in the website
    if not wall_in_front(): #This function is pre-declared in the website
        move() #This function is pre-declared in the website
    elif wall_on_right(): #This function is pre-declared in the website
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        move()
