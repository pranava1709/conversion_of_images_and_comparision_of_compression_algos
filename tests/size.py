# approach 3
# using file object
 
# open file
import os
file = open('lenna_tga.hpp')
 
# get the cursor positioned at end
file.seek(0, os.SEEK_END)
 
# get the current position of cursor
# this will be equivalent to size of file
print("Size of file is :", file.tell(), "bytes")