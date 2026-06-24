'''firewall_log = "/Users/robscomputer/network_logs/firewall_log.txt"

blocked_count = 0

with open(firewall_log, "r") as file:
    log_data = file.read()
for line in file:
    if "BLOCKED" in line:
        # 2. Every time we find a match, increment our counter by 1
        blocked_count += 1

if "BLOCKED" in log_data:
    print(f"BLOCKED traffic found in log.\n"
          f"Count: {blocked_count}")
else:
    print("No BLOCKED traffic found in log.")'''

firewall_log = "/Users/robscomputer/network_logs/firewall_log.txt"

# 1. Initialize our counter variable at 0 BEFORE opening the file
blocked_count = 0

with open(firewall_log, "r") as file:
    for line in file:
        if "BLOCKED" in line:
            # 2. Every time we find a match, increment our counter by 1
            blocked_count += 1

            # (Optional) Keep printing the lines if you still want to see them
            print(f"🚨 SECURITY ALERT: {line.strip()}")

# 3. Print the final tally AFTER the loop and file closure are completely done
print("\n--- Log Scan Complete ---")
print(f"Total Blocked Events Found: {blocked_count}")
