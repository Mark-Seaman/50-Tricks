#!/bin/bash
# List of code files

find $pd|filter-path|grep -v 'node_modules'

