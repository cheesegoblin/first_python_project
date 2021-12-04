car_start = 'start'
car_stop = 'stop'
quit_game = 'quit'
z = 0
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
        if x == car_start and not y:
            print('the car has started to run')
            y = True
            first_time = 1
        else:
            print('the car is currently running')
    elif x == car_stop and first_time == 1:
        if x == car_stop and y:
            print('the car has stopped running')
            y = False

        else:
            print('the car has already stopped running')
            first_time = 0
    elif x == car_stop and first_time == 0:
        print("the car hasn't started yet")

    elif x == quit_game:
        break

    else:
        print("dont understand command")