import config
import fluidsynth
import json

def saveConfig():
	try:
		with open('./config.json', 'w') as f:
			json.dump(config.config, f)
			config.dirty = False
	except:
			print("Failed to save configuration to json file")

def loadConfig():
	try:
		with open('./config.json', 'r') as f:
			config.config = json.load(f)
			config.dirty = False
	except:
		print("Failed to load configuration from json file")

def loadSoundfont(sSoundfont, save=True):
	config.dirty = True
	try:
		if config.config['current_font_nr'] > 0:
			config.synth.sfunload(config.current_font_nr)
			config.config['current_font_nr'] = 0
			config.config['current_font'] = None
	except:
		print("Failed to unload soundfont")

	try:
		nSoundfont = config.synth.sfload("./sf2/" + sSoundfont, 1)
		if nSoundfont > 0:
			config.config['current_font'] = sSoundfont
			config.config['current_font_nr'] = nSoundfont
			print("Loaded soundfont: " + config.config['current_font'])
			if save == True:
				saveConfig()
	except:
		print("Failed to load soundfont: " + sSoundfont)


