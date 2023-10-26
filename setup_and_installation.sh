#@title
### make sure that CUDA is available in Edit -> Nootbook settings -> GPU
!nvidia-smi

!python --version  
!apt-get update
!apt install ffmpeg &> /dev/null 

print('Git clone project and install requirements...')
!git clone https://github.com/vinthony/video-retalking.git &> /dev/null
%cd video-retalking
# !pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
!pip install -r requirements.txt
