"""
Paula Farias
Class: CS 521 - Semester
Date: 03/05/2021
Homework Problem # Final Project
Description of Problem (just a 1-2 line summary!):
This program will calculate BMI, BMR and the caloric intake necessary \
for a 2lb weight gain or loss per weight depending on the BMI.
"""

# Import User class
from pfarias_User import User

# Import Random module
import random


# Functions
def gain_lose(bmr, suggestion):
    """Returns calorie intake based on recommendation"""
    lb_calories = 3500
    if suggestion == "Weight Gain":
        gain_lose_formula = bmr + ((lb_calories * 2) / 7)
    elif suggestion == "Weight Maintenance":
        gain_lose_formula = bmr
    else:
        gain_lose_formula = bmr - ((lb_calories * 2) / 7)
    return int(gain_lose_formula)


def recommendations(bmi):
    """Returns 3 random recommendations based on whether user needs
    to gain, lose or maintain weight """
    bmi = float(bmi)
    rec_list = ["Recommendations:"]
    weight_loss_rec = ["Eat 4 servings of vegetables daily.",
                       "Replace refined grains with whole grains.",
                       "Cut back on sugar as much as possible.",
                       "Choose low-fat dairy products and lean meat.",
                       "Use modest amounts of healthy fats.",
                       "Get active and stay active."]
    weight_maintenance_rec = ["Enjoy food but not too much.",
                              "Workout here and there.",
                              "Maintain a balanced diet.",
                              "Cook meals at home.",
                              "Keep doing what you're doing.",
                              "Don't overeat."]
    weight_gain_rec = ["Eat more frequently.",
                       "Choose nutrient-rich foods.",
                       "Make every bite count.",
                       "Have an occasional treat.",
                       "Use bigger plates.",
                       "Try weight gainer shakes."]
    counter = 0
    while counter <= 2:
        if bmi < 18.5:
            # Picks random recommendation and makes sure it only shows up once
            add_message = random.choice(weight_gain_rec)
            if rec_list.count(add_message) < 1:
                rec_list.append(add_message)
                counter += 1
            else:
                continue
        elif 18.5 <= bmi <= 24.9:
            # Picks random recommendation and makes sure it only shows up once
            add_message = random.choice(weight_maintenance_rec)
            if rec_list.count(add_message) < 1:
                rec_list.append(add_message)
                counter += 1
            else:
                continue
        else:
            # Picks random recommendation and makes sure it only shows up once
            add_message = random.choice(weight_loss_rec)
            if rec_list.count(add_message) < 1:
                rec_list.append(add_message)
                counter += 1
            else:
                continue
    return rec_list


# Execute program
continue_value = False

# Loop through questions until responses given in correct format
while continue_value is False:
    gender_list = ["m", "f"]
    activity_list = ["sedentary", "light exercise",
                     "moderate exercise", "very active"]
    user_gender = (input("Enter M for male and F for "
                         "female (not-case sensitive): ")).lower()
    if user_gender in gender_list:
        try:
            user_age = int(input("Enter age in years (whole number): "))
            user_height = float(input("Enter height in inches: "))
            user_current_wgt = float(input("Enter current weight in pounds: "))
            user_goal_wgt = float(input("Enter goal weight in pounds: "))
            user_activity = (input("Enter the category that most closely "
                                   "defines your level of "
                                   "activity per week (not-case sensitive):\n"
                                   "----Sedentary: little/no exercise\n"
                                   "----Light Exercise: 1-2 days/wk\n"
                                   "----Moderate Exercise: 3-5 days/wk\n"
                                   "----Very Active: 6-7 days/wk\n")).lower()
            if user_activity in activity_list:
                continue_value = True
            else:
                print("Please read directions and re-enter data in the correct format.")
        except ValueError:
            print("Please read directions and re-enter data in the correct format.")
    else:
        print("Please read directions and re-enter data in the correct format.")

# Once responses are given in correct format, continue with program
if continue_value:
    user_profile = User(user_gender, user_age, user_height, user_current_wgt,
                        user_goal_wgt, user_activity)
    # Find calories that user needs to eat daily to lose, gain, or maintain weight
    user_calorie_goal = gain_lose(user_profile.bmr(), user_profile._User__bmi_range())
    # Obtain recommendations for weight loss, gain or maintenance
    user_rec_list = recommendations(user_profile.bmi())
    # Turn rec_list into a string in order to write to output file
    user_rec_str = '\n'.join(user_rec_list)
    # Record results in output file
    try:
        output_file = open("Output.txt", "w")
        output_file.write("Body Mass Index (BMI): {} "
                          "({})".format(user_profile.bmi(), user_profile._User__bmi_range()))
        output_file.write("\n")
        output_file.write("Basal Metabolic Rate (BMR): "
                          "{} calories".format(user_profile.bmr()))
        output_file.write("\n")
        output_file.write("Calorie Goal: {}".format(user_calorie_goal))
        output_file.write("\n")
        output_file.write("\n")
        output_file.write(user_rec_str)
        output_file.close()
    except IOError:
        print("File doesn't exist")

