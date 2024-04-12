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
            
            
            


        
        
        
        
    
    
    
 
        
        
    
    
    
    