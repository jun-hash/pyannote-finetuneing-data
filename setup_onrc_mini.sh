#!/bin/bash

# 작업 디렉토리 생성
mkdir -p my_diarization_setup
cd my_diarization_setup

# 필요한 디렉토리 구조 생성
mkdir -p pyannote
mkdir -p audio_data
mkdir -p lists
mkdir -p uems/train uems/dev uems/test

# lists 파일 생성
cat > lists/train.list.txt << EOL
ONRC_EP3_1
ONRC_EP3_2
EOL

cat > lists/dev.list.txt << EOL
ONRC_EP3_3
EOL

cat > lists/test.list.txt << EOL
ONRC_EP3_4
EOL

# database.yml 파일 생성
cat > pyannote/database.yml << EOL
Databases:
  MyDatabase:
    audio: ../audio_data/{uri}.wav

Protocols:
  MyDatabase:
    SpeakerDiarization:
      mini:     # 테스트용 
        train:
          uri: ../lists/train.list.txt
          annotation: ../audio_data/{uri}.rttm
        development:
          uri: ../lists/dev.list.txt
          annotation: ../audio_data/{uri}.rttm
        test:
          uri: ../lists/test.list.txt
          annotation: ../audio_data/{uri}.rttm

      full:     # 전체 데이터셋용 (향후 확장)
        train:
          uri: ../lists/train.full.txt
          annotation: ../audio_data/{uri}.rttm
        development:
          uri: ../lists/dev.full.txt
          annotation: ../audio_data/{uri}.rttm
        test:
          uri: ../lists/test.full.txt
          annotation: ../audio_data/{uri}.rttm
EOL

# 안내 메시지 출력
echo "디렉토리 구조가 생성되었습니다."
echo "audio_data 폴더에 ONRC wav 파일과 rttm 파일을 업로드해주세요." 