import os
import json


import os
import json


def json2txt():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Create a file path relative to the script's location
    rootDir = os.path.join(script_dir, 'harvest/know_base/json/')

    # Initialize a set to store unique job links
    unique_jobs = set()

    # Create a file path for the output txt file
    txt_file_path = os.path.join(
        script_dir, 'harvest/know_base/txt/job_list.txt')

    with open(txt_file_path, 'w', encoding='utf-8') as f:
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname.endswith('.json'):
                    with open(os.path.join(dirName, fname), 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)

                    for url, jobs in data.items():
                        for job in jobs:
                            # Check if the job link is already in the set of unique job links
                            if job['link'] not in unique_jobs:
                                # Add the job link to the set of unique job links
                                unique_jobs.add(job['link'])

                                # Write the job data to the txt file
                                f.write(f"Title: {job['title']}\n")
                                f.write(f"Company: {job['company']}\n")
                                f.write(f"Location: {job['location']}\n")
                                f.write(f"Link: {job['link']}\n")
                                f.write(
                                    f"Company Logo: {job['company_logo']}\n")
                                f.write("\n")


if __name__ == "__main__":
    json2txt()
