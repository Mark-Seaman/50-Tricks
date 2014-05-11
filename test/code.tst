#!/bin/bash
# List of code files

find $p/code|filter-path|grep -v 'node_modules'

