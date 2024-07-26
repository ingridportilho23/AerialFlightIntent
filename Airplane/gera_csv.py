import os
import csv
import ffmpeg
from datetime import datetime

def get_video_metadata(file_path):
    try:
        probe = ffmpeg.probe(file_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream:
            duration = float(video_stream.get('duration', 0))
            width = int(video_stream.get('width', 0))
            height = int(video_stream.get('height', 0))
            frame_rate = eval(video_stream.get('r_frame_rate', '0/1'))
            codec_name = video_stream.get('codec_name', 'unknown')
            fps = round(frame_rate, 2) if frame_rate else 0
            return duration, width, height, fps, codec_name
        else:
            print(f"No video stream found in {file_path}")
            return 0, 0, 0, 0, 'unknown'
    except Exception as e:
        print(f"Could not get metadata for {file_path}: {e}")
        return 0, 0, 0, 0, 'unknown'

def rename_csv_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.mp4.csv'):
            old_csv_path = os.path.join(directory, filename)
            new_csv_path = os.path.join(directory, filename.replace('.mp4.csv', '.csv'))
            os.rename(old_csv_path, new_csv_path)
            print(f'Renamed: {old_csv_path} to {new_csv_path}')

def rename_files_and_create_csv(base_directory):
    main_dir = os.path.basename(base_directory)
    metadata_file = os.path.join(base_directory, f'{main_dir}_metadata.csv')
    
    # Garantir que o diretório base exista
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
    
    with open(metadata_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['FileName', 'FileSize', 'ModificationDate', 'Duration', 'Resolution', 'FrameRate', 'Format', 'Class'])

        for class_dir in os.listdir(base_directory):
            class_path = os.path.join(base_directory, class_dir)
            if os.path.isdir(class_path):
                rename_csv_files(class_path)  # Renomear arquivos CSV primeiro
                file_count = 1
                for filename in os.listdir(class_path):
                    if filename.endswith('.mp4'):
                        old_mp4_path = os.path.join(class_path, filename)
                        new_mp4_name = f'{main_dir}_{class_dir}_{file_count}.mp4'
                        new_mp4_path = os.path.join(class_path, new_mp4_name)

                        old_csv_name = filename.replace('.mp4', '.csv')
                        old_csv_path = os.path.join(class_path, old_csv_name)
                        new_csv_name = f'{main_dir}_{class_dir}_{file_count}.csv'
                        new_csv_path = os.path.join(class_path, new_csv_name)

                        # Obter metadados antes de renomear
                        duration, width, height, fps, codec_name = get_video_metadata(old_mp4_path)
                        resolution = f"{width}x{height}" if width and height else 'unknown'
                        file_size = os.path.getsize(old_mp4_path)
                        modification_date = datetime.fromtimestamp(os.path.getmtime(old_mp4_path)).strftime('%Y-%m-%d %H:%M:%S')

                        # Renomear arquivos
                        if not os.path.exists(new_mp4_path):
                            os.rename(old_mp4_path, new_mp4_path)
                            print(f'Renamed: {filename} to {new_mp4_name}')
                        else:
                            print(f'Skipped: {new_mp4_name} already exists')

                        if os.path.exists(old_csv_path):
                            if not os.path.exists(new_csv_path):
                                with open(old_csv_path, mode='r', newline='', encoding='utf-8') as infile, open(new_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
                                    reader = csv.reader(infile)
                                    writer_csv = csv.writer(outfile)
                                    headers = next(reader)
                                    writer_csv.writerow(headers)
                                    for row in reader:
                                        row[0] = new_mp4_name  # Atualizar o nome do arquivo no conteúdo do CSV
                                        writer_csv.writerow(row)
                                os.remove(old_csv_path)
                                print(f'Renamed and updated content: {old_csv_name} to {new_csv_name}')
                            else:
                                print(f'Skipped: {new_csv_name} already exists')
                        else:
                            print(f'Skipped: {old_csv_name} does not exist')

                        # Escrever metadados no CSV
                        writer.writerow([new_mp4_name, file_size, modification_date, duration, resolution, fps, codec_name, f"{main_dir}_{class_dir}"])
                        print(f'Added metadata for {new_mp4_name}')

                        # Incrementar a contagem de arquivos
                        file_count += 1

base_directory_path = r'C:\Users\yngri\Downloads\AerialFlightIntent818\Airplane'
rename_files_and_create_csv(base_directory_path)
