#!/bin/bash

if [ -z "$1" ]
then
      DLFOLDER="../../my_diarization_setup/audio_data"
else
      DLFOLDER="$1/audio_data"
fi

# 디렉토리 생성
mkdir -p "$DLFOLDER"

# Google Drive에서 데이터 복사
echo "Copying audio files from Google Drive..."
cp /content/drive/MyDrive/ONRC/*.wav "$DLFOLDER/"
cp /content/drive/MyDrive/ONRC/*.rttm "$DLFOLDER/"

# 파일 확인
echo "Checking copied files..."
ls -l "$DLFOLDER" 