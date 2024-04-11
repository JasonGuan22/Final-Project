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
            body_type = input("Please enter your body type (Ectomorph, Mesomorph, Endomorph)")
            if body_type in self.workout:
                return body_type
            else: 
                print("Invalid body type. Please enter either Ectomorph, Mesomorph, Endomorph")
            
    def workout_routine(self):
        body_type = self.get_body()
        if body_type in self.workout:
            return self.workout[body_type]
        
    
    
        
        
        
        
    
    
    
 
        
        
    
    
    
    