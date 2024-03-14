import os


directories = ["harvest/logo", "know_base"]
for directory in directories:
    os.makedirs(directory, exist_ok=True)
