# These are the following steps to run the our Workout App

## Introduction:

1. This program assists users in planning their workouts and maintaining a 
healthy lifestyle by providing personalized workout routines, meal plans, 
nearest gym locations, and tracking workout progressions.

2. To run the program you need to first open the terminal and run Python3 
Workout_code.py (Mac Users) or Python Workout_code.py (Window Users) on the 
command line.

# Instructions

1. The init method initializes the WorkoutPlanner object, it uses a with statement
to read the JSON file path containing the workout routines for the body types and a
dictionary conttaining the workout gets loaded from the file. 

    - The JSON file contains all the exercises for each body types.

2. The get_body function prompts the user's to enter their body type on the terminal, 
you must enter one of the three main body types (Ectomorph, Mesomorph, Endomorph)
in the terminal or else it will return "invlaid body type" and it will make you 
enter one of the three body type again until it's a vaild body type which is (Ectomorph, 
Mesomorph, Endomorph).  

3. The workout_routine function gets the workout routine/exercises that correlates to 
the users selected body types. 

4. The meal_planner function creates a personalized meal plan correlated to the selected
body type, either (Ectomorph, Mesomorph, Endomorph), which includes the meal plan for
breakfast, lunch, and dinner. It will raise ValueError on the terminal if the body type
is invaild and won't create a personalized meal plan correlated to the selected
body type.

5. The get_cut_bulk_goal function prompts the user's to enter their goal of either 
cutting or bulking on the terminal. You must enter either cut or bulk based on 
what the user's goal is. If the input provided on the terminal is too short 
(less than 2 characters), it will use the default goal, which is a "cut" plan. 


6. The get_nutritional_targets function outputs all the workout routine/exercises
 you could chose from and it will display your daily target nutrients, which is
 the amount of proteins, carbs, and fats in grams that you need to consume. 
 It will also display the meal plan based on your body type and goal for breakfast, 
 lunch, and dinner in the terminal.

7. The nearest_gyms function takes the users location and returns gyms near the users 
location.  Gyms are stored in a dictionary with the name of the gym first then the 
gym's address. When my part of the function pops up, you can enter the city, ex. 
College Park, state, ex. MD, zipcode, ex. 20740, or a gyms street address.  When 
entering an address, it is case sensitive and will return no gyms if inputed wrong. 
If inputting a state, it has to be in two captial letters for the state like MD or VA.
The city has to be in the format of the first letter of the city has to be capitalized.

8. The order_gyms function orders the gyms that has been returned in order of the 
street address.  For example, an address that starts with 1000 will be returned at 
the top and then an address that starts with 4000 will be further down the list. 


9. The Progress_Board function reads in data from a csv file containing the
data of users on this workout app. It retrieves the information of the users active 
progression based on the users specified criteria. You will enter the maximum rank you
want to see in the terminal, the rank ranges from 1 to 30, which any rank you enter in the 
terminal between 1 to 30 will be valid. If the rank provided in the terminal is 
not between 1 to 30, the dataframe will display nothing since our csv file only contains,
users rank from 1 to 30. 

After entering your specified maximum rank, you will then enter the minimum progression score
in the terminal. The progression score showcases the overall effort users put into 
following their dietary meal plans and workouts based on their body type. The 
progression scores ranges from 9 to -9. Progression scores that are 9 indicates that 
the users have been active following their dietary meal plans and workouts, while -9 indicates
that the users have not been active following their dietary meal plans and workouts.

After entering your specified criteria for maximum rank and progression score, a dataframe 
will display in the terminal showcasing the results. 

10. The plot_avg_progression function will display a barplot that calculates the average
progression score by age and also displaying the average progression score for 
each age group in a different window.

This bar plot displays the Average Progression Score by Age. The Average 
Progression Score is calculated by the overall effort put into following the 
dietary meal plans and workouts based on the user's body type. A trend identified 
is that as the user's age increases, the Average Progression Score decreases. 
For users ages 40 and above, the average progression score typically declines to 
below -7.5. This can be due to several factors attributed to aging such as a 
decreased metabolism, hormonal changes, and challenges in finding enough time to 
adhere to the workout/meal plan. For ages 30 and below, the Average Progression 
Score is positive with the peak average score at age 27, above 7.5. This can be 
attributed to having a faster metabolism, health goals, and following fitness 
trends seen on social media. 


# A table indicating primary author of each major function or method

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|          Method/Function             | Primary Author |           Techniques Demonstrated             |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
| def__init__(): (class WorkoutPlanner)|  Jason Guan    |        with statement & json.loads()          |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|     def Progress_Board():            |  Jason Guan    |         Pandas DataFrame Filtering            |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  def get_nutritional_targets():      |     Zayd       |                     N/A                       |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  def get_cut_bulk_goal():            |     Zayd       | Optional Parameters & Conditional Expressions |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  def nearest_gyms():                 |    Isaiah      | Regular Expressions & Sequence Unpacking      |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  def order_gyms():                   |    Isaiah      |          Lambda Expression                    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|  def meal_planner():                 |    Hayat       |  F-strings Containing Expressions             |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
|  def plot_avg_progression():         |    Hayat       |             SeaBorn / BarPlot                 |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




