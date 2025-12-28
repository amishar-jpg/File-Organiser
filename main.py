import os;

def arrange_files(files, ext):
    files_with_ext = [f for f in files if f.endswith(ext)]
    print(f"Files with extension '{ext}': {files_with_ext}")
    
    for i,file in enumerate(files_with_ext):
        os.rename(file, f"photo_{i+1}{ext}")
    
    
if __name__ == "__main__":
    all_files = os.listdir('.')
    arrange_files(all_files, '.jpg')