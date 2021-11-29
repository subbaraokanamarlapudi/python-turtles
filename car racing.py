import msvcrt
import time

high_score = 17.78
name = "KVSR"
while True:
    distance = int(0)
    print('\n-----------------------------------------------------------------------------------------------------')
    print('\n\nWelcome to the 100m sprint, tap z and x rapidly to move!')
    print('* = 100m')
    print('\nCurrent record: ' + str(high_score) + ' by: ' + name)
    print('\nPress enter to start')
    input ()
    print('Ready.......')
    time.sleep(1)
    print('Go!')

    start_time = time.time()
    while distance < 10:
        k1 = msvcrt.getch().decode('ASCII')
        if k1 == 'z':
            k2 = msvcrt.getch().decode('ASCII')
            if k2 == 'x':
                distance += 1

                if distance == 5:
                    print("* you're halfway there!")
                elif distance  % 1 == 0:
                    print('*')

    fin_time = time.time() - start_time
    fin_time = round(fin_time ,2)
    
    
    print('Congrulations on successfully completing the race!')
    print('You took', fin_time, 'seconds to reach the finish line')

    if fin_time < high_score:
        print("Well done you've got a new high score ")
        
        name = input("Please enter your name : ")
        high_score = fin_time