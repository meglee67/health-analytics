import pandas as pd 
import numpy as np 

# Creating variables
heart_rate = 75
patient_name = "Astarion"
heart_rate_list = [60, 70, 80, 90, 120]
patient_data = {
    "name": "Astarion",
    "age": 28,
    "heart_rates": [78, 82, 89],
    "details": {
        "weight": 100,
        "height": 172
    }
}

#Create a function that takes two inputs and calculates with an if/else statement
def analyze_heart_rate(age, resting_heart_rate):
    if age <30:
        if resting_heart_rate < 60:
            return "Below Average"
        elif 60 <= resting_heart_rate <= 100:
            return "Normal"
        else:
            return "Above average, seek medical attention"

# Print Statements
print("Heart Rate:", heart_rate)
print("Patient Name:", patient_name)
print("Heart Rate List:", heart_rate_list)
print("Patient Data:", patient_data)

age = 27
resting_heart_rate = 78
heart_rate_category = analyze_heart_rate(age, resting_heart_rate)
print("Heart Rate Category:", heart_rate_category)