# What is the task you are trying to accomplish? What is the goal? 

 

# What do you think the problem or impediment is? 

 

# What have you specifically tried in your code? 

 

# What did you learn by dropping a breakpoint? 





# (5 points): As a developer, I want to make at least three commits with descriptive messages 

# commit after outline
# commit frequently after lines of code
# commit before review/edit
# commit before submition




introduction = "Welcome to Day Trip Generator!"


print(introduction)

# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, 
# and entertainment in their own separate Lists. 


destinations =["Hogwarts Castle","Diagon Ally","Enchanted Forest","Hogsmead Villiage"]


restaurants =["Hogwards Dining Commons", "The Leaky Couldron","Honeydukes Sweet Shop","Florean Fortescue's Ice Cream Parlor"]


transportation_options =["Hogwarts Express","Three Headed Dog","Flying Car","Floo Powder"]


entertainment_options =["Quidditch Match","Hagrid's Hut","Zonko's Joke Shop","Gringotts Wizarding Bank"]




# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

import random


# new_restaurant = random.choice(restaurants)
# new_transportation_option = random.choice(transportation_options)
# new_entertainment_option = random.choice(entertainment_options)

# new_destination = random.choice(destinations)

# print(new_destination)

# print(new_entertainment_option)
# print(new_transportation_option)
# print(new_restaurant)

#are you satisfied with selection y/n ---> no will restart the random selection; yes will print 'selection confirmed'??

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation,
# and/or form of entertainment if I don’t like one or more of those things.

def confirm_choice(list):
    user_selection = "n"
    while user_selection != "y":
       new_selection = random.choice(list)  
       print(new_selection)
       user_selection = input("Are you satisfied with selection y/n?")
    return new_selection

confirm_choice(destinations)
confirm_choice(restaurants)
confirm_choice(transportation_options)
confirm_choice(entertainment_options)

# funtion that allows users to loop over list selections to reselect. 
# if user chooses confirm then print "Selection Confirmed"

# while loop?

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# once all selections are confirmed, user can select "Complete Trip Plan"



# (10  points): As a user, I want to display my completed trip in the console

# print all selections of completed trip as "Confirmed Completed Trip Plan"



# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. 
# Remember, each function should do just one thing! 

# review/edit all code to make sure single responsibility is active in each line