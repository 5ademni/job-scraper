import os


directories = [
    "harvest/know_base/json", "harvest/know_base/txt"]
for directory in directories:
    os.makedirs(directory, exist_ok=True)
