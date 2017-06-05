#!/bin/bash
date >> /Users/agoldfarb/Desktop/Loudness/dates.txt
echo "WATC" >> /Users/agoldfarb/Desktop/Loudness/dates.txt
/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/agoldfarb/Desktop/Loudness/loudness.py WATC
mv /Users/agoldfarb/Desktop/Loudness/svg/*.svg /Volumes/Divisions/Loudness/svg
#open /Users/agoldfarb/Desktop/Archive/LF/Dan.app