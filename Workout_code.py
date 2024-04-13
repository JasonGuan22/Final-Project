from argparse import ArgumentParser
import json
import re

class WorkoutPlanner:
    """ 
    A class for planning the workout routine based on the user body type.
    
    Attributes:
        workout (dict): A dictionary containing the workout routines 
        categorized by the body type of the user.
        
    Methods:
        __init__(): Initializes the WorkoutPlanner object with an empty workout
        dictionary.
        
        get_body():
            Prompts the user to input their body type either Ectomorph, 
            Mesomorph or Endomorph.
            
        workout_routine (input_file: str):
            Reads the workout routine from an input file and categorizes the
            workout routine by the body type and prints the categorized 
            workout routine correlated to the body type. 
    """

    def __init__(self):
        self.workout = {}
    
    def get_body(self):
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph)")
            if body_type in self.workout:
                self.body_type = body_type
                return body_type
            else:
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")

    def workout_routine(self, input_file):
        """ Reads the workout routine from an input file and categorizes the
        workout routine by the body type and prints the categorized workout 
        routine correlated to the body type.
        
        Args:
            Input_file (str): The file path of the input file containing the
            workout routines.
        
        Returns:
            list: A list of exercises correlated with the user's body type. It
            returns None if the body type does not match either Ectomorph, 
            Mesomorph or Endomorph. 
        
        Side effects:
            Reads from a file and modifies the workout dictionary by adding new
            key-value pairs. 
            Prints the updated workout dictionary to the console.
        """
        with open(input_file, "r", encoding= "utf-8") as f:
            for line in f:
               workout = line.strip().split(",")
               self.workout[workout[0]] = workout
               print(self.workout)
        if self.body_type in self.workout:
            return self.workout[self.body_type]

    def meal_planner(self, body_type):
        """
        Creates a personalized meal planner based on body type 
        
        Args: 
            body_type (str): The body type for which to create the meal plan
            (Ectomorph, Mesomorph, or Endomorph)
            
        Returns:
            str: A string of the meal plan for the body type selected 
            
        Raises:
            ValueError: If an invalid body type is provided 
        """
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
        
        if body_type not in meal_plans:
            raise ValueError("Invalid body type. Please select Ectomorph, Mesomorph, or Endomorph.")
        
        select_meal_plan = meal_plans[body_type]
        
        meal_plan = f"Meal Plan for {body_type}: \n"
        meal_plan += f"Breakfast: {select_meal_plan['Breakfast']}\n"
        meal_plan += f"Lunch: {select_meal_plan['Lunch']}\n"
        meal_plan += f"Dinner: {select_meal_plan['Dinner']}\n"
        
        return meal_plan

class TargetNutrition(WorkoutPlanner):
    """
    This is a class that represents target nutritional values based on the body 
    type and the goal the user is trying to attain (cut or bulk). 
    This is a subclass that inherits from the WorkoutPlanner class.

    Attributes:
        targets (dict): A dictionary containing the target nutritional values based
        on whether the user's goal is to cut or bulk in weight.
    
    Methods:
        __init__(): Initializes the TargetNutrition object.
        get_cut_bulk_goal(): Asks the user to input their goal (cut or bulk) and
        returns it.
        get_nutritional_targets(): Determines the nutritional targets based on 
        the body type and goal of the user.
        get_body(): Asks the user to input their body type and returns it.
    """
    
    def __init__(self):
        super().__init__() 
        self.targets = {  
            "cut": ["Protein: 60g", "Carbs: 40g", "Fat: 30g"],
            "bulk": ["Protein: 70g", "Carbs: 60g", "Fat: 40g"],
        }

    def get_cut_bulk_goal(self):
        while True:
            goal = input("Are you looking to cut or bulk (cut/bulk): ")
            if goal.lower() in self.targets:
                return goal.lower()
            else:
                print("Invalid goal. Please enter either cut or bulk")

    def get_nutritional_targets(self):
        
        self.body_type = self.get_body()
        cut_bulk_goal = self.get_cut_bulk_goal()
        workout_routine = super().workout_routine()  

        target_plan = {
            "body_type": self.body_type,
            "workout_routine": workout_routine,
            "cut_bulk": cut_bulk_goal,
            "nutritional_targets": self.targets[cut_bulk_goal]
        }
        return target_plan


target_nutrition = TargetNutrition()
nutritional_plan = target_nutrition.get_nutritional_targets()
print(f"Based on your body type ({nutritional_plan['body_type']}) and goal ({nutritional_plan['cut_bulk']}):")
print(f"Workout Routine: {nutritional_plan['workout_routine']}")
print(f"Daily Target Nutrients:")
for target in nutritional_plan["nutritional_targets"]:
    print(f"\t{target}")
    
def nearest_gyms(location):
    """Finds the nearest gyms based on user's location.

    Args:
        location (str): String that represents the location for the gym search.
        Matches user's provided location with gym addresses that are nearest them.

    Returns:
        list: List of tuples that contains gym address information and if no 
        near gyms are found, an empty list is returned.
    """
    gyms ={
        "Crunch Fitness": "4320 Calvert Rd, College Park, MD 20740",
        "Eppley Recreation Center": "4128 Valley Dr, College Park, MD 20742",
        "LA Fitness": "2970 Belcrest Center Dr, Hyattsville, MD 20782",
        "Planet Fitness": "6881 New Hampshire Ave, Takoma Park, MD 20912",
        "UMD School of Public Health": "4200 Valley Dr, College Park, MD 20742",
        "Ritchie Coliseum": "7675 Baltimore Ave, College Park, MD 20742",
        "Orange Theory": "8321 Baltimore Ave, College Park, MD 20740"
    }
    
    loc_pattern = re.compile(r'\b{}\b.*?(?:,\s+(?P<state>[A-Z]{2})\s+(P<zip>\d{5}))?\b'
                         .format(location.replace(' ', r'\s')), re.IGNORECASE)
    
    nearest_gyms = []
    for gym, address in gyms.items():
        match = re.search(loc_pattern, address)
        if match:
            city = location
            state = match.group('state') if match.group('state') else "" 
            zip_code = match.group('zip') if match.group('zip') else ""
            nearest_gyms.append((gym, address, city, state, zip_code)) 
            
    return nearest_gyms


