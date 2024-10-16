import datetime

def delay_subtitles(input_file, output_file, delay_seconds):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    
    output_lines = []
    for line in lines:
        line = line.strip()
        if ' --> ' in line:
            # This is a timing line (format: 00:00:00.000 --> 00:00:00.000)
            try:
                start_end = line.split(' --> ')
                start_time = start_end[0]
                end_time = start_end[1]
                
                # Parse start and end times
                start_time_obj = datetime.datetime.strptime(start_time, '%H:%M:%S.%f')
                end_time_obj = datetime.datetime.strptime(end_time, '%H:%M:%S.%f')
                
                # Add delay
                start_time_delayed = start_time_obj + datetime.timedelta(seconds=delay_seconds)
                end_time_delayed = end_time_obj + datetime.timedelta(seconds=delay_seconds)
                
                # Format the new times in vtt format
                new_start_time = start_time_delayed.strftime('%H:%M:%S.%f')[:-3]
                new_end_time = end_time_delayed.strftime('%H:%M:%S.%f')[:-3]
                
                # Construct the new timing line
                new_timing_line = f"{new_start_time} --> {new_end_time}\n"
                output_lines.append(new_timing_line)
            except ValueError as e:
                print(f"Error parsing line '{line}': {e}")
                output_lines.append(line + '\n')
        else:
            output_lines.append(line + '\n')
    
    # Write the modified subtitles to the output file
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(output_lines)
        print(f"Delayed subtitles saved to '{output_file}'.")
    except IOError:
        print(f"Error writing to file '{output_file}'.")

# load input and output files
input_file = 'input.vtt'
output_file = 'output.vtt'
delay_seconds = 0.5

delay_subtitles(input_file, output_file, delay_seconds)
