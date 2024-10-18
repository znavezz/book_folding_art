import csv
import re
import os
import sys

# Input file path given as command line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = os.path.join(os.path.dirname(input_file_path), 'Reversed_Page_Numbers_Book_Folding_Pattern.csv')

# Read the content of the input file and extract data lines
lines = []
first_page = None
try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Extract lines with valid page numbers
            match = re.match(r'\s*(\d+)', line)
            if match:
                if first_page is None:
                    first_page = int(match.group(1))
                lines.append(line.strip())
    print(f"Successfully read from input file: {input_file_path}")
except FileNotFoundError:
    print(f"Error: File not found - {input_file_path}")
    sys.exit(1)
except Exception as e:
    print(f"Error reading input file: {e}")
    sys.exit(1)

# Determine the maximum page number
try:
    max_page_number = max(int(re.split(r'\s+', line, maxsplit=3)[0]) for line in lines if re.match(r'\s*\d+', line))
except ValueError:
    print("Error: No valid page numbers found in the input file.")
    sys.exit(1)

# Reverse the page numbers
reversed_lines = []
try:
    for line in lines:
        parts = re.split(r'\s+', line, maxsplit=3)
        if len(parts) >= 1 and parts[0].isdigit():
            # Reverse the page number while keeping the rest of the line the same
            parts[0] = str(max_page_number - int(parts[0]) + first_page)  # Reverse dynamically based on the max page number
        reversed_lines.append(parts)
    print("Successfully reversed page numbers.")
except Exception as e:
    print(f"Error reversing page numbers: {e}")
    sys.exit(1)

# Write the output to a CSV file
try:
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Page", "Top Fold", "Bottom Fold"])
        for parts in reversed_lines:
            csv_writer.writerow(parts + ["" for _ in range(3 - len(parts))])
    print(f"Successfully wrote output to CSV file: {output_file_path}")
except Exception as e:
    print(f"Error writing to output CSV file: {e}")
    sys.exit(1)