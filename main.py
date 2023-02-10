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
    print(f"Destination: {list[0]}\nRestaurant: {list[1]}\nTransportation: {list[2]}\nActivity: {list[3]}\n")

#return int of user feedback 
def user_feedback(user_list):
    answer = input("Are you satisfied with your trip 'yes' or 'no'?\n")
    #loop until readable answer given
    while True:
        if answer == 'yes':
            print("Your final list:\n")
            print(readout_of_options(user_list))
            return 6  #program is continuing to run 
        elif answer == 'no':
            user_feedback = int(input("Choose what to change:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Activity\n5 for everything\n"))
            return user_feedback
            break
        else:
            print("incorrect input, please try again")
            continue


def get_new_item(user_feedback, user_list):
    if user_feedback == 5:  
        #rerun initial setup
        print(trip_choices(all_lists))
    elif user_feedback >= 1 or user_feedback < 5:
        index = user_feedback - 1
        list_to_change = all_lists[index]
        unwanted_item = user_list[index]
        new_item = random.choice(list_to_change)
        while new_item == unwanted_item:
            new_item = random.choice(list_to_change)
        return new_item
    else:
        print("Thank you")

    
def revise_list(user_list, user_change, new_item):
    index = user_change -1
    user_list[index] = new_item

def run_program(all_lists):
    #initial run
    user_list = trip_choices(all_lists)
    readout_of_options(user_list)
    #feedback
    feedback = user_feedback(user_list)
    new_item = get_new_item(feedback, user_list)
    revise_list(user_list, feedback, new_item)









run_program(all_lists)


