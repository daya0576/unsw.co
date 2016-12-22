#!/bin/sh

ls -al | egrep '0 Dec' | cut -d' ' -f16 | while read filename
do 
    ls -al "$filename"
    rm -f "$filename"
done 
