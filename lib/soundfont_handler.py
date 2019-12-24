import tornado.web
import config
import util
import os

class SoundfontHandler(tornado.web.RequestHandler):
	def post(self):
		sfDelete = (self.get_argument("delete", None))
		sfSelect = (self.get_argument("select", None))
		if sfDelete != None:
			try:
				os.remove("./sf2/" + sfDelete)
				config.fonts.remove(sfDelete)
			except:
				print("Failed to delete soundfont file: " + sfDelete)
		if sfSelect != None:
			util.loadSoundfont(sfSelect)

		self.redirect('/')

