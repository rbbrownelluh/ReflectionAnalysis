import os
import re
from collections import defaultdict
from bs4 import BeautifulSoup

# Define the base directory where the folders are located
base_directory = "."
output_directory = os.path.dirname(os.path.abspath(__file__))

# Dictionary to group files by H1 number
html_files_by_number = defaultdict(list)

# Iterate through all the subdirectories in the base directory
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            html_files_by_number[file_path] = file_path

# Function to extract order based on folder name and H1 tag
def get_reflection_order(file_path):
    # Extract the folder name to determine the day
    folder_name = os.path.basename(os.path.dirname(file_path))
    
    # Assign a priority based on the folder name
    match = re.search(r'Day_(\d+)', folder_name, re.IGNORECASE)
    if match:
        return int(match.group(1))

    # Default order if folder name does not match expected pattern
    return float('inf')

# Function to extract headings and their following divs, modifying headings as needed
def extract_headings_and_divs(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove all <style> and <script> elements
    for tag in soup.find_all(["style", "script"]):
        tag.decompose()

    # Convert lower-level headings to <strong>
    for heading in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
        strong_tag = soup.new_tag("strong")
        strong_tag.string = heading.get_text(strip=True)
        heading.replace_with(strong_tag)

    extracted_content = ""
    h1_number = None

    # Extract all <h1> headings and their following divs
    for heading in soup.find_all("h1"):
        # Strip attributes from the <h1> tag
        heading.attrs = {}
        extracted_content += str(heading) + "\n"

        # Extract the number from the <h1> text
        match = re.search(r":\s*(\d+)$", heading.get_text(strip=True))
        if match:
            h1_number = match.group(1)

        # Find the next div sibling and process it
        sibling = heading.find_next_sibling()
        while sibling and sibling.name != "div":
            sibling = sibling.find_next_sibling()
        if sibling and sibling.name == "div":
            # Remove attributes from the div and its children but keep the structure
            sibling.attrs = {}
            for tag in sibling.find_all(True):
                tag.attrs = {}
            extracted_content += str(sibling) + "\n"

    return extracted_content, h1_number

# Dictionary to group content by extracted H1 number
grouped_content = defaultdict(str)

# Process files and group by H1 number
for file_path in html_files_by_number.keys():
    with open(file_path, "r") as f:
        html_content = f.read()
        headings_and_divs, h1_number = extract_headings_and_divs(html_content)
        if h1_number:
            grouped_content[h1_number] += headings_and_divs

# Write each group of reflections into a separate file
for h1_number, content in grouped_content.items():
    output_file = os.path.join(output_directory, f"combined_{h1_number}_reflections.html")
    with open(output_file, "w") as output:
        output.write(content)
    print(f"Combined HTML files saved to {output_file}")
