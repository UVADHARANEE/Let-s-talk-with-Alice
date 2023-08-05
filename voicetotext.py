from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
import pywhatkit
import datetime
import wikipedia
import pyjokes

import gtts
from playsound import playsound
import vlc




app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['DEBUG']


@app.route("/")
def homepage():
    return render_template('index.html')



player = None

def play(sound_file):
    global player
    if player is not None:
        player.stop()
    player = vlc.MediaPlayer(sound_file)
    player.play()




@app.route("/Home")
def Home():
    command = request.args.get('search')
    print(command)
    if 'Play' in command:

        song = command.replace('Play', '')


        sss='playing ' + song
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert1.mp3")
        #playsound("static//alert1.mp3")
        play("static//alert1.mp3")
        pywhatkit.playonyt(song)





    elif 'Time' in command:

        time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        sss = 'Date' + time
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert2.mp3")
        play("static/alert2.mp3")


    elif 'Wikipedia' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        sss =  info
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert3.mp3")
        play("static//alert3.mp3")




    elif 'Date' in command:
        #talk('sorry, I have a headache')


        sss ='sorry I have a headache'
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert4.mp3")
        play("static//alert4.mp3")

    elif 'Are you single' in command:
        #talk('I am in a relationship with wifi')
        sss = 'I am in a relationship with wifi'
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert5.mp3")
        play("static//alert5.mp3")


    elif 'Joke' in command:
        #talk(pyjokes.get_joke())
        sss = pyjokes.get_joke()
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert6.mp3")
        play("static//alert6.mp3")

    else:
        #talk('Please say the command again.')
        sss = 'Please say the command again.'
        tts = gtts.gTTS(sss, lang="es")
        tts.save("static/alert7.mp3")
        play("static//alert7.mp3")







    return render_template('index.html')










if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
