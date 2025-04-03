# TEXT TO SPEECH

This project demonstrates how to convert text to speech using Python. We can use libraries like `pyttsx3` and `gTTS` for this purpose.

## Using pyttsx3

`pyttsx3` is an offline Text-to-Speech conversion library in Python.

### Installation

```bash
pip install pyttsx3
```

### Example Code

```python
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

`gTTS` (Google Text-to-Speech) is an easy-to-use library for converting text to speech using Google Translate's TTS API.

### Installation

```bash
pip install gtts
```

### Example Code

```python
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

Both libraries provide simple and effective ways to implement text-to-speech functionality in Python. Choose the one that best fits your requirements!
