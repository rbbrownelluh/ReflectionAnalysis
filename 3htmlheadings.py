import os
from bs4 import BeautifulSoup

def edit_html_file(file_path):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract the number from the first <h1>
    first_h1 = soup.find('h1')
    if not first_h1:
        print(f"No <h1> tag found in {file_path}.")
        return

    number = None
    for part in first_h1.text.split():
        if part.isdigit():
            number = part
            break

    if not number:
        print(f"No number found in the first <h1> tag of {file_path}.")
        return

    # Create the new <h1>
    new_h1 = soup.new_tag('h1')
    new_h1.string = f"{number}'s Reflections"

    # Insert the new <h1> at the beginning of the document
    soup.insert(0, new_h1)

    # Convert all existing <h1> tags (except the new one) to <h2>, keeping their content and placement
    existing_h1s = soup.find_all('h1')[1:]  # Skip the newly added h1
    for h1 in existing_h1s:
        h2 = soup.new_tag('h2')
        h2.string = h1.string
        h1.replace_with(h2)

    # Write the modified HTML back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Edited {file_path} successfully.")

# Script to edit all HTML files in the current folder
if __name__ == "__main__":
    folder_path = os.getcwd()
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            edit_html_file(file_path)
