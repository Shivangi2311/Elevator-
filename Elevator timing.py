#Programming Coursework:
import random 
#Building :
floor = int(input("PLease enter the number of floors in the building: "))
if floor < 0 :
    new_floor = int(input("Sorry this building does not have basement enter any number more than 0: "))
    print ("The building has",new_floor,"floors")
    floor = new_floor
elif floor == 0 :
    new_floor1 = int(input("This building starts from floor 1 please enter anything above 1: "))
    print ("The building has",new_floor1,"floors")
    floor = new_floor1
#Cannot create an error if in the second try they enter 0 floored building




def lift():
    diff_1 = (abs(current_floor - lift_1))
    diff_2 = (abs(current_floor - lift_2))
    if diff_1 > diff_2 : 
        print ("Lift 2 is coming")
        waiting = (((abs(lift_2 - current_floor))*2)+5)
        print ("Waiting time is ",waiting,"secs")
    else :
        print ("Lift 1 is coming")
        waiting = (((abs(lift_1 - current_floor))*2)+5)
        print ("Waiting time is ",waiting,"secs")
    
    
     

#Lift :
no_of_people = random.randint(0,10)
print ("Number of people in the lift: ",no_of_people)


#lift positions
lift_1 = random.randint(1,floor)
print ("Lift 1 is on floor: ",lift_1)
lift_2 = random.randint(1,floor)
print ("Lift 2 is on floor: ",lift_2)

#Current position of the passenger
current_floor = int(input("Please enter the floor you are currently on: "))
#cannot be more than the height of the building
if current_floor > floor :
    current_position1 = int(input("Please recheck the floor you are on,and re-enter: "))
    print ("You are on floor, ",current_position1)



def time_to_reach():
    #time = current_floor - reach_position
    if current_floor < reach_position :
        time = (((reach_position - current_floor)*2)+5)
        print ("The lift will reach the destination in ",time,"secs")

    elif current_floor > reach_position :
        time = (((current_floor - reach_position)*2)+5)
        print ("The lift will reach the destination in ",time,"secs")
    elif current_floor == reach_position :
        print ("The lift will reach the destination in 5 secs")



    
c = 0
y = 0
n = 0
call = (input("Please press c if you want to call the lift: "))
if call == 'c' :
##    print ("The lift is coming")
    lift()
    reach_position = int(input("Please enter the floor you want to go to: "))
    if reach_position > floor :
    ##    print ("This is building is not so tall")
        call_again = int(input("Please enter floor that is in the building: "))
        time_to_reach()
    else:
        #print ("You will reach the lift in sec")
        time_to_reach()
else  :
    new_call = input("Do you want to call the lift? y or n : ")
    
    if new_call == 'n' :
        print ("Lift is not called")
    elif new_call == 'y' :
        #print ("Lift is coming")
        lift()
        reach_position = int(input("Please enter the floor you want to go to: "))
        if reach_position > floor :
        ##    print ("This is building is not so tall")
            call_again = int(input("Please enter floor that is in the building: "))
            time_to_reach()
        else:
            #print ("You will reach the lift in sec")
            time_to_reach()







    

        
        


















    


        
