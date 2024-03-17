from flask import Flask, render_template, request
import requests
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/voice_list')
def voice_list():
    url = "https://text-to-speech-google-neural.p.rapidapi.com/voices"
    headers = {
        "X-RapidAPI-Key": "19cc2eee97mshe979bc8b599a029p14567bjsn92e68abe5a3e",
	    "X-RapidAPI-Host": "text-to-speech-google-neural.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return render_template('voice_list.html', voices=data)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/text2speech', methods=['GET', 'POST'])
def text2speech():
    if request.method == 'POST':
        text = request.form['text']
        voice_id = request.form['voice_id']
        url = "https://text-to-speech-google-neural.p.rapidapi.com/text-to-speech/onwK4e9ZLuTAKqWW03F9/stream"
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_id": voice_id
        }
        headers = {
            "content-type": "application/json",
	        "X-RapidAPI-Key": "19cc2eee97mshe979bc8b599a029p14567bjsn92e68abe5a3e",
	        "X-RapidAPI-Host": "text-to-speech-google-neural.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"static/history/speech_{timestamp}.mp3"
            audio_content = response.content
            with open(file_name, "wb") as f:
                f.write(audio_content)
            return render_template('text2speech.html', success=True, timestamp=timestamp)
        else:
            return render_template('text2speech.html', error="Failed to convert text to speech", voices=data, selected_voice=voice_id)

    else:  
        url = "https://text-to-speech-google-neural.p.rapidapi.com/voices"
        headers = {
            "X-RapidAPI-Key": "19cc2eee97mshe979bc8b599a029p14567bjsn92e68abe5a3e",
	        "X-RapidAPI-Host": "text-to-speech-google-neural.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()['voices']
            selected_voice = request.form.get('voice_id')
            return render_template('text2speech.html', voices=data, selected_voice=selected_voice)
        else:
            return render_template('text2speech.html', error="Failed to retrieve voices", voices=None, selected_voice=None)

@app.route('/about')
def  about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
