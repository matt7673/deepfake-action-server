# deepfake-action-server
Action server for playing audio generated with ElevenLabs.Intended to be used in conjuction with elevenlabs-voice-manager: https://github.com/matt7673/elevenlabs-voice-manager 

## Installation

Elevenlabslib is required, you can install it with ```pip install elevenlabslib```.

On Linux, you may also need portaudio. On debian and derivatives, you can install with ```sudo apt-get install libportaudio2```, and possibly also ``sudo apt-get install python3-pyaudio``.

## Usage

Action server takes two requests, scipt_name and voice_name. voice_name should be identical to a matching directory inside voiceProfiles. script_name should match with either an audiofile in the voice_name's directory or with a text file in the script directory. Do not include the file extension. 

voiceProfile and scripts directories can be found in the resources folder, if you relocate them please update the path to them in the deep_fake.py script. Initially these two directories are empty, they should have the same structure as their counterparts from elevenlabs-voice-manager, copy and replacing them from there is optimal.