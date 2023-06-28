import os
import subprocess

video_directory_path = r'I:\I Drive Video Master Folder\1_test_saul'
output_directory_path = r'I:\I Drive Video Master Folder\1_test_saul_export'

for video_file in os.listdir(video_directory_path):
    if video_file.endswith(('.mp4', '.flv', '.mov', '.avi', '.mkv')):
        base_name = os.path.splitext(video_file)[0]
        full_input_path = os.path.join(video_directory_path, video_file)
        full_output_path = os.path.join(output_directory_path, 'louder_subs_' + video_file)
        
        ## hardcode srt file or default existing embed
        srt_file_path = os.path.join(video_directory_path, base_name + '.srt')
        
        if os.path.isfile(srt_file_path):
            command = f'ffmpeg -i "{full_input_path}" -af "volume=10dB" -scodec mov_text -s "{srt_file_path}" -disposition:s:0 default "{full_output_path}"'
        else:
            command = f'ffmpeg -i "{full_input_path}" -af "volume=10dB" "{full_output_path}"'

        subprocess.call(command, shell=True)

print('Volume increase and subtitle embedding (where available) completed for all videos.')