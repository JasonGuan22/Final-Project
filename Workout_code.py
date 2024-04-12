from argparse import ArgumentParser
import re
import json

class WorkoutPlanner:
    
    def __init__(self):
        self.workout = {
            "Ectomorph": ["Bench Press", "Pull Ups", "Deadlifts", "Squats", 
                          "Standing Military Press", "Compound Lifts"],
            "Mesomorph": ["Pushups", "Burpee", "Mountain Climbers", "Lunges"],
            "Endomorph": ["Treadmill Sprint", "Barbell Back Squat", 
                          "Battling Ropes", "Indoor Cycling"],
        }
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
        
    def get_body(self):
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph)")
            if body_type in self.workout:
                return body_type
            else: 
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")
            
    def workout_routine(self):
        body_type = self.get_body()
        if body_type in self.workout:
            routine = self.workout[body_type]
            return routine 
        
         
    

    
    
    
    

    def get_body(self):
        pattern = r"^\s*(Ectomorph|Mesomorph|Endomorph)\s*$"
        while True:
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph)")
            match = re.match(pattern, body_type, re.IGNORECASE)  
            if match:
                return match.group(1)
            else: 
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")
              
    def workout_routine(self, body_type = "Mesomorph"):
        body_type = self.get_body()
        if body_type in self.workout:
            routine = self.workout[body_type]
            print(f"This is your recommended workout routine {routine}.")
            
            
            


        
        
        
        
    
    
    
 
        
        
    
    
    
    