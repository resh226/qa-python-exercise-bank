import os  # For file deletion

# File name to use
filename = "sample.txt"

# ---------- 1. Create and Write to a File ----------
# ---------- Check if file already exists ----------
if os.path.exists(filename):
    print(f"File '{filename}' already exists. Not creating.")
else:
    # Create the file only if it doesn't exist
    with open(filename, 'x') as file:  # 'x' = exclusive creation
        file.write("Hello, this is a newly created file.\n")
    print(f"File '{filename}' created successfully.")

# ---------- 2. Read from the File ----------
with open(filename, 'r') as file:
    content = file.read()
    print("File Content:", content)

# ---------- 3. Update (Append) to the File ----------
with open(filename, 'a') as file:
    file.write("We are adding more lines to update the file.\nPython file handling is easy!")
    print("File updated.")

# ---------- 4. Count Words in the File ----------
with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)

print(f"Total number of words in the file: {word_count}")

# ---------- 5. Delete the File ----------
os.remove(filename)
print("File deleted.")
