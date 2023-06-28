from datetime import datetime, timedelta

# Define the input and output paths
input_srt_file_path = r"I:\I Drive Video Master Folder\Better Call Saul - S01\S01E01_exp.srt"
output_srt_file_path = r"I:\I Drive Video Master Folder\Better Call Saul - S01\S01E01_exp2.srt"

# This is the amount of time to adjust
time_shift = timedelta(seconds=5)

with open(input_srt_file_path, 'r') as input_file, open(output_srt_file_path, 'w') as output_file:
    for line in input_file:
        if '-->' in line:  # This line contains timestamps
            start_time_str, end_time_str = line.strip().split(' --> ')

            # Parse the timestamps into datetime objects
            start_time = datetime.strptime(start_time_str, '%H:%M:%S,%f')
            end_time = datetime.strptime(end_time_str, '%H:%M:%S,%f')

            # Adjust the times
            start_time -= time_shift
            end_time -= time_shift

            # Format the new timestamps and write them to the output file
            line = f"{start_time.strftime('%H:%M:%S,%f')[:-3]} --> {end_time.strftime('%H:%M:%S,%f')[:-3]}\n"
        
        output_file.write(line)

print(f'SRT file has been adjusted and saved to {output_srt_file_path}.')
