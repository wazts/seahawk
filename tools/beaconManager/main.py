from gi.repository import Gtk
from beaconRest import *

class Handler:
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	def onButtonPressed(self, button):
		content = get_beacons()
		for item in content:
			print (get_user (userId=1))


## The main function
def main ():

	# Build from the glade file
	builder = Gtk.Builder()
	builder.add_from_file("BeaconMgr.glade")

	# Connect the handlers
	builder.connect_signals(Handler())

	# Get the main window
	window = builder.get_object ("main_window")
	window.show_all()

	Gtk.main()

if __name__ == '__main__':
	main()




