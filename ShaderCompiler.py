import os
import subprocess

# If they fail to convert, try only converting for 120,150 or 150 instead of 100 es
# otherwise, debug the shader it self

# Paths
source_directory = 'package/contents/ui/Shaders6Originals/convert'
output_directory = 'package/contents/ui/Shaders6'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

DELETE_AFTER_COMPILATION = False

# Iterate over all .frag files in the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.frag'):
            # Construct the full path to the source file
            source_file_path = os.path.join(root, file)
            # Construct the output file path
            output_file_name = file.replace('.frag', '.frag.qsb')
            output_file_path = os.path.join(output_directory, output_file_name)
            # Construct and execute the command
            cmd = [
                'qsb', '--glsl', '100 es,120,150', '--hlsl', '50', '--msl', '12',
                '-o', output_file_path, source_file_path
            ]
            
            try:
                subprocess.run(cmd, check=True)
                # If the command was successful, delete the source file
                if (DELETE_AFTER_COMPILATION)
                    os.remove(source_file_path)
                print(f"Successfully converted and deleted: {file}")
            except subprocess.CalledProcessError:
                # If the command failed, do not delete the source file
                print(f"Conversion failed for: {file}")
