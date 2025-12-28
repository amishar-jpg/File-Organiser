

#  File Organizer App (Python)

A simple Python-based **File Organizer Application** that automatically renames files based on their extension. This project helps in organizing files (such as images) in a directory by giving them a consistent and structured naming format.

---

##  Features

* Scans the current directory for files
* Filters files by extension (e.g., `.jpg`)
* Automatically renames matching files in sequence
* Lightweight and beginner-friendly
* Useful for organizing image folders

---

##  Tech Stack

* **Python**
* **OS Module**

---

##  Project Structure

```
file-organizer-app/
│
├── main.py        # Main script for organizing files
├── README.md      # Project documentation
```

---


##  How to Run the App

```bash
python main.py
```

After running, all `.jpg` files will be renamed as:

```
photo_1.jpg
photo_2.jpg
photo_3.jpg
...
```

---

##  Important Note

* The script **renames files permanently**
* Make sure to **backup your files** before running the program
* Avoid running it in directories with important system files

---

##  Customization

### Change File Extension

Modify this line in `main.py`:

```python
arrange_files(all_files, '.jpg')
```

Example:

```python
arrange_files(all_files, '.png')
```

### Change File Naming Pattern

```python
os.rename(file, f"photo_{i+1}{ext}")
```

Example:

```python
os.rename(file, f"image_{i+1}{ext}")
```

---

## 📚 What I Learned

* Working with files and directories in Python
* Using the `os` module for file handling
* Automating repetitive file management tasks
* Writing modular Python functions

---
