import os
import re
from bs4 import BeautifulSoup

# Define the base directory where the folders are located
base_directory = "."
output_directory = os.path.dirname(os.path.abspath(__file__))

# Dictionary to hold the list of HTML files
html_files = {}

# Iterate through all the subdirectories in the base directory
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)

            if file not in html_files:
                html_files[file] = []

            html_files[file].append(file_path)

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

# Function to retain all headings and their following divs, modifying headings as needed
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
    h1_numbers = []

    # Extract all <h1> headings and their following divs
    for heading in soup.find_all("h1"):
        # Strip attributes from the <h1> tag
        heading.attrs = {}
        extracted_content += str(heading) + "\n"

        # Extract the number from the <h1> text
        match = re.search(r":\s*(\d+)$", heading.get_text(strip=True))
        if match:
            h1_numbers.append(match.group(1))

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

    return extracted_content, h1_numbers

# Iterate over all the HTML files with the same name
for filename, file_list in html_files.items():
    # Sort the files by the reflection number extracted from the folder name
    file_list_sorted = sorted(file_list, key=lambda x: get_reflection_order(x))

    combined_content = ""
    all_numbers = []

    for file_path in file_list_sorted:
        with open(file_path, "r") as f:
            html_content = f.read()
            headings_and_divs, h1_numbers = extract_headings_and_divs(html_content)
            combined_content += headings_and_divs
            all_numbers.extend(h1_numbers)

    # Use the first number for the filename, if available
    file_number = all_numbers[0] if all_numbers else "unknown"

    # Define the output file path using the extracted number
    output_file = os.path.join(output_directory, f"combined_{file_number}_reflections.html")

    # Write the processed content to the output file
    with open(output_file, "w") as output:
        output.write(combined_content)

    print(f"Combined HTML files saved to {output_file}")
