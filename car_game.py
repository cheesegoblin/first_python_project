car_start = 'start'   //command to start the car
car_stop = 'stop'    // command to stop the car
quit_game = 'quit'   // command to quit the game

z = 0
w = 0
first_time = 0

y = False
flag = True

print('''
     start car - start
     stop car -stop
     quit game - quit''')

while flag:
    x = input('\n >').lower()

    if x == car_start:
        if x == car_start and not y:                    //condition to start the car
            print('the car has started to run')
            y = True
            first_time = 1
            w = 1
        else:
            print('the car is currently running')       //condition the car is already running
    elif x == car_stop and first_time == 1:
        if x == car_stop and y:
            print('the car has stopped running')        //condition to stop the car
            y = False
            w = 0
        else:                                           //condition that car has stopped already
            print('the car has already stopped running')
            first_time = 0
    elif x == car_stop and first_time == 0:             //condition that car is not running
        print("the car hasn't started yet")

    elif x == quit_game:
        if w == 0:                                       //condition to quit the game
            break
        else:
            print('stop the car first to quit the game') //condition for qitting the game

    else:
        print("don't understand command")
