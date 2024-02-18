import os
# os.mkdir("Hello")
# os.rmdir("Hello")
# os.unlink("text.txt")  # delete
# os.makedirs("hello/how/are/you")  # works on unix, use \\ separator on windows

# chdir;mkdir;makedirs;getcwd();
# rmdir;unlink;listdir()

# os.walk(".")
for folders, subfolders, files in os.walk("./Hello/Hey"):
    print("----Currently----")
    print("folders:\n", folders)
    print("subfolders:\n", subfolders)
    print("files:\n", files)
# myfiles = [(folders, subfolders, files)
#            for folders, subfolders, files in os.walk(".")]
# print(myfiles)
