#import statements here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predict_mood(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[temp_min, temp_max, temp_mean]],
                      columns=['Temp_Min', 'Temp_Max', 'Temp_Mean'])
    return model.predict(df)[0]

data = pd.read_csv('AR1-3_input105721.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['temp_min', 'temp_max', 'temp_mean']]
Y = data['avg_mood']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)


print("Multiple Linear Regression Model Complete!")

# Checking how well it worked
mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")

# I had no idea what MEAN SQUARED meant so this scale might be helpful to you

mse_remark = interpret_mse(mse)
print("How good is this model? ", mse_remark)

# Making a prediction using the model




# Let the user enter their own 3 parameters
print("")
print("USER CHOOSES 3 TEMPERATURE LEVELS MODE")
hours = int(input("Enter temperature hours. Can be any integer from 0-24"))
temp = float(input("Enter average temperature. Can be anything from 1-800 "))
peak = float(input("Enter peak temperature. Can be anything from 1-800"))

predicted_mood = predict_mood(hours, temp, peak)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)


# WHAT-IF Question 1
# What is will your mood be with low values of all three parameters?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("Let's test what the mood will be if the sunlight is very low")

# Low values for all 3 parameters
sunlight_hours = 2
average_sunlight = 100
peak = 200

mood_if_littleSun = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The low sun score mood is", mood_if_littleSun)



# WHAT-IF Question 2
# What is will your mood be with high values of all three parameters?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 2")
print("Let's test what the mood will be if the sunlight is very high")

# High values for all 3 parameters
sunlight_hours = 15
average_sunlight = 600
peak = 800

mood_if_LoadsaSun = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The higher sun score mood is", mood_if_LoadsaSun)



# WHAT IF QUESTION 3
# What variable is more important
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 3")
print("Let's test if average sunlight is more important than peak sunlight")
print("We will keep the hours (A) the same and double the others (B) and (C) one at a time")
print("")

print("Let's get a baseline from fairly average values...")

# Baseline 
sunlight_hours = 6
average_sunlight = 300
peak = 300

baseline_mood = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The baseline Score mood is", baseline_mood)
print("")


# Double the average sunlight
print("Let's double the average sunlight...")
sunlight_hours = 6
average_sunlight = 600
peak = 300

doubleAverageOutcome = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("The double sunlight mood is", doubleAverageOutcome)
print("")

# Double the peak sunlight
print("Let's double the peak sunlight...")
sunlight_hours = 6
average_sunlight = 300
peak = 600

doublePeakOutcome = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("The double peak mood is", doublePeakOutcome)
print("")


# PRINTED FEEDBACK

print("OUTCOME:")
if doubleAverageOutcome > doublePeakOutcome:
    print("It's the average that improves mood the most")
else:
    print("It's the peak that improves mood the most")


#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Questions 1 & 2
import matplotlib.pyplot as plt

# Data: names of the variables and their values
variable_names = ['Mood if Little Sun', 'Mood if Loadsa Sun',]
values = [mood_if_littleSun, mood_if_LoadsaSun]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Moodiness')
plt.title('Bar Chart of WHAT-IF Q1, Q2 Outcomes')

# Show the plot
plt.show()

#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Question 3
import matplotlib.pyplot as plt

# Data: names of the variables and their values
variable_names = ['Mood if Double Average', 'Mood if Double Peak',]
values = [doubleAverageOutcome, doublePeakOutcome]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Moodiness')
plt.title('Bar Chart of WHAT-IF Q3 Outcome')

# Show the plot
plt.show()