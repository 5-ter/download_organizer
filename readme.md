# Download Organizer

A Python script that automatically organizes files in your Downloads folder by reading their magic numbers (file signatures) and sorting them into categorized subfolders.

## About

This script keeps your Downloads folder clean by automatically categorizing files based on their actual file type rather than just their extension. It reads the first few bytes of each file (the "magic number") to determine what type of file it really is, making it more reliable than extension-based sorting.

**Currently supports:**
- Text: txt
- Images: PNG, JPEG, GIF
- Videos: MP4, WEBM
- Documents: PDF , DOCX
- Audio: MP3
- Executables: EXE
- Installers: MSI, MSIX
- Everything else goes to Misc

Files are sorted into dedicated folders: `executables`, `photos`, `videos`, `installers`, `docs`, `txt` and `misc`.

## How It Works

1. Creates the necessary category folders in your Downloads directory if they don't exist
2. Scans each file and reads its first 4 bytes to identify the file signature
3. Matches the signature against a dictionary of known magic numbers
4. For MP4 files specifically, reads up to 12 bytes to check for the ftyp marker
5. Falls back to file extension if no magic number matches
6. Moves files to their appropriate category folder
7. Automatically handles name conflicts by appending numbers (e.g., `photo(1).jpg`)

## Getting Started

### Prerequisites
- Python 3.10 or higher (uses match-case statements)

### Installation

```bash
# Clone the repository
git clone https://github.com/5-ter/download-organizer.git
cd download-organizer

# Run the script
python3 main.py
```

That's it. The script will create the necessary folders and start organizing your files.

## Usage

Simply run:
```bash
python3 main.py
```

The script will process all files in your Downloads folder and move them to appropriate subfolders. Files currently in use or lacking proper permissions will be skipped with an error message.

**Example:**
```
Downloads/
├── vacation.jpg       → Downloads/photos/
├── report.pdf         → Downloads/docs/
├── song.mp3          → Downloads/misc/
└── installer.exe      → Downloads/executables/
```

## Technical Details

The script uses file magic numbers instead of relying solely on extensions, which means:
- A `.txt` file renamed to `.jpg` will still be correctly identified
- More accurate file type detection
- Better handling of files with missing or incorrect extensions

**Magic numbers currently recognized:**
- `89504E470D0A1A0A` - PNG images
- `FFD8FF` - JPEG images  
- `474946383761` - GIF images
- `4D5A` - EXE executables
- `494433`, `FFFB`, `FFF3`, `FFF2` - MP3 audio
- `255044462D` - PDF documents
- `66747970` (within first 12 bytes) - MP4 video

## Built With

- **pathlib** - Modern file path handling
- **shutil** - File moving operations
- **sys** - System-specific parameters

## Planned Features

- Monitor Downloads folder for new files to organize automatically
- Custom folder configuration
- Command line arguments for more control
- Expanded magic number dictionary for more file types
- Option to organize by date or custom rules
- Dry-run mode to preview changes
- Logging of all file operations

## Important Notes

- The script **moves** files, it doesn't copy them
- Files that can't be read (permission errors) are skipped
- Consider backing up your Downloads folder before running for the first time
- Duplicate filenames are handled automatically with numbered suffixes

## What I Learned

Building this project taught me about:
- Reading and interpreting binary file signatures
- Recursive functions for handling edge cases
- Python's pathlib for cross-platform file handling
- Error handling in file operations
- Practical automation that solves a real problem

## License

Open source and available for personal and educational use.

## Author

**Henrique**  
GitHub: [@5-ter](https://github.com/5-ter)

## Contributing

Found a bug or have a feature suggestion? Feel free to open an issue or submit a pull request.

---

A simple utility that does one thing well: keeping your Downloads folder organized.

