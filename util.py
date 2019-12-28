import config
import fluidsynth
import json

def saveConfig():
	try:
		with open('./config.json', 'w') as f:
			json.dump(config.config, f)
			config.dirty = False
	except Exception as e:
		print("Failed to save configuration to json file")
		print (e)

def loadConfig():
	try:
		with open('./config.json', 'r') as f:
			config.config = json.load(f)
			config.dirty = False
	except Exception as e:
		print("Failed to load configuration from json file - using defaults")
		print(e)

def loadSoundfont(sSoundfont, save=True):
	config.dirty = True
	try:
		if config.current_font_nr > 0:
			config.synth.sfunload(config.current_font_nr)
			config.current_font_nr = 0
			config.config['current_font'] = None
	except Exception as e:
		print("Failed to unload soundfont")
		print(e)

	try:
		nSoundfont = config.synth.sfload("./sf2/" + sSoundfont, 1)
		if nSoundfont > 0:
			config.config['current_font'] = sSoundfont
			config.current_font_nr = nSoundfont
			print("Loaded soundfont: " + config.config['current_font'])
			if save == True:
				saveConfig()
	except Exception as e:
		print("Failed to load soundfont: " + sSoundfont)
		print(e)


