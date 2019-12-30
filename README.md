# fluidbox-py
*NOTE: This project is superceeded by c++ implementation*
Raspberry Pi Fluidsynth Python with web interface

Fluidsynth is a soundfont player. This project provides an instance of Fluidsynth running on a Raspberry Pi. It uses a Python wrapper to host the Fluidsynth library and presents configuration via a web interface on port 8888. Configuration is persisted by a json file and soundfonts must exist in the sf2 subdirectory.

Soundfonts may be uploaded and deleted using the web interface.
Soundfonts may be selected using the web interface.
Reverb and chorus effects may be adjsuted using the web interface.
Control of note on / off and patch selection is via MIDI input.
All alas_seq MIDI inputs are automatically routed to the input of Fluidsynth including USB MIDI interfaces plugged after boot.

The web interface may be accessed from http://<hostname>:8888. From here you can see the currently selected soundfont, select a different soundfont, delete (non-default(1)) soundfonts, upload new soundfonts, enable and adjust parameters of reverb and chorus effects.

(1) A symlink is created from sf2/default to /usr/share/sounds/sf2 and this content is regarded as default soundfonts and may not be deleted.
  
* Dependencies
Fluidbox depends on the following software modules:
* Fluidsynth 2.1
* pyfluidsynth with patches for fluidsynth 2.1 (https://github.com/riban-bw/pyfluidsynth)
* Python 3
* alsa_seq

