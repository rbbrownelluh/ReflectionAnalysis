import os

# Define the folder where the script and HTML files are located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Initialize an empty string to hold the combined HTML content
combined_content = ""

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
            combined_content += file.read() + "\n"

# Step 2: Adjust headers
# Convert <h2> to <h3> first
adjusted_content = combined_content.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
# Then convert <h1> to <h2>
adjusted_content = adjusted_content.replace("<h1>", "<h2>").replace("</h1>", "</h2>")

# Step 3: Add the new <h1> at the top
final_content = "<h1>All Student Reflections</h1>\n" + adjusted_content

# Step 4: Write the final content to a new file
output_file = os.path.join(folder_path, "combined_reflections.html")
with open(output_file, "w", encoding="utf-8") as output:
    output.write(final_content)

print(f"Combined file created: {output_file}")