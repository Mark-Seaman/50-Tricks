#!/usr/bin/python
# Perform text replacement in files

from os.path    import exists

# Read lines from a file and strip off the tailing newline
def read_file(filename):
    if not exists(filename): return [ ]
    f=open(filename)
    results = [line[:-1] for line in f.readlines()]
    f.close()
    return results

# Write lines of text to a file
def write_file(filename, lines):
    f=open(filename, "w")
    f.write("\n".join(lines)+"\n")
    f.close()
 
# Convert a single line of text
def replace_line(line, from_string, to_string):
    return line.replace(from_string, to_string)

# Delete a relative path name   
def replace_text(f1, f2, from_string, to_string):  
    t = read_file(f1)
    t = map (lambda x: replace_line(x,from_string,to_string), t)
    write_file(f2, t)
