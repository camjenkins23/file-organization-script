# File Organizer Script

## Overview
The File Organizer Script is a Python program designed to automate file management. It organizes files in a specified folder by categorizing them into subfolders based on their file types or user-specified criteria. This tool simplifies folder organization, making it ideal for managing cluttered directories.

## Features
- **Organize Entire Folder:** Automatically detect file types and organize all files into categorized subfolders.
- **Organize Specific File Types:** Select and organize only specific file types into dedicated subfolders.
- **Custom Mappings:** Includes support for common file types (e.g., .pdf, .txt, .docx, .py) and allows for fallback categorization.
- **Interactive Command-Line Interface:** User-friendly prompts guide the organization process.
- **Error Handling:** Robust error handling ensures smooth operation even with permission or file system issues.


## Technologies Used
- **Python**
  - Libraries: `shutil`, `mimetypes`, `pathlib`

## Setup
1. **Clone the Repository** 
```bash
git clone https://github.com/camjenkins23/file-organization-script.git
cd file-organizer
```
2. **Run the Script**
```bash
python file_organizer.py
```
3. **Follow the Prompts**
```python
Option 1: Organize specific file types by entering the file extension (e.g., txt, pdf, jpg).
Option 2: Organize the entire folder by categorizing all file types.
```
## Usage
```python
from file_organizer import organize_entire_folder, organize_specific_file_type

# Example 1: Organize an entire folder by file types
organize_entire_folder()

# Example 2: Organize specific file types (e.g., PDFs)
organize_specific_file_type()

# Follow the prompts in the terminal to provide the folder path and/or file type.
```

## Example Outputs
### Organizing Entire Folder
**Input**: A folder with files like `example.pdf`, `photo.jpg`, `document.docx`, and `script.py`  

**Output**:
```python
[1/4] Moving: example.pdf -> pdf_files
[2/4] Moving: photo.jpg -> image_files
[3/4] Moving: document.docx -> docx_files
[4/4] Moving: script.py -> py_files

Organization Complete! Successfully moved 4/4 files.
```

### Organizing Specific File Type
**Input**: Specify pdf as the file type.

**Output**:
```
[1/1] Moving: example.pdf -> pdf_files

Organization Complete! Successfully moved 1/1 files.
```

## Custom File Type Mappings

The script uses MIME types to identify files. Common file extensions are mapped to user-friendly labels:

| MIME Type                                                                      | Folder Name  |
|-------------------------------------------------------------------------------|--------------|
| `text/plain`                                                                   | `txt_files`  |
| `application/pdf`                                                              | `pdf_files`  |
| `application/vnd.openxmlformats-officedocument.wordprocessingml.document`      | `docx_files` |
| `text/x-python`                                                                | `py_files`   |

For unmapped types, files are categorized under `unknown_files`.


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Contributions
Contributions are welcome! If you have suggestions for improvements or want to extend functionality, feel free to open an issue or submit a pull request.

## Future Improvements
- Add support for recursive directory organization.
- Implement logging for a detailed summary of the operations.
- Allow undoing of moves.# file-organization-script
Python script to automate file organization based on types or user-specified criteria.
