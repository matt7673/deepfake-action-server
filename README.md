# deepfake-action-server
Action server for playing audio generated with ElevenLabs.Intended to be used in conjuction with elevenlabs-voice-manager: https://github.com/matt7673/elevenlabs-voice-manager 

## Installation

Elevenlabslib is required, you can install it with ```pip install elevenlabslib```.

On Linux, you may also need portaudio. On debian and derivatives, you can install with ```sudo apt-get install libportaudio2```, and possibly also ``sudo apt-get install python3-pyaudio``.

## Usage

Action server takes two requests, scipt_name and voice_name. voice_name should be identical to a matching directory inside voiceProfiles. script_name should match with either an audiofile in the voice_name's generatedAudio directory or with a text file in the script directory. Do not include the file extension. 

voiceProfile and scripts directories are assumed to be found in a directory named resources on the same level as deep_fake and deep_fake_msgs. If you plan to put them somewhere else, please update the path to them in the deep_fake.py script. They need to be inside the same directory. They also must have the same structure as their counterparts from elevenlabs-voice-manager, copy and replacing them from there is optimal.
