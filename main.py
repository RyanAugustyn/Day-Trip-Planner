import random

# lists for day planner 
destinations = ["Madison", "San Diego", "Miami", "Seattle"]
restaurants = ["Sugar River Pizza", "Hodad's", "McDonald's", "Cafe' Nervosa"]
modes_of_transportation = ["Speedboat", "Plane", "Train", "Automobile"]
forms_of_entertainment =["Hiking", "Music Concert", "Surfing"]

all_lists = [destinations, restaurants, modes_of_transportation, forms_of_entertainment]

#functions 

#pick random item from list 
def pick_random_item(list_of_items):
    return random.choice(list_of_items)

#pick one random item from multiple lists
def trip_choices(list_of_lists):
    temp_list = []
    for list in list_of_lists:
        temp_list.append(pick_random_item(list))
    return temp_list

#print out randomly chosen items 
def readout_of_options(list):
    print(f"\nDestination: {list[0]}\nRestaurant: {list[1]}\nTransportation: {list[2]}\nActivity: {list[3]}\n")

#return int of user feedback 
def user_feedback(user_list):
    answer = input("Are you satisfied with your trip 'yes' or 'no'?\n")
    #loop until readable answer given
    while answer != 'yes' and answer != 'no':
        print("\nincorrect input, please try again\n")
        answer = input("Are you satisfied with your trip 'yes' or 'no'?\n\n")
    if answer == 'yes':
        print("\nYour final list:")
        readout_of_options(user_list)
        return 0 #check in run_program if continues or not
    elif answer == 'no':
        user_feedback = int(input("\nChoose what to change:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Activity\n5 for Everything\n6 for Surprise Me! (randomly picks 1-5)\n"))
        while user_feedback < 1 or user_feedback > 6:
            print("\nInvalid input, please choose from the following options\n")
            user_feedback = int(input("Choose what to change:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Activity\n5 for Everything\n6 for Surprise Me! (randomly picks 1-5)\n"))
        return user_feedback
        
#return new item(s) based on user feeback 
def get_new_item(user_feedback, user_list):
    index = user_feedback - 1
    list_to_change = all_lists[index]
    unwanted_item = user_list[index]
    new_item = random.choice(list_to_change)
    #ensure old item is not reselected:
    while new_item == unwanted_item:        
        new_item = random.choice(list_to_change)
    return new_item

#start over with new list
def get_new_list(user_list):
    new_list = trip_choices(all_lists) 
    readout_of_options(new_list)
    return new_list

#add in change from get_new_item function    
def revise_list(user_list, user_change, new_item):
    index = user_change -1
    user_list[index] = new_item
    return user_list

#program to run everything else
def run_program(all_lists):
    #initial run
    user_list = trip_choices(all_lists)
    readout_of_options(user_list)
    #feedback
    feedback = user_feedback(user_list)

    while(feedback != 0):
        #choose option 6, surprise me
        if feedback == 6:
            feedback = random.randrange(1,5)
        if feedback >= 1 and feedback < 5:
            new_item = get_new_item(feedback, user_list)
            user_list = revise_list(user_list, feedback, new_item)
            readout_of_options(user_list)
        elif feedback == 5:
            user_list = get_new_list(user_list)  

        feedback = user_feedback(user_list)


###START PROGRAM###

run_program(all_lists)