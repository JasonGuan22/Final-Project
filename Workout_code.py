import json
from argparse import ArgumentParser


class WorkoutPlanner:

    def __init__(self):
        self.workout = {
            "Ectomorph": ["Bench Press", "Pull Ups", "Deadlifts", "Squats"],
            "Mesomorph": ["Pushups", "Burpee", "Mountain Climbers", "Lunges"],
            "Endomorph": ["Treadmill Sprint", "Barbell Back Squat",
                          "Battling Ropes", "Indoor Cycling"],
        }
        
    def get_body(self):
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph) ")
            if body_type in self.workout:
                self.body_type = body_type
                return body_type
            else:
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")

    def workout_routine(self):
        
        if self.body_type in self.workout:
            return self.workout[self.body_type]

    def meal_planner(self,body_type):
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
print(f"Based on your body type ({nutritional_plan['body_type']}) and goal({nutritional_plan['cut_bulk']}):")
print(f"Workout Routine: {nutritional_plan['workout_routine']}")
print(f"Daily Target Nutrients:")
for target in nutritional_plan["nutritional_targets"]:
    print(f"\t{target}")
