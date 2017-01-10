#!/bin/sh

ls -al | egrep '0 Dec' | cut -d' ' -f15 | while read filename
do 
    echo "Deleting $filename"
    ls -al "$filename"
    rm -f "$filename"
done 
