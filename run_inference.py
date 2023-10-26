#@title
input_video_path = 'examples/face/{}'.format(default_vid_name.value)
input_audio_path = 'examples/audio/{}'.format(default_audio_name.value)

!python3 inference.py \
  --face {input_video_path} \
  --audio {input_audio_path} \
  --outfile results/output.mp4
