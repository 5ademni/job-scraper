import os
import json


def json2txt():
    # Define the directory you want to start from
    rootDir = 'harvest/know_base/json/'

    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname.endswith('.json'):
                with open(os.path.join(dirName, fname), 'r', encoding='utf-8') as f:
                    data = json.load(f)

                with open(f'harvest/know_base/txt/{os.path.splitext(fname)[0]}.txt', 'w', encoding='utf-8') as f:
                    for url, jobs in data.items():
                        for job in jobs:
                            f.write(f"Title: {job['title']}\n")
                            f.write(f"Company: {job['company']}\n")
                            f.write(f"Location: {job['location']}\n")
                            f.write(f"Link: {job['link']}\n")
                            f.write(f"Company Logo: {job['company_logo']}\n")
                            f.write("\n")
