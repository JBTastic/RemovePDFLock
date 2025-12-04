# PDF Decrypter

This tool decrypts password-protected PDF files inside a selected folder. It recursively scans all subfolders, detects encrypted PDFs, and saves decrypted versions either separately or by replacing the originals.

## Features

- Decrypts all encrypted PDF files in a folder (including subfolders).
- Option to keep the original files (saves as decrypted_FILENAME.pdf).
- Automatically skips:
  - Non-PDF files
  - Already unencrypted PDFs
  - PDFs with an incorrect password
  - Invalid or corrupted files
- Displays a summary after completion.

## Installation

### Requirements

- Python 3.10 or newer
- Required Python libraries: pypdf, cryptography, tkinter  
``` bash
  pip install -r requirements.txt
```

(tkinter is included by default on Windows and most Linux distributions.)

## Windows Executable
A prebuilt `.exe` for Windows 10 is available in the [Releases](https://github.com/JBTastic/RemovePDFLock/releases) section of this repository.
You can download it and run it directly without installing Python.

## Usage with Python

1. Start the script:  
``` bash
python RemovePDFLock.py
```

2. In the GUI:
   - Select the folder containing the PDFs
   - Enter the password
   - (Optional) Enable “Keep originals” to store decrypted copies separately
   - Click “Decrypt PDFs”

3. After processing, a summary window shows how many files were decrypted and how many were skipped.

## Notes

- Files are overwritten only if “Keep originals” is disabled.
- The provided password is applied to all PDFs in the selected directory.
- The application works entirely locally; nothing is uploaded or transmitted.

## License

This project is licensed under the terms described in the [LICENSE](LICENSE) file.
