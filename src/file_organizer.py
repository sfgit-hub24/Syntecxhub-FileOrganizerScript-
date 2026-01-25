import os
import shutil
import logging
#---------------------------------------------------------------
# Configuration
#---------------------------------------------------------------
dry_run = False
# dry_run=True, PREVIEW & dry_run=False, MOVE FILES
folder_path = r"C:\Users\HABEE\OneDrive\Documents\Test_Cleanup"
log_file = r"C:\Users\HABEE\OneDrive\Documents\File_Movement.log" # Log file OUTSIDE the folder being organized
#---------------------------------------------------------------
# Logging Setup
logging.basicConfig(
    filename=log_file,
    level = logging.INFO,
    format = "%(asctime)s - %(message)s", # Format of Message in Log
    force = True
    )
logging.info("This is my first log entry")
#---------------------------------------------------------------
# Main Code
#---------------------------------------------------------------
for file in os.listdir(folder_path):
    source_path = os.path.join(folder_path, file)
    if os.path.isfile(source_path): # Process files alone, skip folders
        if file == os.path.basename(__file__): # Log & Script Files are IGNORED to avoid Errors
            continue
        name,extension = os.path.splitext(file) # Skip files without an extension
        if extension == "":
            continue
        folder_name = extension[1:].upper()# Folder extensions(TXT, JPG, PDF, MP3)
        destination_folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(destination_folder): # To create a Folder if doesn't exist
            if dry_run:
                print(f"[dry_run] Would create folder '{folder_name}'")
            else:
                os.mkdir(destination_folder)
        destination_path = os.path.join(destination_folder, file)
        c=1 # Counter, to handle naming collisions
        while os.path.exists(destination_path):
            new_name = f"{name}_{c}{extension}"
            destination_path = os.path.join(destination_folder, new_name)
            c+=1
        if dry_run: # Move or DRY RUN
            print(f"[dry_run] Would move '{file}' -> '{folder_name}/'")
        else:
            shutil.move(source_path, destination_path)
            logging.info(f"Moved '{file}' -> '{folder_name}/'")
            logging.getLogger().handlers[0].flush() # Force log write immediately
            print("Logged test entry successfully.")
            print(f"Moved '{file}' -> '{folder_name}/'") # Force immediate write
# -------------------------------------------------------------
# Moving Script File itself into PY FOLDER
# -------------------------------------------------------------
if not dry_run:
    script_path = os.path.realpath(__file__)
    script_folder = os.path.join(folder_path, "PY")
    if not os.path.exists(script_folder):
        os.mkdir(script_folder)
    shutil.move(script_path, os.path.join(script_folder, os.path.basename(script_path)))
# -------------------------------------------------------------
# Move Log File itself to LOG FOLDER
# -------------------------------------------------------------
if not dry_run:
    for handler in logging.getLogger().handlers: # Close Logging to Release File Handle
        handler.close()
        logging.getLogger().removeHandler(handler)
    log_folder = os.path.join(folder_path, "LOG") # To Create LOG Folder
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    shutil.move(log_file, os.path.join(log_folder, os.path.basename(log_file)))
#--------------------------------------------------------------
# Finish Message
print("\nSCRIPT FINISHED!")
#--------------------------------------------------------------
if dry_run: # If dry_run=True
    print("Dry run complete. Set DRY_RUN = False to actually move files.")
else:
    print(f"All moved files are logged in: {os.path.join(log_folder, os.path.basename(log_file))}")
