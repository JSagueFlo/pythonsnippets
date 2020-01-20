"""
Aquest script agafa totes les fotografies i videos del directori DIRECTORI
i els canvia el nom segons la data de creació en format:

              xxY-xxM-xxD_xxh-xxm-xxsUTC.ext
"""

# CONSTANTS
DIRECTORI = input("Entra el directori aboslut:\n")
DIRECTORI = DIRECTORI + "\\"
print(DIRECTORI)

import os
import re
from datetime import datetime
import time

timer_start = time.time()

def is_image(file_name):
    extensions = {".jpeg", ".jpg", ".png", ".gif", ".JPEG", ".JPG", ".PNG", ".GIF", ".mp4", ".MPG"}
    return any(file_name.endswith(ext) for ext in extensions)

def get_name(new_file_date):
    # Create the new filename (format: xxY-xxM-xxD_xxh-xxm-xxsUTC.ext)
    date, time = new_file_date.split(" ")
    date_items = date.split("-")
    date_items[0] = date_items[0] + "Y-"
    date_items[1] = date_items[1] + "M-"
    date_items[2] = date_items[2] + "D"
    date = "".join(date_items)
    time_items = time.split("-")
    time_items[0] = time_items[0] + "h-"
    time_items[1] = time_items[1] + "m-"
    time_items[2] = time_items[2][0:2] + "s"
    # És possible que arribi fins als microsegons xD
    # Així es creen alguns duplicats no destijats, pero el nom és un pel més curt
    time = "".join(time_items)
    new_file_name = date + "_" + time + "UTC"
    return new_file_name

file_counter = 0
image_counter = 0
images_parsed = 0

for file_name in os.listdir(DIRECTORI):
    file_counter += 1
    # Split filename and extension
    file_name, file_extension = os.path.splitext(file_name)
    # Check if the file is image, if so, go on
    if is_image(file_extension):
        image_counter += 1
        
        match=re.search(r'\d\dY-\d\dM-\d\dD_\d\dh-\d\dm-\d\dsUTC', file_name)
        if not match:
            # Get the full path of this file
            file_path = DIRECTORI + file_name + file_extension
            # Get the creation date of this file
            file_date = datetime.utcfromtimestamp(os.path.getmtime(file_path))
            # Convert the creation date to a string well formated
            new_file_date = str(file_date).replace(":", "-")
            new_file_name = get_name(new_file_date)
            new_file_path = DIRECTORI + new_file_name + file_extension
            
            # print()
            # print("File path:", file_path)
            # print("New path :", new_file_path)
            # print("Datetime: ", file_date)
            # print("Original :", file_name + file_extension)
            # print("New name :", new_file_name + file_extension)

            # Check if new name exists
            existing_names = 1
            while os.path.exists(new_file_path):
                new_file_name = new_file_name + "({})".format(existing_names)
                new_file_path = DIRECTORI + new_file_name + file_extension
                # print("New name :", new_file_name + file_extension)
                # print("New path :", new_file_path)
                existing_names += 1
            # Rename the file
            try:
                os.rename(file_path, new_file_path)
                images_parsed += 1
            except Exception as e:
                print("Error! {}".format(e))

print()
print("Directory: {}".format(DIRECTORI))
print("Files found: {}".format(file_counter))
print("Images found: {}".format(image_counter))
print("Images parsed: {}".format(images_parsed))
timer_end = time.time()
print("Executed in {} seconds".format(timer_end - timer_start))
print()
