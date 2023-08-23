import re
from collections import Counter


def analyze_logs(log_file_path):
    error_count = 0
    warning_count = 0
    unique_errors = Counter()

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if re.search(r'ERROR', line, re.IGNORECASE):
                error_count += 1
                error_message = re.search(r'ERROR: (.+)', line).group(1)
                unique_errors[error_message] += 1
            elif re.search(r'WARNING', line, re.IGNORECASE):
                warning_count += 1

    return error_count, warning_count, unique_errors


def generate_report(error_count, warning_count, unique_errors):
    print("Log Analysis Report:")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}\n")

    print("Unique Errors:")
    for error, count in unique_errors.items():
        print(f"{error} - Occurrences: {count}")


if __name__ == "_main_":
    log_file_path = '/path/to/your/logfile.log'
    errors, warnings, unique_errors = analyze_logs(log_file_path)
    generate_report(errors, warnings, unique_errors)
