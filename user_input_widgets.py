#@title
import glob, os, sys
import ipywidgets as widgets
from IPython.display import HTML
from base64 import b64encode

print("Choose the Video name to edit: (saved in folder 'examples/face')")
vid_list = glob.glob1('examples/face/', '*.mp4')
vid_list.sort()
default_vid_name = widgets.Dropdown(options=vid_list, value='1.mp4')
display(default_vid_name)

print("Choose the Audio name to edit: (saved in folder 'examples/audio')")
audio_list = glob.glob1('examples/audio/', '*')
audio_list.sort()
default_audio_name = widgets.Dropdown(options=audio_list, value='1.wav')
display(default_audio_name)
