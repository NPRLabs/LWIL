#!/bin/bash
date >> /Users/agoldfarb/Desktop/Loudness/dates.txt
echo "NC" >> /Users/agoldfarb/Desktop/Loudness/dates.txt
/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/agoldfarb/Desktop/Loudness/newscast.py
mv /Users/agoldfarb/Desktop/Loudness/*.svg /Volumes/Divisions/Loudness/svg
#open /Users/agoldfarb/Desktop/Archive/LF/NCDan.app