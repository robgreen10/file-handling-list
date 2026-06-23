def retrieve_knowledge_base(search_query, database_records):
    db_record = database_records.copy()
    db_record.pop(0)

    matched_context = []

    for log in db_record:
        if search_query in log:
            matched_context.append(log)
    return matched_context


def generate_llm_prompt(user_question, *retrieved_context, **model_settings):
    print(f"{user_question}:\n")

    for c in retrieved_context:
        print(f"{c}")

    for model, settings in model_settings.items():
        print(f"{model} {settings}")


# Master knowledge base archive (Global space)
master_security_logs = [
    "SYSTEM_PLACEHOLDER_LOG_DO_NOT_USE",
    "CRITICAL: Unauthorized SSH login attempt detected on Server-B.",
    "INFO: Standard database backup completed successfully.",
    "WARNING: Unauthorized API call flagged on endpoint /v1/auth.",
    "INFO: Firewall rules updated for cluster-3."
]

print("--- STEP 1: RUNNING RETRIEVAL ---")
# 1. Run the retrieval function and capture its returned list in a variable
extracted_context = retrieve_knowledge_base(
    "Unauthorized", master_security_logs)


print("\n--- STEP 2: GENERATING AUGMENTED PROMPT ---")
# 2. Pass the extracted context data directly into the prompt generator using unpacking (*)
generate_llm_prompt(
    "Analyze these security threats immediately",
    *extracted_context,
    security_clearance="Level-3",
    llm_router="Clara-v2"
)

# Global Safety Verification Check
print(
    f"\n[GLOBAL REPORT] Master Logs Integrity Check:\n {master_security_logs}")
