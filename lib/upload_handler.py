import tornado.web
import config
import os

class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		files = []
		try:
			files = self.request.files['files']
		except:
			self.redirect('/')
		for xfile in files:
			path,ext = os.path.splitext(xfile['filename'])
			ext = ext.lower()
			filename = path + ext
			if ext != ".sf2":
				continue
			fileObj = open("./sf2/" + filename, 'wb')
			fileObj.write(xfile['body'])
			config.fonts.append(filename)
		self.redirect('/')

