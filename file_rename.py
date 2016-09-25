# ----------------
# Script to rename all files in directory
# Useful for getting rid of annoying keywords from torrent downloads.
# Example:
#   [AliQ] Steven Universe S03E01 Super Watermelon Island [1080p;WEB-DL x264]
#
#   1. Run this script
#   2. Specify full path: D:\TV Shows\Steven Universe\Season 3
#   3. File Extension: mp4
#   4. Keywords to delete: [AliQ]
#                          [1080p;WEB-DL x264]
#                          done
#   Voila
#------------------

import os

# Done string
done_str = "done"

# Get the directory to search
file_dir = raw_input("Enter the directory path (c/p path): ")

# Get file extension to look for
file_ext = raw_input("File Extension: ")
if not file_ext.startswith("."):
    file_ext = "." + file_ext

# List to store keywords to look for
search_list = []

# Get the list of keywords to search
while True:

    search_str = raw_input("Keyword to search (enter 'done' when finished): ")
    if search_str == done_str:
        break;

    search_list.append(search_str)

# Go through each file that ends with the matching file extension
for filename in os.listdir(file_dir):
    if filename.endswith(file_ext):

        # Capture the filename without extension
        new_filename = filename.replace(file_ext, '')

        # Iterate through the list and search for keyword
        for keyword in search_list:
            # Remove keyword
            new_filename = new_filename.replace(keyword, '')

        # Strip left and right whitespace
        new_filename = new_filename.lstrip()
        new_filename = new_filename.rstrip()

        # Add back the file extension
        new_filename = new_filename + file_ext

        # Finally rename the file
        os.rename( os.path.join(file_dir, filename), os.path.join(file_dir, new_filename) )
