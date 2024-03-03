# Elevator-

A tall office building contains 2 lifts. Each lift starts out in the lobby (the “1” floor).
When a button next to the lift door on a particular floor is pressed, then the building
sends the nearest lift (in terms of distance) to that floor. The lift then travels to the
required floor and stays there until summoned again by the building. To simplify
matters the lifts move one at a time.

Elevator Timing:

1) Building - this represents the building itself. It must have a member variable to
represent the number of floors.
2) Lift - this represents a single lift. It must have a member variable to represent the
current position of the lift
It takes a lift 2 seconds to move up or down a single floor plus 5 seconds to get started
and slow down again. Thus to move ten floors it takes:
(10 * 2) + 5 = 25 seconds.
Simulating a building has 2 lifts aggregated inside it. The
building will thus be responsible for the creation of each lift.

Elevator Efficiency:

Main method that emulates the behaviour of a lift and then from the history
data to find the average waiting time for a lift, by repeatedly calling a lift to a random
floor (I suggest 1000 calls would give you a good approximation) and making it travel
to a second random destination floor. You will need to implement a while loop to do
this as well as use the random () library.
Imagine that the lifts were not made by same manufacturer and that they have a
second variable, efficiency that will act as a modifier to the time taken to move
between floors (e.g. an efficiency of 0.5 meant it took half the time). 
