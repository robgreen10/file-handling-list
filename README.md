# Auth Log Parser

## Summary
This Python script automates the scanning of local auth log files to identify potential security incidents. It searches line-by-line for specific threat signatures, handles mixed text casing seamlessly, and prints the exact line location of every match. The script concludes by generating a summary report displaying the total number of security events detected.

First Block of Code:

Safely opens the log file in read-only mode and automatically closes it when finished. It uses enumerate to track ascending line numbers starting at 1 while simultaneously stripping whitespace from each raw log entry.

Second For Loop

Loops through every target phrase for each log line, converting both strings to uppercase to ensure a case-insensitive match. If a phrase is found, it increments the alert counter, prints the line details, and breaks early to prevent duplicate alerts for the same line.

Ending:

Executes exactly once at the very end of the script execution after the file stream closes. It prints a clean visual header followed by the aggregated final count of all security events intercepted.
