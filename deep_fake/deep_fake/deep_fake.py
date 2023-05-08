import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from deep_fake_msgs.action import DeepFakeRequest

import os
from elevenlabslib.helpers import *
from elevenlabslib import *

# directory where scripts and voiceProfiles is located
# assumed to be located in a folder in the src directory. first gets path of where this file is, then travels
# up two times and adds the folder name to the path, here it is assumed to be called resources
# can be changed to your liking just make sure that base path is the path to where scripts and voiceProfiles are.
basePath = os.path.dirname(os.path.realpath(__file__))
basePath = os.path.dirname(basePath)
basePath = os.path.dirname(basePath)
dirName = 'resources'
basePath += f'/{dirName}'

class DeepFakeActionServer(Node):

    def __init__(self):
        super().__init__('deep_fake_action_server')
        self._action_server = ActionServer(
            self,
            DeepFakeRequest,
            'read_script',
            self.execute_callback)
        

    def execute_callback(self, goal_handle):
        request =  goal_handle.request
        self.get_logger().info('Playing audio for ' + request.voice_name + " reading " + request.script_name)
        apiKey = os.environ.get("apiKey")
        success = self.playScript(request.script_name, request.voice_name, apiKey)
        result = DeepFakeRequest.Result()

        if success:   
            result.status = "success"
            goal_handle.succeed()
        else:
            result.status = 'failure'
            goal_handle.abort()
            
        return result
    
    # plays audio of script
    # scriptName: string, name of script
    # voiceName: string, name of voice, must match with directory name
    # apikey: elevenlabs api profile key
    # returns True if script played successfuly, False if an error occured trying to play
    def playScript(self, scriptName, voiceName, apikey):
        # login user
        user = ElevenLabsUser(apikey)

        voicePath = basePath + f'/voiceProfiles/{voiceName}'
        filePath = voicePath + f'/generatedAudio'
        # store path for location of script text file
        scriptPath = basePath + f'/scripts/{scriptName}.txt'
        

        # check to make sure voice profile exists
        if os.path.exists(voicePath):
            try:
                # path for audio file
                tempPath = filePath + f"/{scriptName}.wav"
                play_audio_bytes(open(tempPath,"rb").read(),False)

            except FileNotFoundError:
                print(f"No file found for script {scriptName} at filepath {tempPath}, generating audio and saving")
                voiceProfile = user.get_voices_by_name(voiceName)[0] #grab user from elevenlabs

                # read script file 
                with open(scriptPath, 'r') as file:
                    script = file.read().replace('\n', ' ')

                #Generate the audio using the script
                audioData = voiceProfile.generate_and_play_audio(script, stability=0.4, playInBackground=False)

                #Save audio
                savePath = filePath + f"/{scriptName}.wav"
                # save_audio_bytes(audioData, savePath, outputFormat="wav")
                with open(savePath, mode='bx') as file:
                    file.write(audioData)


        # no profile, abort
        else:
            print(f"No profile found for {voiceName}.")
            return False

        return True

def main(args=None):
    rclpy.init(args=args)

    action_server = DeepFakeActionServer()

    rclpy.spin(action_server)


if __name__ == '__main__':
    main()