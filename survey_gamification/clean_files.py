import os

# Define the range of numbered folders
folder_range = range(11, 25)  # 11 to 24 inclusive

# Define the main folders and subfolders to check
main_folders = ['pre', 'post']
sub_folders_to_check = ['baseline', 'cognitive_load', 'survey']

# Define the files to keep for each sub-folder
files_to_keep = {
    'baseline': ['muse_eeg.csv'],
    'cognitive_load': ['muse_eeg.csv', 'stroop_responses.csv'],
    'survey': ['muse_eeg.csv', 'questionnaires.csv', 'responses.csv']
}

# Iterate over each numbered folder
for folder_number in folder_range:
    parent_folder = str(folder_number)
    
    # Check if the parent folder exists
    if not os.path.isdir(parent_folder):
        print(f"Folder {parent_folder} does not exist. Skipping.")
        continue
    
    # Iterate over the 'pre' and 'post' main folders
    for main_folder in main_folders:
        main_folder_path = os.path.join(parent_folder, main_folder)
        
        # Check if the main folder exists
        if not os.path.isdir(main_folder_path):
            print(f"Main folder {main_folder_path} does not exist. Skipping.")
            continue
        
        # Iterate over each sub-folder (baseline, cognitive_load, survey)
        for sub_folder in sub_folders_to_check:
            sub_folder_path = os.path.join(main_folder_path, sub_folder)
            
            # Check if the sub-folder exists
            if not os.path.isdir(sub_folder_path):
                print(f"Sub-folder {sub_folder_path} does not exist. Skipping.")
                continue
            
            # Get a list of files in the sub-folder
            files_in_sub_folder = os.listdir(sub_folder_path)
            
            # Delete files that are not in the list of files to keep
            for file_name in files_in_sub_folder:
                if file_name not in files_to_keep[sub_folder]:
                    file_path = os.path.join(sub_folder_path, file_name)
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete {file_path}: {e}")
