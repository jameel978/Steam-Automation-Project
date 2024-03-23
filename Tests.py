from bs4 import BeautifulSoup
import os
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

def merge_html_reports(input_files, output_file):
    # Read the content of the first HTML file and extract the specific section
    with open(input_files[0], 'r', encoding='utf-8') as f:
        first_html_content = f.read()
        first_soup = BeautifulSoup(first_html_content, 'html.parser')
        specific_section = first_soup.find('tr', id='et1.1')

    # Copy the HTML content of the first file to create a template
    template_soup = BeautifulSoup(first_html_content, 'html.parser')

    # Remove the specific section from the template
    if specific_section:
        specific_section.decompose()

    # Iterate through the remaining HTML files
    for file in input_files[1:]:
        # Read the content of the current HTML file and extract the specific section
        with open(file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            specific_section = soup.find('tr', id='et1.1')
            if specific_section:
                # Append the specific section to the template
                template_soup.body.append(specific_section)

    # Write the merged HTML report to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(template_soup))

def get_files_in_directory(directory):
    # Initialize an empty list to store file paths
    file_paths = []

    # Iterate over all the files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full path of the file
            file_path = os.path.join(root, file)
            # Add the full path to the list
            file_paths.append(file_path)

    return file_paths

# Example usage:
input_files = get_files_in_directory("Reports")
output_file = 'merged_report.html'  # Output file name for the merged HTML report

print(input_files)
merge_html_reports(input_files, output_file)
