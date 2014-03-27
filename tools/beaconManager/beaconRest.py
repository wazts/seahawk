import requests
import json

## Get the beacons from the server
def get_beacons():
	return request_url("http://0.0.0.0:5000/beacons")

## Get the user
def get_user (userId=-1, url=""):

	getUrl =""
	if (userId > 0):
		getUrl = 'http://0.0.0:5000/users/' + str(userId)
	elif url != "":
		getUrl = url

	return request_url (getUrl)

## Request a certain url
def request_url (url):
	r = requests.get (url)
	return r.json()