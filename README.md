seahawk
=======

# About
Seahawk is a simple tool for updating and using data collected from beacon interactions using Bluetooth LE devices. Currently the server archetecture uses a web front end powered by Django and Django REST Framework. There are no API details yet as this is still in planning.

The server side stack is geared for Heroku and has all the neccessary files to work with no modification except to the environment configuration file.

# Installation
Seahawk uses python as a backend and the RESTful API runs on Django. To setup the proper environment on Linux, you first need VirtualEnv for sandboxing the python environment.

    $ python3 -m venv myvenv
	$ source myvenv/bin/activate
	(myvenv)$

	(myvenv)$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

	(myvenv)$ deactivate
	$ source myvenv/bin/activate
	(myvenv)$ which pip

This creates a sandbox with pip installed and allows you to control the packages used in the system. 

Next, install all the neccessary packages for the code to run. To do this use `pip` and the `requirements.txt`. Some of the packages require other libraries/packages on the system.
	
	libpq-dev (Ubuntu/Debian) or postgresql-devel
	python-dev

After those are installed you can use the following to get the necessary packages.

    pip install -r requirements.txt

This should install everything needed to run the system.