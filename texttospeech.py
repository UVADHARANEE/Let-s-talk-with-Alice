import gtts
from playsound import playsound


tts = gtts.gTTS("Hola Mundo escape with plane", lang="es")
tts.save("alert.mp3")
playsound("alert.mp3")