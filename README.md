seahawk
=======

# About
Seahawk is a simple tool for updating and using data collected from beacon interactions using Bluetooth LE devices. Currently the server archetecture uses a web front end powered by Django and Django REST Framework. There are no API details yet as this is still in planning.

The server side stack is geared for Heroku and has all the neccessary files to work with no modification except to the environment configuration file.

# Installation
Seahawk uses python as a backend and the RESTful API runs on Django. To setup the proper environment on Linux, you first need VirtualEnv for sandboxing the python environment.

    apt-get install python-virtualenv

Alternatively, you can install pip and then do `pip install virtualenv`.

Once VirtualEnv is installed, move into the cloned seahawk repo to create the virtual environment and set the shell in the environment.

    virtualenv venv
    source venv/bin/activate

This creates a sandbox with pip installed and allows you to control the packages used in the system. 

Next, install all the neccessary packages for the code to run. To do this use `pip` and the `requirements.txt`.

    pip install -r requirements.txt

This should install everything needed to run the system.