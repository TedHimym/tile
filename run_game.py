import sys, os
try: 
	libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
	sys.path.insert(0, libdir)
except:
	pass

from game import game
game.run()


