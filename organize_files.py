import os
import shutil
from datetime import datetime

def get_creation_and_modification_time(file_path):
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    return creation_time, modification_time

def rename_and_move_file(file_path, destination_folder):
    creation_time, modification_time = get_creation_and_modification_time(file_path)
    
    # Convert timestamps to datetime objects
    creation_datetime = datetime.fromtimestamp(creation_time)
    modification_datetime = datetime.fromtimestamp(modification_time)
    
    # Determine the earliest timestamp
    earliest_datetime = min(creation_datetime, modification_datetime)
    
    # Format the datetime string
    formatted_datetime = earliest_datetime.strftime('%Y%m%d_%H%M%S')
    
    # Extract the filename and extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    
    # Construct the new filename
    new_file_name = f"{formatted_datetime}_{file_name}{file_extension}"
    
    # Create year and month folders if they don't exist
    year_folder = os.path.join(destination_folder, str(earliest_datetime.year))
    month_folder = os.path.join(year_folder, earliest_datetime.strftime('%m'))
    os.makedirs(month_folder, exist_ok=True)
    
    # Move the file to the month folder with the new name
    new_file_path = os.path.join(month_folder, new_file_name)
    shutil.move(file_path, new_file_path)
    
    print(f"Moved '{file_path}' to '{new_file_path}'")

def process_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            rename_and_move_file(file_path, directory)

if __name__ == "__main__":
    directory_path = "YOUR_DIRECTORY"
    process_files_in_directory(directory_path)
