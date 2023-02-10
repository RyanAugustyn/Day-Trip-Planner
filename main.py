import random

# lists for day planner 
destinations = ["Madison", "San Diego", "Miami", "Seattle"]
restaurants = ["Sugar River Pizza", "Hodad's", "McDonald's", "Cafe' Nervosa"]
modes_of_transportation = ["Speedboat", "Plane", "Train", "Automobile"]
forms_of_entertainment =["Hiking", "Music Concert", "Surfing"]

all_lists = [destinations, restaurants, modes_of_transportation, forms_of_entertainment]

user_list = []

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

def trip_choices(list_of_lists):
    user_list = []
    for list in list_of_lists:
        user_list.append(pick_random_item(list))
    return user_list

print(trip_choices(all_lists))

    


