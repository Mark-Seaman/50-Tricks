#!/usr/bin/env python
# Wiki page links

from os.path    import exists, dirname, basename, join
from re         import sub, IGNORECASE, DOTALL

# Convert the url in a string to an HTML anchor
def muse_double_anchor(url):
    s = r"\[\[([\/\w\.\:\-\_]*)\]\[([ \w\.\-\_\,\?\%]*)\]\]"
    pat = re.compile(s, IGNORECASE | DOTALL)
    return pat.sub(r' <a href="\1">\2</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_single_anchor(url):
    s = r"\[\[([\/\w\.\-\_]*)\]\]"
    pat = re.compile(s, IGNORECASE | DOTALL)
    return  pat.sub(r' <a href="\1">\1</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_anchor(url):
    url = muse_double_anchor(url)
    return muse_single_anchor(url)

# Convert the Wiki Words to hyperlinks
def wiki_words(text):
    s = r"[^A-Za-z\"\']*([A-Z][a-z]+[A-Z][a-z]+([A-Z][a-z]+)*)[^A-Za-z\'\"]*"
    pat = re.compile(s, DOTALL)
    return muse_anchor(pat.sub(r'[[\1]]', text))

# Get one link from a string as a list
def extract_link(str):
    link = sub ( r'\]\[.*', '', str)
    if link.find('/')==-1: return [ link ]
    else: return []
    
# Extract all of the links from one line of text
def get_links(line):
    x=line.find('[[') 
    y=line.find(']]')
    if x>=y: return []
    return extract_link(line[x+2:y]) + get_links(line[y+2:])

# Eliminate the duplication from a list
def unique(with_dups):
    s = set()
    for i in with_dups: s.add(i) 
    return [ i for i in s ] 
            
# Extract links from an array of text
def get_all_links(text):
    results = []
    for line in text: results += get_links(line)
    return  unique(results)

# Get the links contained in this MyBook file
def get_file_links(filename):
    if not exists(filename):
        print "File not found", filename
        return [ ]
    return get_all_links(open(filename).read().split('\n'))

# Get the links contained in this MyBook file
def has_file(filename):
    return exists(filename)

