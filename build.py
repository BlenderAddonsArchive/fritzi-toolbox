import os
import shutil

##### CONFIG VARIABLES START ######

# Destination path of addon build. For Windows filesystems be sure to use forward slashes, as backslashes may break the file path.
# Make sure the destination folder does NOT exist before running the script.
destination_path = 'C:/Users/Anwender/Desktop/'

# Version number of addon. NO trailing dot at the end. Should match bl_info in __init__.py
version_number = '0.0.0'

# Automatically pack into .zip archive. Needed for installing the addon in Blender.
pack_to_zip = True

# If true unpacked files will be removed so that only the zip archive is left in the destination folder
remove_unpacked_files_after_zip = True

##### CONFIG VARIABLES END ######




# do not build files that match following patterns, to exclude development files that the end user does not need
IGNORE_PATTERNS = ('*.pyc', 'tmp*', '*__pycache__*', '.git', '.vscode', '.gitignore', '.gitattributes', 'build.py', 'fritzi-toolbox_updater')


# Add root folder to path
if destination_path[-1] in ['/', '\\']:
    destination_path += "fritzi-toolbox-" + version_number + "/"
else:
    destination_path += "/fritzi-toolbox/" + version_number + "/"

zip_path = destination_path



# Add second layer folder (required for blender addon installation process)
if destination_path[-1] in ['/', '\\']:
    destination_path += "fritzi-toolbox/"
else:
    destination_path += "/fritzi-toolbox/"



dir_path = os.path.dirname(os.path.realpath(__file__))
shutil.copytree(dir_path, destination_path, ignore=shutil.ignore_patterns(*IGNORE_PATTERNS))

if pack_to_zip:
    shutil.make_archive(zip_path, "zip", zip_path)

    if remove_unpacked_files_after_zip:
        shutil.rmtree(zip_path)

print("Build script done.")
