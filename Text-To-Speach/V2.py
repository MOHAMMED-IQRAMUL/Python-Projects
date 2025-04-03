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