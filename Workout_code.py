from argparse import ArgumentParser
import pandas as pd
import seaborn as sns
import json
import re

class WorkoutPlanner:

    def __init__(self, workout_file):
        with open(workout_file, "r", encoding = "utf-8") as workouts:
            self.workout = json.load(workouts)         
        
    def get_body(self):
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph) ")
            if body_type in self.workout:
                self.body_type = body_type
                return body_type
            else:
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")

    def workout_routine(self):
        body_type = self.get_body()
        if body_type in self.workout:
            return self.workout[body_type]


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

class TargetNutrition(WorkoutPlanner):

    def __init__(self, workout_file):
        super().__init__(workout_file) 
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
    
def nearest_gyms(location):
   
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


if __name__ == "__main__":
    target_nutrition = TargetNutrition("workout.json")
    nutritional_plan = target_nutrition.get_nutritional_targets()
    print(f"Based on your body type ({nutritional_plan['body_type']}) and goal ({nutritional_plan['cut_bulk']}):")
    print(f"Workout Routine: {nutritional_plan['workout_routine']}")
    print(f"Daily Target Nutrients:")
    meal_plan = target_nutrition.meal_planner()
    print(meal_plan)
    for target in nutritional_plan["nutritional_targets"]:
        print(f"\t{target}")
        






