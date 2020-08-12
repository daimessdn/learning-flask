# learning-flask
This is the tutorial of learning `Flask`, a web framework in Python.

# languages features
- Python, contains library (in [requirements.txt](https://github.com/daimessdn/learning-flask/blob/master/requirements.txt))
  - Flask@1.1.1

# installation within this repository
- Clone this repository by
  - using **Terminal** (on Mac or Linux) or **Git Bash** (on Windows), type (assumning `git` has been installed) 
  ```bash
  git clone https://github.com/daimessdn/learning-flask.git
  ```
  or
  - [**clicking here**](https://github.com/daimessdn/learning-flask/archive/master.zip)
- Still using terminal console, navigate to the main console.<br />
  ```bash
  cd learning-flask
  ```
- Still in terminal console, type to activate virtual environment
  ```
  # on MacOS or Linux
  virtualenv venv
  source venv/bin/activate

  # on Windows
  venv\scripts\activate
  ```
- Install Python dependencies inside `requirements.txt`
  ```bash
  pip install -r requirements.txt
  ```
- Now we can use Flask directly by
  ```bash
  python hello.py
  ```