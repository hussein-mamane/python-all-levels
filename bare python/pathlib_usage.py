import pathlib

str_path = "./Hello"
str_path_create = "./Hello/created.txt"
str_path_read = "./Hello/Hey/How.txt"

path = pathlib.Path(str_path)
path.mkdir(parents=False, exist_ok=True)

path_create = pathlib.Path(str_path_create)
path_create.touch(exist_ok=True)

path_read = pathlib.Path(str_path_read)
text_read = path_read.read_text(encoding="utf-8")

print(path.is_dir())
print(path.is_file())
print(path.exists())
print(path.absolute().as_uri())
print(path.resolve())
print(path.name)
print(path.suffix)
print(path.stem)
print(path.stat().st_size)  # in bytes

# depth of the one directory only, not subdirectories
for p in path.iterdir():
    print("Directory :", p) if p.is_dir() else print("File :", p)

for p in path.glob("*.txt"):
    print("Text File :", p)

for p in path.rglob("*.txt"):
    print("Text File in Subdirectory :", p)

# The same as rglob
for p in path.glob("**/*.txt"):
    print("Text File in Subdirectory :", p)
    print(type(p))  # <class 'pathlib.PosixPath'>
    p.rename(f"{p.parent}/{p.stem}.text")
"""
print(text_read)

# path_create.unlink(missing_ok=True)
# path.rename("HELLO")

path_create.write_text(text_read)
# read_bytes and write bytes also exists
# pathlib does not write if the file doesn't exists it does not create it

with path_read.open("a") as f:
    f.writelines(text_read)
    
"""
