import tornado.web
import fluidsynth
import config
import util

class EffectsHandler(tornado.web.RequestHandler):
	def post(self):
		# Reverb
		bEnable = (self.get_argument('enable_reverb', False))
		config.config['reverb_enable'] = bEnable
		config.synth.enable_reverb(bEnable)
		config.config['reverb_roomsize'] = float(self.get_argument('reverb_roomsize', 0))/100
		config.config['reverb_damping'] = float(self.get_argument('reverb_damping', 0))/100
		config.config['reverb_width'] = float(self.get_argument('reverb_width', 0))/100
		config.config['reverb_level'] = float(self.get_argument('reverb_level', 0))/100
		config.synth.set_reverb(roomsize=config.config['reverb_roomsize'], damping=config.config['reverb_damping'], width=config.config['reverb_width'], level=config.config['reverb_level'])
		# Chorus
		bEnable = (self.get_argument('enable_chorus', False))
		config.config['chorus_enable'] = bEnable
		config.synth.enable_chorus(bEnable)
		config.config['chorus_nr'] = int(self.get_argument('chorus_nr', 0))
		config.config['chorus_level'] = float(self.get_argument('chorus_level', 0))/10
		config.config['chorus_speed'] = float(self.get_argument('chorus_speed', 0))/20
		config.config['chorus_depth'] = float(self.get_argument('chorus_depth', 0))/10
		config.config['chorus_type'] = int(self.get_argument('chorus_type', 0))
		print(config.config['chorus_type'])
		config.synth.set_chorus(nr=config.config['chorus_nr'], level=config.config['chorus_level'], speed=config.config['chorus_speed'], depth=config.config['chorus_depth'], type=config.config['chorus_type'])

		util.saveConfig()

		self.redirect('/')

