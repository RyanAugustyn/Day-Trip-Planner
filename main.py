import random

# lists for day planner 
destinations = ["Madison", "San Diego", "Miami", "Seattle"]
restaurants = ["Sugar River Pizza", "Hodad's", "McDonald's", "Cafe' Nervosa"]
modes_of_transportation = ["Speedboat", "Plane", "Train", "Automobile"]
forms_of_entertainment =["Hiking", "Music Concert", "Surfing"]

all_lists = [destinations, restaurants, modes_of_transportation, forms_of_entertainment]

#end goal is program runs, shows a destination, restaurant, mode of transportation and form of entertainment to be randomly selected
#ask user if they like result, if yes, print out the Completed Trip in console 
#if not, allow user to select which of the four options (or all) they would like to re-randomize

#store 4 categories in their own separate lists 

'''Functions from video

def run_day_trip_generator():

def print_full_trip(list_of_options):
    
def generate_random_item(list_of_items):
    
def determine_satisfaction(current_trip, trip_options):

def re_select_option(current_trip, options):
    
'''

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

def user_feedback(user_list):
    answer = input("Are you satisfied with your trip 'yes' or 'no'?\n")
    #loop until readable answer given
    while True:
        if 'yes':
            print("Your final list:\n", readout_of_options(user_list))
            break
        elif 'no':
            to_change = int(input("Choose what to change:\n1 for Destination\n2 for Restaurant\n3 for Transportation\n4 for Activity\n5 for everything"))
            return to_change
            break
        else:
            print("incorrect input, please try again")
            continue


def get_new_item(user_feedback):
    if user_feedback == 5:
        #rerun initial setup
        print(trip_choices(all_lists))
    else:
        index = user_feedback - 1
        list_to_change = all_lists[index]
        unwanted_item = user_list[index]
        new_item = random.choice(list_to_change)
        while new_item == unwanted_item:
            new_item = random.choice(list_to_change)
        
        return new_item
    
def revise_list(user_list, user_change, new_item):
    index = user_change -1
    user_list[index] = new_item

def run_program(all_lists):
    #initial run
    user_list = trip_choices(all_lists)
    readout_of_options(user_list)
    #feedback
    feedback = user_feedback(user_list)
    new_item = get_new_item(feedback)
    revise_list(user_list, feedback, new_item)



run_program(all_lists)


