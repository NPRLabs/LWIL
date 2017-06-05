#!/bin/bash
date >> /Users/username/Desktop/Loudness/dates.txt
echo "WE Sat" >> /Users/username/Desktop/Loudness/dates.txt
/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/username/Desktop/Loudness/loudness.py WESat
mv /Users/username/Desktop/Loudness/svg/*.svg /Volumes/Divisions/Loudness/svg
#open /Users/username/Desktop/Archive/LF/Dan.app