import os

def rttm_to_uem(rttm_file_path, uem_file_path):
    """
    RTTM 파일을 읽어 UEM 파일을 생성합니다.
    """
    with open(rttm_file_path, 'r') as rttm_file, open(uem_file_path, 'w') as uem_file:
        for line in rttm_file:
            parts = line.strip().split()
            if parts and parts[0] == "SPEAKER":
                file_id = parts[1]
                start_time = float(parts[3])
                duration = float(parts[4])
                end_time = start_time + duration
                uem_file.write(f"{file_id} 1 {start_time:.3f} {end_time:.3f}\n")

def process_rttm_folder(rttm_folder):
    """
    RTTM 폴더 내의 각 RTTM 파일마다 같은 위치에 동일한 이름의 UEM 파일을 생성합니다.
    """
    for filename in os.listdir(rttm_folder):
        if filename.endswith('.rttm'):
            rttm_path = os.path.join(rttm_folder, filename)
            uem_path = os.path.join(rttm_folder, filename.replace('.rttm', '.uem'))
            
            # 각 RTTM 파일에 대해 UEM 생성
            rttm_to_uem(rttm_path, uem_path)
            print(f"UEM 파일이 생성되었습니다: {uem_path}")

if __name__ == "__main__":
    # 현재 스크립트의 디렉토리를 기준으로 상대 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rttm_folder = os.path.join(current_dir, "rttm")
    
    # RTTM 폴더가 존재하는지 확인
    if not os.path.exists(rttm_folder):
        print(f"Error: RTTM 폴더를 찾을 수 없습니다: {rttm_folder}")
    else:
        process_rttm_folder(rttm_folder)
        print(f"모든 RTTM 파일들이 처리되어 UEM 파일들이 생성되었습니다.")