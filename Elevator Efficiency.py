#Programming Coursework:
import random 
#Building :
wait_time_1 = []
wait_time_2 = []
floor = int(input("PLease enter the number of floors in the building: "))
if floor < 0 :
    new_floor = int(input("Sorry this building does not have basement enter any number more than 0: "))
    print ("The building has",new_floor,"floors")
elif floor == 0 :
    new_floor1 = int(input("This building starts from floor 1 please enter anything above 1: "))
    print ("The building has",new_floor1,"floors")

#Cannot create an error if in the second try they enter 0 floored building
print("The lift takes total of 5 seconds to open and close")
travel_speed_1 = (float(input("Please enter the travel speed between floors you would like for lift 1 to have: ")))
travel_speed_2 = (float(input("Please enter the travel speed between floors you would like for lift 2 to have: ")))
##print (travel_speed_1)
##print(travel_speed_2)

def lift():
    waiting_1 = (((abs(lift_1-current_floor))*travel_speed_1)+5)
    print ("Waiting time for lift 1 is ",waiting_1,"secs")
    wait_time_1.append(waiting_1)
    waiting_2 = (((abs(lift_2 - current_floor))*travel_speed_2)+5)
    print ("Waiting time for lift 2 is ",waiting_2,"secs")
    wait_time_2.append(waiting_2)
    


def time_to_reach():
    #time = current_floor - reach_position
    time_1 = (((abs(current_floor - reach_position))*travel_speed_1)+5)
    time_2 = (((abs(current_floor - reach_position))*travel_speed_2)+5)
    print ("Time taken to reach destination by lift 1 is ",time_1,"secs")
    print ("Time taken to reach destination by lift 2 is ",time_2,"secs")



count = 0
while count < 1000 :
    lift_1 = random.randint(1,floor)
    print ("Lift 1 is on floor: ",lift_1)
    lift_2 = random.randint(1,floor)
    print ("Lift 2 is on floor: ",lift_2)
    
    current_floor = random.randint(1,floor)
    print ("You are currently on floor",current_floor)
    lift ()
    reach_position = random.randint (1,floor)
    print ("Your destination floor is",reach_position)
    time_to_reach()
    
    count = count +1
    
sum_of_wait_travel_time_1 = sum(wait_time_1)
sum_of_wait_travel_time_2 = sum(wait_time_2)
print("The sum of waiting time for lift 1 is : ",round(sum_of_wait_travel_time_1,0))
print("The sum of waiting time for lift 2 is : ",round(sum_of_wait_travel_time_2,0))
average_wait_time_1 = sum_of_wait_travel_time_1 / len(wait_time_1)
print ("The average waiting time for lift 1 is : ",average_wait_time_1)
average_wait_time_2 = sum_of_wait_travel_time_2 / len(wait_time_2)
print ("The average waiting time for lift 2 is : ",average_wait_time_2)
if average_wait_time_1 > average_wait_time_2 :
    print ("Lift 2 is more efficient")
elif average_wait_time_1 == average_wait_time_2:
    print("They are equally efficient")
else :
    print("Lift 1 is more efficient")


        
        


















    


        
