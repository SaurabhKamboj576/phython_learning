import datetime
import pyttsx3

# Get the current date and time
now = datetime.datetime.now()
date = now.strftime("%A, %B %d, %Y")

# Get the current hour
hour = now.hour

# Determine the greeting based on the time
if hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Night"

# Get user input
name = input("Enter your Name: ")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say(f"{greeting}, {name}. Today is {date}. your a motherfucker")
engine.runAndWait()
