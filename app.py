from flask import Flask, render_template, request

app = Flask(__name__)

# Mapping moods to song suggestions
mood_songs = {
    'Happy': [
        'https://www.youtube.com/watch?v=4fndeDfaWCg',  # Pharrell Williams - Happy
        'https://www.youtube.com/watch?v=qJJiUGaL-lQ',  # Neha Kakkar - Dilbar
        'https://www.youtube.com/watch?v=70evfUG5ut8',  # "Baarish" - Vishal Mishra (Kannada)
    ],

    'Sad': [
        'https://www.youtube.com/watch?v=YQHsXMglC9A',  # Adele - Hello
        'https://www.youtube.com/watch?v=BLZlVt7rix0',  # Arijit Singh - Channa Mereya
        'https://www.youtube.com/watch?v=FOVsUvN1PYc',  # "Ninna Nodalenthu" - Karthik (Kannada)
    ],

    'Excited': [
        'https://www.youtube.com/watch?v=ktvTqknDobU',  # Katy Perry - Firework
        'https://www.youtube.com/watch?v=5Y60lsz_tA0',  # Badshah - Genda Phool
        'https://www.youtube.com/watch?v=At86lY2f8U8',  # "Buddhi Manja" - Puneeth Rajkumar (Kannada)
    ],

    'Angry': [
        'https://www.youtube.com/watch?v=3M_5mVg3v0Y',  # Eminem - The Real Slim Shady
        'https://www.youtube.com/watch?v=6hvFEf4_Za0',  # Divine - Mirchi
        'https://www.youtube.com/watch?v=uM4Gn3t5V1Q',  # "Chakra" - Kiccha Sudeep (Kannada)
    ],
}



@app.route('/', methods=['GET', 'POST'])
def index():
    songs = []
    if request.method == 'POST':
        mood = request.form.get('mood')
        songs = mood_songs.get(mood, [])
    
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
