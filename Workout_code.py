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
    def meal_planner(self,body_type):
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
            return self.workout[body_type]
        
    
    
        
        
        
        
    
    
    
 
        
        
    
    
    
    