import shutil, mimetypes
from pathlib import Path

def main():
    while True:
        print("\nChoose an option:")
        print("1. Organize by specific file type")
        print("2. Organize entire folder by file types")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            organize_specific_file_type()
        elif choice == "2":
            organize_entire_folder()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def query_user_for_folder():
    '''
    queries user for a valid file path and only continues when a valid path is provided.

    Return: 
        a path object containing the path to the folder
    '''   

    while True:
        input_folder = input("provide the path to the folder you would like to organize: ").strip()
        folder_path = Path(input_folder)

        if folder_path.exists() and folder_path.is_dir():
            return folder_path
        print('Could not find folder. Please try again.')


def move_file(file, destination_folder):
    '''
        attempts to move a file to a destination folder and throws an exception when unsuccessful.

        Params:
            file - the file you wish to move
            destination_folder - the folder you wish to move the file to

        Return:
            True - if the move was successful
            False - if the move was not successful
    '''
    try:
        shutil.move(str(file), destination_folder / file.name)
        print(f"Moved: {file} -> {destination_folder}")
        return True
    
    except Exception as e:
        print(f"Failed to move: {file}. Error: {e}")
        return False


def query_user_for_file_type():
    '''
        queries user for a valid file type and only continues when a valid file type is provided.

        Return: 
            a string containing the file type.
    '''
    while True:
        input_file_type = str(input("provide file type to be organized (ex: txt, pdf, ...): ")).strip().lower()

        if input_file_type.isalnum():
            return input_file_type
        
        print('Invalid file type. Try again.')

def mime_to_label(file_extension):
    '''
        maps a mime response to a simplified version of the file extension given.
    '''
    dictionary = {
        'vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
        'x-python': 'py',
        'x-zip-compressed': 'zip',
        'plain': 'txt',
        'msword': 'doc',
        'vms-excel': 'xsl',
        'vopenxmlformats-officedocument.spreadsheetml.sheet': 'xlsx',
        'vms-powerpoint': 'ppt',
        'openxmlformats-officedocument.presentationml.presentation': 'pptx'
    }

    if file_extension in dictionary:
        return dictionary.get(file_extension)
    else:
        return file_extension
            

def organize_entire_folder():
    '''
        organizes an entire folder by detecting the types of the files inside the folder and creating files for each of those types of file.
    '''
    # creates a path object containing the path to the folder that will be organized
    folder_path = query_user_for_folder()

    # defines the constants such as the files in the folder and the amount of files.
    all_files = [file for file in folder_path.glob('*') if not file.name.startswith('.')]
    files_length = len(all_files)
    successful_files_moved = 0

    if files_length == 0:
        print("No files found in this folder.")
    else:
        for index, file in enumerate(all_files, start=1):
            if file.is_file():
                # attempts to classify every file by its type
                file_type, _ = mimetypes.guess_type(file)
                if file_type:
                    file_type = mime_to_label(file_type.split('/')[-1])  
                    sanitized_type = file_type.lower()  
                else:
                    sanitized_type = 'unknown'

                # finds or creates a destination folder for the file to be moved to.
                destination_folder = folder_path / f"{sanitized_type}_files"
                destination_folder.mkdir(exist_ok=True)

                print(f"[{index}/{files_length}] Moving: {file.name}")
                if move_file(file, destination_folder):
                    successful_files_moved += 1

                

    print(f'\n\n Organization Complete! Successfully moved {successful_files_moved} / {files_length} files.')


def organize_specific_file_type():
    '''
        organizes the files with a specified type within a folder.
    '''
    # prompt the user for a file type and path to folder.
    input_file_type = query_user_for_file_type()
    source_folder = query_user_for_folder()

    # populate a list with the files of specified type
    files = list(source_folder.glob(f"*.{input_file_type}"))
    files_length = len(files)

    if files_length == 0:
        print(f"No files found with type: {input_file_type}")
    else: 
        # find a directory associated with the specific file type or create one if not found.
        destination_folder = source_folder / f'{input_file_type}_files'
        destination_folder.mkdir(exist_ok=True)

        # move the files and update the user on process
        successfully_moved_file_count = 0
        for index, file in enumerate(files, start=1):
            print(f"[{index}/{files_length}] Moving: {file.name}")
            if move_file(file, destination_folder):
                successfully_moved_file_count += 1


        print(f'\n\n Organization Complete! Successfully moved {successfully_moved_file_count} / {files_length} files.')


if __name__ == '__main__':
    main()