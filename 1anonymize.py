import os
import re

# Set the path to the parent directory to the folder the script is currently in
parent_directory = os.path.dirname(os.path.abspath(__file__))

# Define the list of text pairs to search for and replace
replacements = [
    ('student_name_1', 'anonymized_name_1'),
    ('student_name_2', 'anonymized_name_2'),
    ('student_name_3', 'anonymized_name_3'),
    # Add more pairs as needed
]

# Loop through each folder and file in the parent directory
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            # Read the content of the HTML file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Replace each text pair in the content
            for find_text, replace_text in replacements:
                content = re.sub(find_text, replace_text, content)
                
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Updated: {file_path}")

print("Text replacement complete!")




