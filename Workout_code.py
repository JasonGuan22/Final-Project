from argparse import ArgumentParser
import pandas as pd
import seaborn as sns
import json
import re
import matplotlib.pyplot as plt

class WorkoutPlanner:
    """ This class helps users plan their workouts based on their bodytype.
    
    Attributes:
        workout_file (str): The path to the JSON file containing workout data. 
        In the JSON data is formatted as a dictionary with body types as keys
        and workout routines as values.
            
        workout (dict): A dictionary loaded from the "workout_file", containing
        the workout routines for the different body types (Ectomorph, Mesomorph,
        Endomorph). 
            
        body_type (str): The user's selected body type, where it get set by the 
        "get_body" method.
    """
    def __init__(self, workout_file):
        """ Initializes the WorkoutPlanner object.
        
        Args:
            workout_file (str): The path to a JSON file containing the workout
            data that's formatted as a dictionary with body types as keys and 
            workout routines as values. 
            
        Side effects: 
            Modifies the internal state of the object by loading the workout
            data from the JSON file and storing it in the "workout" attribute.
            
        Primary Author: Jason Guan
        
        Technique(s) Shown: with statements & json.loads()
        """
        with open(workout_file, "r", encoding = "utf-8") as workouts:
            self.workout = json.load(workouts)  
            
        self.targets = {  
            "cut": ["Protein: 50g", "Carbs: 40g", "Fat: 15g"],
            "bulk": ["Protein: 70g", "Carbs: 60g", "Fat: 40g"],
        }
                     
    def get_body(self):
        """ Prompts the user to enter their body type and validates the input.
        
        Returns:
            str: The selected body type of the user (Ectomorph, Mesomorph, 
            Endomorph).
            
        Side effects:
            Sets the "body_type" attribute of the object.
        """
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph) ")
            if body_type in self.workout:
                
                return body_type
            else:
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")

    def workout_routine(self):
        """ Retrieves the workout routine based on the user's selected body type.
        
        Returns:
            list or None: A list of exercises in the workout routine for the 
            user's selected body type if the body type exists in the "workout"
            dictionary. None if the user's "body_type" atrribute has not 
            been set.
        """
        if self.body_type in self.workout:
            return self.workout[self.body_type]
    
    def meal_planner(self):

        meal_plans = {
            "Ectomorph": {
                "Breakfast": "Oatmeal topped with strawberry and walnuts",
                "Lunch": "Mediterranean quinoa salad with chopped veggies",
                "Dinner": "Grilled chicken and a tomato and cucumber salad"
            },
            "Mesomorph": {
                "Breakfast": "Greek yogurt parfait with pumpkin, cinnamon, peacans, and raisins toppings",
                "Lunch": "Large salad with chopped veggies, sweet potato chunks, and avocados",
                "Dinner": "Baked salmon, roasted broccoli, and veggies"
            },
            "Endomorph": {
                "Breakfast": "Vegetable omlette",
                "Lunch": "Sitr-fry made with chicken and peppers over brown rice",
                "Dinner": "Grilled tofu with stir-fried vegetables"
            }
        }
        
        if self.body_type not in meal_plans:
            raise ValueError("Invalid body type. Please select Ectomorph, Mesomorph, or Endomorph.")
        
        select_meal_plan = meal_plans[self.body_type]
        
        meal_plan = f"Meal Plan for {self.body_type}: \n"
        meal_plan += f"Breakfast: {select_meal_plan['Breakfast']}\n"
        meal_plan += f"Lunch: {select_meal_plan['Lunch']}\n"
        meal_plan += f"Dinner: {select_meal_plan['Dinner']}\n"
        
        return meal_plan

    def get_cut_bulk_goal(self, default_goal = "cut", min_input_length = 2):
        while True:
            goal = input("Are you looking to cut or bulk? (default goal is to cut): ")
            if len(goal) < min_input_length:
                print(f"\nInvalid input. Minimum length is {min_input_length} characters. \
                      \nThe default goal will be used.")
            return (goal.lower() if len(goal) >= min_input_length and 
                    goal.lower() in self.targets else default_goal)

    def get_nutritional_targets(self):
        
        self.body_type = self.get_body()
        cut_bulk_goal = self.get_cut_bulk_goal()
        workout_routine = self.workout_routine()  

        target_plan = {
            "body_type": self.body_type,
            "workout_routine": workout_routine,
            "cut_bulk": cut_bulk_goal,
            "nutritional_targets": self.targets[cut_bulk_goal]
        }
        return target_plan
    
def nearest_gyms(location):
    """Finds the nearest gyms based on user's location.
     
    Args: 
        location (str): String that represents the location for the gym search.
        Matches user's provided location with gym addresses that are nearest them.
        
    Returns: 
        list: List of tuples that contains gym address information and if no near gyms 
        are found, an empty list is returned. 
        
    Primary Author: Isaiah Sampilo
    
    Technique(s) Shown: Regular Expression & Sequence Unpacking
    """ 
    loc_pattern = (re.compile(rf'\b{re.escape(location)}\b.*?(?:,\s+(?P<state>[A-Z]{2})\s+(?P<zip>\d{5}))?\b', re.IGNORECASE))
    gyms ={
        "Crunch Fitness": "4320 Calvert Rd, College Park, MD 20740",
        "Eppley Recreation Center": "4128 Valley Dr, College Park, MD 20742",
        "LA Fitness": "2970 Belcrest Center Dr, Hyattsville, MD 20782",
        "Planet Fitness": "6881 New Hampshire Ave, Takoma Park, MD 20912",
        "UMD School of Public Health": "4200 Valley Dr, College Park, MD 20742",
        "Ritchie Coliseum": "7675 Baltimore Ave, College Park, MD 20742",
        "Orange Theory": "8321 Baltimore Ave, College Park, MD 20740",
        "Planet Fitness": "6100 Greenbelt Rd, Greenbelt, MD 20770",
        "OneLife Fitness": "1407 Research Blvd, Rockville, MD 20850",
        "Gold's Gym": "26 Maryland Ave, Rockville, MD 20850",
        "Planet Fitness": "1100 Wayne Ave, Silver Spring, MD 20910",
        "LA Fitness": "8616 Cameron St, Silver Spring, MD 20910",   
        "Gold's Gym": "4595 Woodberry St, Riverdale Park, MD 20737",
        "Greenbelt Aquatic and Fitness Center": "101 Centerway, Greenbelt, MD 20770",
        "Prince George's Sports & Learning Complex": "8001 Sheriff Rd, Landover, MD 20785",
        "LA Fitness": "9450 Ruby Lockhart Blvd, Lanham, MD 20706",
        "CrossFit Hyattsville": "4616 Ingraham St, Hyattsville, MD 20781"
    }
        
    nearest_gyms = []
    for gym, address in gyms.items():
        match = re.search(loc_pattern, address)
        if match:
            city = location
            state = match.group('state') if match.group('state') else "" 
            zip_code = match.group('zip') if match.group('zip') else ""
            nearest_gyms.append((gym, address, city, state, zip_code)) 
            
    return nearest_gyms

def order_gyms(gyms_list):
    """Orders the gyms returned by the user ordered by their address. The lower 
    numbered addresses at the top then the higher number address going down. 

    Args:
        gyms_list (list): List of tuples containing the gyms information.

    Returns:
        list: List of tuples containing gym information that is sorted.
        
    Primary Author: Isaiah Sampilo
        
    Technique(s) Shown: Lambda expression
    """
    ordered_gyms = sorted(gyms_list, key=lambda gym_info: gym_info[1])

    return ordered_gyms

def Progress_Board(max_rank, min_progression_score):
    """ Retrieves the infromation about the active progression from a workout 
    scoreboard based on the specified criteria.
    
    Args:
        max_rank (int): The maximum rank allowed for the progressions to be
        considered for the specified criteria. User's with a rank lower than or
        equal to this value will be included in the results.
        
        min_progression_score (int): The minimum progression score required 
        for the progressions to be considered for the specified criteria. User's
        with a progression score higher than this value will be included in the 
        results.
        
    Returns:
        pandas.DataFrame: A DataFrame containing information about the active 
        progressions that meets the specified criteria (rank & progression 
        score).
        
    Primary Author: Jason Guan
        
    Technique(s): Pandas DataFrame Filtering
    """
    score = pd.read_csv("Workout_ScoreBoard.csv", encoding="utf-8")
    active_progression = (score[(score["Rank"] <= max_rank) & 
                    (score["Progression Score"] > min_progression_score)])
    return active_progression


if __name__ == "__main__":
    target_nutrition = WorkoutPlanner("workout.json")
    nutritional_plan = target_nutrition.get_nutritional_targets()
    
    print(f"\nBased on your body type ({nutritional_plan['body_type']}) and goal ({nutritional_plan['cut_bulk']}):")
    
    print(f"\nWorkout Routine: {nutritional_plan['workout_routine']}")
    print(f"\nDaily Target Nutrients:")
    for target in nutritional_plan["nutritional_targets"]:
        print(f"\t{target}")
        
    meal_plan = target_nutrition.meal_planner()
    print("\n" + meal_plan)
    
    location = input("\nEnter your location: ")
    gyms_list = nearest_gyms(location)
    ordered_gyms = order_gyms(gyms_list)
    if ordered_gyms:
        print("\nNearest gyms (ordered by address):")
        for gym, address, city, state, zip_code in ordered_gyms:
            print(f"{gym}: {address} ({city}, {state}, {zip_code})")
    else:
        print("\nNo gyms found near you.")
        
    print("\nWorkout app user progression board: ")
    
    max_rank_input = int(input("\nEnter the maximum rank: "))
    min_progression_score_input = int(input("\nEnter the minimum progression score: "))

    filtered_data = Progress_Board(max_rank_input, min_progression_score_input)
    print(filtered_data) 
    
def plot_avg_progression():
    score_df = pd.read.csv("Workout_ScoreBoard.csv", encoding="utf-8")
    
    avg_scores = score_df.groupby('Age')['Progression Score'].mean().reset_index()
    sns.barplot(x='Age', y='Progression Score', data= avg_scores)
    plt.title('Average Progression Score by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Progression Score')
    plt.show()





























