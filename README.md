# fluidbox
Raspberry Pi Fluidsynth Python with web interface

Fluidsynth is a soundfont player. This project provides an instance of Fluidsynth running on a Raspberry Pi. It uses a Python wrapper to host the Fluidsynth library and presents configuration via a web interface on port 8888. Configuration is persisted by a json file and soundfonts must exist in the sf2 subdirectory.

Soundfonts may be uploaded and deleted using the web interface.
Soundfonts may be selected using the web interface.
Reverb and chorus effects may be adjsuted using the web interface.
Control of note on / off and patch selection is via MIDI input.
All alas_seq MIDI inputs are automatically routed to the input of Fluidsynth including USB MIDI interfaces plugged after boot.
