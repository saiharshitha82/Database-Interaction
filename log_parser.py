import re
import csv
from collections import Counter

def parse_log_file(log_file_path):
    # Counter to keep track of the occurrences of each unique error or warning message
    error_count = Counter()

    # Open and read the log file
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Check if the line contains "ERROR" or "WARNING" (case-insensitive)
                if re.search(r"ERROR|WARNING", line, re.IGNORECASE):
                    # Extract the message after "ERROR" or "WARNING" (case-insensitive and flexible format)
                    message = re.search(r"(ERROR|WARNING)[:\]\s-]+(.*)", line, re.IGNORECASE)
                    if message:
                        error_message = message.group(2).strip()  # Extract the error/warning message
                        error_count[error_message] += 1  # Count occurrences of each message
                        print(f"Matched line: {line.strip()}")  # Debug print for verification

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
        return error_count

    return error_count

def write_to_csv(error_count, output_csv_path):
    # Write the results to a CSV file
    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["Error Message", "Count"])
        # Write each error message and its count
        for error_message, count in error_count.items():
            writer.writerow([error_message, count])

def main():
    # Define the path to the log file and the output CSV file
    log_file_path = "server_logs.txt" 
    output_csv_path = "error_report.csv"

    # Parse the log file and get the error counts
    error_count = parse_log_file(log_file_path)

    # Check if any errors/warnings were found
    if not error_count:
        print("No errors or warnings found in the log file.")
    else:
        # Write the error count to the CSV file
        write_to_csv(error_count, output_csv_path)
        print(f"Error report generated successfully in '{output_csv_path}'.")

if __name__ == "__main__":
    main()
