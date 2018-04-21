# Reddit-Guestbook

==Work in Progress==

~~~~~~~~~~~
Description
~~~~~~~~~~~

A Flask web app where users can sign a guest book by entering their name and a message into a web form. This project was designed to serve as an exercise both in implementing a SQLite3 type database and placing a Python application in a Docker container for deployment on an Ubuntu server. 

~~~~~~~~~~~~
Requirements:
~~~~~~~~~~~~
WTForms==2.1

Flask==0.12.2

Flask_WTF==0.14.2

~~~~~~~~~~~~
How to run:
~~~~~~~~~~~~

**Without Docker**

1. Clone repo
2. Open Reddit-Guestbook folder
3. Open terminal and pip install requirements.txt (i.e. `$ pip install -r requirements.txt`)
4. In terminal, use python to run rgb.py (i.e. `$ python3 rgb.py`)
5. Open browser and navigate to the localhost port 5000 (i.e. http://127.0.0.1:5000/)
6. Enjoy the program :) 

**With Docker**
1. Install Docker if you do not already have it (See Docker website https://docs.docker.com/install/)
2. Clone repo
3. Open Reddit-Guestbook folder
4. Open terminal
5. Type: `$ sudo docker build -t reddit-guest-book:latest .`
6. Type: `4 sudo docker run -d -p 5000:5000 reddit-guest-book`
7. Open browser and navigate to the localhost port 5000 (i.e. http://127.0.0.1:5000/)
8. Enjoy the program :)

~~~~~~~
Useage:
~~~~~~~

**The landing page**

![Alt text](/readme_images/home.png?raw=true "The landing page")

**Enter you name/username and a message**

![Alt text](/readme_images/submit.png?raw=true "Enter you name/username and a message")

**View your submission and see what other people wrote :)**

![Alt text](/readme_images/view.png?raw=true "View your submission and see what other people wrote :)")


