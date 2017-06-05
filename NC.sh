#!/bin/bash
date >> /Users/username/Desktop/Loudness/dates.txt
echo "NC" >> /Users/username/Desktop/Loudness/dates.txt
/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/username/Desktop/Loudness/newscast.py
mv /Users/username/Desktop/Loudness/*.svg /Volumes/Divisions/Loudness/svg
#open /Users/username/Desktop/Archive/LF/NCDan.app