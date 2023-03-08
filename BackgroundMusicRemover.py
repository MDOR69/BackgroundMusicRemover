import os
import shutil

from spleeter.separator import Separator
import warnings
import shlex
import subprocess


#Use spleeter's embedded configuration.
#separator = Separator('spleeter:5stems', multiprocess=False)
#separator.separate_to_file('test.mp4', '')

#Get all the files inside Input
files = os.scandir("Input")

#Get all the files inside
for file in files:
    #Remove the file extension
    file_name = str(file.name).split(".")[0]
    print("Starting with "+file_name)

    #Use Spleeter to cut out the music from the video
    separator = Separator('spleeter:5stems', multiprocess=False)
    separator.separate_to_file("Input/"+file.name, '')

    #Use FFMpeg to replace the audio track of the video with the output vocal track and write it to the output dir
    command = 'ffmpeg -y -i input/'+file.name+' -i '+ file_name +'/vocals.wav -c:v copy -map 0:v:0 -map 1:a:0 output/'+file_name+'_output.mp4'
    command = shlex.split(command)
    subprocess.call(command)
    shutil.rmtree(file_name)
    print(file_name+" is completed")

print("Done Isolating All Files")