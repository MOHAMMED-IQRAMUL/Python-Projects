import pyttsx3

# Initialize the converter
engine = pyttsx3.init()

# Text to be converted
text = "Hello, welcome to Python text to speech conversion!"

# Convert text to speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()