new_file = "/Users/robscomputer/network_logs/auth_log.txt"

phrases = ["UNAUTHORIZED", "warning", "critical"]

keyword_found = 0

with open(new_file, "r") as log:
    for line_number, line in enumerate(log, start=1):
        clean_line = line.strip()

        for phrase in phrases:
            if phrase.upper() in clean_line.upper():
                keyword_found += 1

                print(f"Line {line_number}: {line.strip()}")

                break

print("\n------KEYWORD REPORT-------\n")
# print(f"Line {line_number}: {line.strip()}")
print(f"Total occurences of target keywords: {keyword_found}")
