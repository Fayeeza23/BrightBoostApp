
User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ python --version
Python 3.11.4

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ pip --version
pip 23.2.1 from C:\Users\User\AppData\Local\Programs\Python\Python311\Lib\site-p
ackages\pip (python 3.11)

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ py -m venv brightboost

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ brightboost/Scripts/activate.bat


User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ py -m pip install Django

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ py --version
Python 3.11.4

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ django-admin --version
4.2.4

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ django-admin startproject bright_boost

// changing directory
User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost
$ cd bright_boost

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost/bright_boost
$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).




User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost/bright_boost
$ python manage.py migrate

User@LAPTOP-G4HDVPF0 MINGW64 /c/BrightBoost/bright_boost
$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 08, 2023 - 13:30:15
Django version 4.2.4, using settings 'bright_boost.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[08/Sep/2023 13:30:20] "GET / HTTP/1.1" 200 10664

commands to run when running the program : 
python manage.py makemigrations
python manage.py migrate 

python manage.py runserver