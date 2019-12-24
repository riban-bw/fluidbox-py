#! /usr/bin/python3

# Fluidbox is a Fluidsynth with web interface and automatic MIDI input routing
# riban 2019
# brian@riban.co.uk

import fluidsynth
import config
import util
import tornado.web
import tornado.ioloop
import os
import glob

from lib.dashboard_handler import DashboardHandler
from lib.upload_handler import UploadHandler
from lib.soundfont_handler import SoundfontHandler
from lib.effects_handler import EffectsHandler


def make_app():
	settings = {
		"template_path": "templates"
	}
	return tornado.web.Application([
		(r'/$', DashboardHandler),
		(r'/upload', UploadHandler),
		(r'/soundfont', SoundfontHandler),
		(r'/effects', EffectsHandler)
		], **settings)

if __name__ == "__main__":
	app = make_app()
	app.listen(8000)

	config.synth=fluidsynth.Synth(MidiAutoconnect=1, cores=3, SynthChorusActive=0, SynthReverbActive=0)
	config.synth.start(driver="alsa", midi_driver="alsa_seq")
	sfFiles = [f for f in glob.glob("./sf2/**/*.sf2", recursive=True)]
	for f in sfFiles:
		config.fonts.append(f[6:])

	util.loadConfig()
	util.loadSoundfont(config.config['current_font'], save=False)

	tornado.ioloop.IOLoop.current().start()

