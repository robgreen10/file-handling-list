active_leads = ["Boise Roofing", "Apex Builders", "Summit Teams"]


def process_lead(leads_list):

    removed_lead = leads_list.pop(0)

    print(f"Status message: removed lead {removed_lead}")


print(f"Before: {active_leads}")
process_lead(active_leads)

print(f"After: {active_leads}")
