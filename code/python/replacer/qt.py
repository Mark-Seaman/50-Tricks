#!/usr/bin/python
# Test the replace   (usage:  qt.py)

from replace import *

# Test helper to check for same text
def check_text(expected_text, actual_text):
    if expected_text!=actual_text:
        print '------------------------BAD TEXT --------------------------------'
        print "Expected:"
        print expected_text
        print "Actually Got:"
        print actual_text
        exit (1)

# Here is where all the tests are performed
def quick_test():
    # Define sample data
    fromfile = 'f1'
    tofile = 'f2'
    sample_text   = [ 'this is some sample text' ]
    expected_text = [ 'that is some sample text' ]

    # Call the worker code
    write_file (fromfile, sample_text)
    replace_text(fromfile, tofile, 'this','that')
    output_text = read_file (tofile)
    
    # Check the results
    check_text(expected_text,output_text)
    expected_text += ["create an error"]
    #check_text(expected_text,output_text)

quick_test()
print "All tests pass"

