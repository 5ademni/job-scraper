import json

# Load the JSON file
with open('harvest/jobs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open the output text file with 'utf-8' encoding
with open('know_base/job_offers.txt', 'w', encoding='utf-8') as f:
    # Iterate over each job
    for url, jobs in data.items():
        for job in jobs:
            # Write the job data to the text file
            f.write(f"Title: {job['title']}\n")
            f.write(f"Company: {job['company']}\n")
            f.write(f"Location: {job['location']}\n")
            f.write(f"Link: {job['link']}\n")
            f.write(f"Company Logo: {job['company_logo']}\n")
            f.write("\n")
