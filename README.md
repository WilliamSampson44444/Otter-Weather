# Otter Weather


## Prerequisites
* Python 3
* Any modern browser

## Installation
Clone this repository to a directory of your choice, and run the following command in a fresh Python 3 Virtual Environment:
```
pip install -r /path/to/requirements.txt
```
(With "/path/to/requirements.txt" replaced with a path to this program's requirements.txt file.)

## Running

#### Bash
There are two options. In the root of the Otter Weather directory:
* Enter `chmod +x flaskrun.sh`
    * (Only needs to be done once) 
* Followed by `source flaskrun.sh`
    * This script will automatically run app.py via Flask.

#### Powershell
While in the directory of the Otter Weather app, enter the command `.\flaskrun.ps1` into your Powershell, and press enter.

### Accesing Webpage
In your browser, enter whatever local IP Flask has chosen for the app and press enter.
* Default IP should be `127.0.0.1:5000`


## Built With

### Python Modules
* Flask
* Flask-Bootstrap
* OpenCV
* Pillow
* requests

### APIs
* Google Maps: cloud.google.com/maps-platform/
* Openweathermap: www.openweathermap.org
* Zipcode API: www.zipcodeapi.com


## Authors
#### Nayeli De Jesus
#### William Sampson
#### Waleed Shaikh
#### Mark Trantham
#### Joseph Villegas


## License
This project is licensed under the MIT license.
