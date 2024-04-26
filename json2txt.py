import os
import json


def json2txt():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Create a file path relative to the script's location
    rootDir = os.path.join(script_dir, 'harvest/know_base/json/')

    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname.endswith('.json'):
                with open(os.path.join(dirName, fname), 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Create a file path relative to the script's location
                txt_file_path = os.path.join(
                    script_dir, f'harvest/know_base/txt/{os.path.splitext(fname)[0]}.txt')
                with open(txt_file_path, 'w', encoding='utf-8') as f:
                    for url, jobs in data.items():
                        for job in jobs:
                            f.write(f"Title: {job['title']}\n")
                            f.write(f"Company: {job['company']}\n")
                            f.write(f"Location: {job['location']}\n")
                            f.write(f"Link: {job['link']}\n")
                            f.write(f"Company Logo: {job['company_logo']}\n")
                            f.write("\n")
