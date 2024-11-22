# SmartMenue

## Installation
1. Clone the repository: https://github.com/GuillaumeBrgnFR/SmartMenue.git

2. Create a virtual environment and activate it. (Optional but recommended)
Execute the command `python -m venv venv` (or `python3.9 -m venv venv`) to create the virtual environment.
Execute the command `source venv/bin/activate` to activate the virtual environment.

3. Execute the command `pip install -r requirements.txt` to install the dependencies.

4. Execute the command `npm install` from the `frontend` directory to install the dependencies.
You have to install Node.js and npm to do this.

5. Execute the command `npm run build` from the `frontend` directory to build the frontend.


## Usage
1. Execute the command `pwd` to get the path of the project. Then, execute the command `export PYTHONPATH="copy_pwd_result"` to set the PYTHONPATH environment variable.

2. Execute the command `python src/web-app/app.py` to start the flask server.

3. In another terminal, execute the command `npm start` from the `frontend` directory to start the frontend.

4. Open your browser and go to `http://localhost:5000/` to use the application.


## With Docker
1. Download the Docker image from the Docker Hub.
2. Execute the command `docker run -p 5001:5000 guillaumebourgain/smartmenue:latest` to start the container.
3. Open your browser and go to `http://localhost:5001/` to use the application.


## Features
- Upload a menu in jpg, jpeg or png format.
- Extract the text from the menu.
- Display the menu with a formal presentation.
- Possibility to modify the menu.


## Warning
The project is tested on macOS and with Python 3.9. It doesn't work with Python 3.13. 
