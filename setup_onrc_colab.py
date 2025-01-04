import os
import subprocess
from google.colab import drive

def setup_onrc():
    print("1. Google Drive 마운트 중...")
    drive.mount('/content/drive')
    
    print("2. 필요한 패키지 설치 중...")
    subprocess.run("pip install -qq pyannote.audio==3.1.1", shell=True)
    subprocess.run("pip install -qq ipython==7.34.0", shell=True)
    
    print("3. ONRC-diarization-setup 클론 중...")
    subprocess.run("git clone https://github.com/your-username/ONRC-diarization-setup.git", shell=True)
    
    print("4. 오디오 데이터 복사 중...")
    subprocess.run("cd ONRC-diarization-setup/pyannote && bash download_onrc_mini.sh", shell=True)
    
    print("설정 완료!")

if __name__ == "__main__":
    setup_onrc() 