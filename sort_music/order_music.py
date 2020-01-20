"""
Aquest script agafa totes les cançons del directori DIRECTORI

Si l'arxiu no és mp3 el converteix a mp3

Canvia el nom de la següent manera:
            Nom Artista - Nom Album - Nom Cançó.mp3

També esborra arxius no desitjats si els troba:
            desktop.ini
            fotos (.jpg, .png, .jpeg, .gif)
"""

# CONSTANTS
DIRECTORI = input("Entra el directori aboslut:\n")  # "F:\\Amaral"
DIRECTORI = DIRECTORI + "\\"

import os
import re
from datetime import datetime
import time

timer_start = time.time()

file_counter = 0
dir_counter = 0
songs_counter = 0
image_counter = 0
other_counter = 0
songs_parsed = 0
image_deleted = 0
other_deleted = 0


def is_song(file_name):
    extensions = {".mp3", ".3gp", ".m4a", ".ogg", ".wav", ".wma"
                  ".MP3", ".3GP", ".M4A", ".OGG", ".WAV", ".WMA"}
    return any(file_name.endswith(ext) for ext in extensions)


def is_image(file_name):
    extensions = {".jpeg", ".jpg", ".png", ".gif",
                  ".JPEG", ".JPG", ".PNG", ".GIF"}
    return any(file_name.endswith(ext) for ext in extensions)


def is_deletable(file_name):
    matches = {"desktop.ini", "Desktop.ini", "Thumbs.db"}
    return any(file_name == match for match in matches)


def parse_dir(path):
    global dir_counter
    global file_counter

    for file_name in os.listdir(path):
        full_path = path + file_name

        if os.path.isdir(full_path):
            full_path = full_path + "\\"
            dir_counter += 1
            print(f"\nDirectory found: {full_path}")
            parse_dir(full_path)

        if os.path.isfile(full_path):
            file_counter += 1
            parse_file(full_path)


def clean_string(string):
    string = string.replace(' ', '_')
    string = re.sub('_+', '_', string)  # Get rid of double spaces

    while (string.startswith('_') or string.startswith('-')):
        if string.startswith('_'):
            string = string.replace('_', '', 1)
        if string.startswith('-'):
            string = string.replace('-', '', 1)

    return string


def parse_file(full_path):
    global songs_counter
    global image_counter
    global other_counter
    global songs_parsed
    global image_deleted
    global other_deleted

    print(f"File found: {full_path}")
    path_split = full_path.split('\\')
    file = path_split[-1]
    dir_name = path_split[-2]

    if is_song(file):
        # TODO: print("is song!")  # WHY DOESNT DETECT .WMA???
        songs_counter += 1
        file_name, file_extension = os.path.splitext(file)

        # TODO: Si no es mp3, converteixlo a mp3

        dir_name = dir_name.lower()
        dir_name = clean_string(dir_name)

        file_name = file_name.lower()
        file_name = clean_string(file_name)
        # If the file already contains the name of the dir, remove it
        if file_name.startswith(dir_name):
            file_name = file_name.replace(dir_name, '', 1)
        file_name = clean_string(file_name)

        if len(file_name) == 0:
            print("ALERT ::: File name is void")

        # Busca si el nom de la canço conté _-_nomartista_-_
        if dir_name in file_name:
            # Note: might contain the name but it's well formated
            # match with: '' + dir_name + ''
            # Example: "Hammerfall - Hammerfall.mp3"
            # Order of ps matters (from more to less chars)
            possible_matches = ['_-_' + dir_name + '_-_',

                                '_-' + dir_name + '_-_',
                                '_-_' + dir_name + '-_',

                                '_-_' + dir_name + '_',
                                '_-' + dir_name + '-_',
                                '-' + dir_name + '_-_',
                                '_' + dir_name + '_-_',

                                '_-_' + dir_name + '',
                                '_-' + dir_name + '_',
                                '-' + dir_name + '-_',
                                '_' + dir_name + '-_',
                                '' + dir_name + '_-_',

                                '_-' + dir_name + '',
                                '-' + dir_name + '_',
                                '_' + dir_name + '_',
                                '' + dir_name + '-_',

                                '-' + dir_name + '',
                                '_' + dir_name + '',

                                '' + dir_name + '_']
            for ps in possible_matches:
                if ps in file_name:
                    file_name = file_name.replace(ps, '')  # replaces all match
                    print("replaced")
        print("Current file name:", file_name)

        final_name = dir_name + "_-_" + file_name + file_extension
        final_name = final_name.replace("_", " ")
        final_name = final_name.title()

        path_split[-1] = final_name

        final_path = "\\".join(path_split)
        print(f"Final name: {final_name}")

        print(f"Full path was: {full_path}")
        print(f"Final path is: {final_path}\n")

        # Rename the file
        try:
            os.rename(full_path, final_path)
            songs_parsed += 1
        except Exception as e:
            print("Error! {}".format(e))

    if is_image(file):
        image_counter += 1
        try:
            os.remove(full_path)
            image_deleted += 1
        except Exception as e:
            print(f"\n{e}\n")

    if is_deletable(file):
        other_counter += 1
        try:
            os.remove(full_path)
            other_deleted += 1
        except Exception as e:
            print(f"\n{e}\n")

parse_dir(DIRECTORI)

# file_counter += 1
# # Split filename and extension
# file_name, file_extension = os.path.splitext(file_name)
# # Check if the file is image, if so, go on
# if is_image(file_extension):
#     image_counter += 1

#     match = re.search(r'\d\dY-\d\dM-\d\dD_\d\dh-\d\dm-\d\dsUTC', file_name)
#     if not match:
#         # Get the full path of this file
#         file_path = DIRECTORI + file_name + file_extension
#         # Get the creation date of this file
#         file_date = datetime.utcfromtimestamp(os.path.getmtime(file_path))
#         # Convert the creation date to a string well formated
#         new_file_date = str(file_date).replace(":", "-")
#         new_file_name = get_name(new_file_date)
#         new_file_path = DIRECTORI + new_file_name + file_extension

#         # print()
#         # print("File path:", file_path)
#         # print("New path :", new_file_path)
#         # print("Datetime: ", file_date)
#         # print("Original :", file_name + file_extension)
#         # print("New name :", new_file_name + file_extension)

#         # Check if new name exists
#         existing_names = 1
#         while os.path.exists(new_file_path):
#             new_file_name = new_file_name + "({})".format(existing_names)
#             new_file_path = DIRECTORI + new_file_name + file_extension
#             # print("New name :", new_file_name + file_extension)
#             # print("New path :", new_file_path)
#             existing_names += 1
#         # Rename the file
#         try:
#             os.rename(file_path, new_file_path)
#             images_parsed += 1
#         except Exception as e:
#             print("Error! {}".format(e))


print()
print(f"Directory: {DIRECTORI}")
print(f"Items found: {file_counter}")
print(f"Directories found: {dir_counter}")
print(f"Songs found: {songs_counter}")
print(f"Images found: {image_counter}")
print(f"Other found: {other_counter}")
print(f"Songs parsed: {songs_parsed}")
print(f"Images deleted: {image_deleted}")
print(f"Other files deleted: {other_deleted}")
timer_end = time.time()
print("Executed in {} seconds".format(timer_end - timer_start))
print()
