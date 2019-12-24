import tornado.web
import fluidsynth
import config
import util

class EffectsHandler(tornado.web.RequestHandler):
	def post(self):
		# Reverb
		config.synth.enable_reverb(self.get_argument("enable_reverb", False))
		config.config['reverb_roomsize'] = float(self.get_argument('reverb_roomsize', 0))/100
		config.config['reverb_damping'] = float(self.get_argument('reverb_damping', 0))/100
		config.config['reverb_width'] = float(self.get_argument('reverb_width', 0))/100
		config.config['reverb_level'] = float(self.get_argument('reverb_level', 0))/100
		config.synth.set_reverb(roomsize=config.config['reverb_roomsize'], damping=config.config['reverb_damping'], width=config.config['reverb_width'], level=config.config['reverb_level'])
		# Chorus
		config.synth.enable_chorus(self.get_argument("enable_chorus", False))
		config.config['chorus_nr'] = float(self.get_argument('chorus_nr', 0))/100
		config.config['chorus_level'] = float(self.get_argument('chorus_level', 0))/100
		config.config['chorus_speed'] = float(self.get_argument('chorus_speed', 0))/100
		config.config['chorus_depth'] = float(self.get_argument('chorus_depth', 0))/100
		config.config['chorus_type'] = float(self.get_argument('chorus_type', 0))/100

		util.saveConfig()

		self.redirect('/')

