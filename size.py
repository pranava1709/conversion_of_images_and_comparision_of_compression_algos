import os
file = open('"file_name".txt')
file.seek(0, os.SEEK_END)
print("Size of file is :", file.tell(), "bytes")