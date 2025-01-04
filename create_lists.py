import os
from pathlib import Path

def create_lists():
    # audio_data 디렉토리 경로
    audio_dir = Path('my_diarization_setup/audio_data')
    lists_dir = Path('my_diarization_setup/lists')
    
    # 파일 분류를 위한 딕셔너리
    file_categories = {
        'train': [],
        'dev': [],
        'test': []
    }
    
    # audio_data 디렉토리에서 .wav 파일 검색
    for audio_file in audio_dir.glob('*.wav'):
        base_name = audio_file.stem  # 확장자 제외한 파일명
        
        # 파일명에 따라 분류
        if base_name.startswith('train'):
            file_categories['train'].append(base_name)
        elif base_name.startswith('dev'):
            file_categories['dev'].append(base_name)
        elif base_name.startswith('test'):
            file_categories['test'].append(base_name)
    
    # 각 카테고리별로 리스트 파일 생성
    for category, files in file_categories.items():
        list_file = lists_dir / f'{category}.list.txt'
        with open(list_file, 'w', encoding='utf-8') as f:
            for file_name in sorted(files):
                f.write(f'{file_name}\n')

if __name__ == "__main__":
    create_lists()
    print("리스트 파일이 성공적으로 생성되었습니다!") 