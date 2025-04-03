# TEXT TO SPEECH

We can use libraries like pyttsx3 and gTTS for converting the text to speech.

## Using pyttsx3

Installing pyttsx3 -> pip install pyttsx3

``` py
import pyttsx3

# Initialize the converter
engine = pyttsx3.init()

# Text to be converted
text = "Hello, welcome to Python text to speech conversion!"

# Convert text to speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()
```

## Using gTTS

Install gTTS -> pip install gtts

``` py
from gtts import gTTS
import os

# Text to be converted
text = "Hello, welcome to Python text to speech conversion!"

# Language in which you want to convert
language = 'en'

# Creating the gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
tts.save("output.mp3")

# Playing the converted file (optional)
os.system("start output.mp3")  # Use 'afplay' on macOS or 'xdg-open' on Linux
```
