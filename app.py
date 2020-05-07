# filename: app.py

from api import *
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        location = get_user_location()
    
        lat = location['lat']
        lon = location['lon']

        current_forcast, daily_forcast, hourly_forcast = get_weather(lat, lon)

        return render_template('index.html', 
                               location = location, 
                               current_forcast = current_forcast, 
                               daily_forcast = daily_forcast,
                               hourly_forcast = hourly_forcast)

    elif request.method == 'POST':
        zip_code = request.form['zip_code']
        location = get_city(zip_code)
        if location['success']:
            lat = location['lat']
            lon = location['lon']
            current_forcast, daily_forcast, hourly_forcast = get_weather(lat, lon)
            return render_template('index.html', 
                                   location = location, 
                                   current_forcast = current_forcast, 
                                   daily_forcast = daily_forcast,
                                   hourly_forcast = hourly_forcast)
            
        return render_template('index.html', location = location)

@app.route('/about', methods=['GET'])
def about():      
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)