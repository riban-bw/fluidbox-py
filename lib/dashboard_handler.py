import tornado.web
import config

class DashboardHandler(tornado.web.RequestHandler):

	def get(self):
		super().render("dashboard.html", title="riban fluidbox dashboard", fonts=config.fonts, config=config.config)
