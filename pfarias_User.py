"""
Paula Farias
Class: CS 521 - Semester
Date: 03/05/2021
Homework Problem # Final Project
Description of Problem (just a 1-2 line summary!):
This is the class file for a program that will calculate BMI, \
BMR and calorie intake necessary \
for a 2lb weight gain or loss per weight depending on the BMI.
"""

# User-defined class
class User(object):
    """Holds information about user and performs calculations"""
    def __init__(self, gender, age, height, current_wgt, goal_wgt, activity):
        """Constructor"""
        self.gender = gender
        self.age = age
        self.height = height
        self.current_wgt = current_wgt
        self.__goal_wgt = goal_wgt
        self.activity = activity

    def __repr__(self):
        """Return user attributes"""
        user_attributes = "Attributes of user: " + self.gender + ", " + str(self.age) + ", " \
                          + str(self.height) + ", " + str(self.current_wgt) + ", " + str(self.__goal_wgt) \
                          + ", " + self.activity
        return user_attributes

    def bmr(self):
        """Returns Basal Metabolic Rate (BMR) based on gender and activity level"""
        if "m" == self.gender:
            bmr = 66 + (6.3 * self.current_wgt) + (12.9 * self.height) - (6.8 * self.age)
            if "sedentary" == self.activity:
                bmr *= 1.2
            elif "light exercise" == self.activity:
                bmr *= 1.375
            elif "moderate exercise" == self.activity:
                bmr *= 1.55
            else:
                bmr *= 1.725
        else:
            bmr = 655 + (4.3 * self.current_wgt) + (4.7 * self.height) - (4.7 * self.age)
            if "sedentary" == self.activity:
                bmr *= 1.2
            elif "light exercise" == self.activity:
                bmr *= 1.375
            elif "moderate exercise" == self.activity:
                bmr *= 1.55
            else:
                bmr *= 1.725
        return int(bmr)

    def bmi(self):
        """Returns Body Mass Index(BMI) based on weight and height"""
        bmi = (self.current_wgt / self.height ** 2) * 703
        return '{:.2f}'.format(bmi)

    def __bmi_range(self):
        """Returns a suggestion for user based on BMI range"""
        bmi = (self.current_wgt / self.height ** 2) * 703
        if bmi < 18.5:
            bmi_suggestion = "Underweight: 2lb p/week weight gain recommended"
        elif 18.5 <= bmi <= 24.9:
            bmi_suggestion = "Normal: weight maintenance recommended"
        elif 25.0 <= bmi <= 29.9:
            bmi_suggestion = "Overweight: 2lb p/week weight loss recommended"
        else:
            bmi_suggestion = "Obese: 2lb p/week weight loss recommended"
        return bmi_suggestion


# Unit tests for User
if __name__ == '__main__':
    sample_user = User("f", 33, 66, 200, 148, "sedentary")
    # Testing attributes
    assert sample_user.gender == "f"
    assert sample_user.age == 33
    assert sample_user.height == 66
    assert sample_user.current_wgt == 200
    assert sample_user._User__goal_wgt == 148
    assert sample_user.activity == "sedentary"
    # Testing methods
    assert sample_user.__repr__() == "Attributes of user: f, 33, " \
                                     "66, 200, 148, sedentary"
    assert sample_user.bmr() == 2004
    assert sample_user.bmi() == "32.28"
    assert sample_user._User__bmi_range() == "Obese: 2lb p/week weight loss recommended"
