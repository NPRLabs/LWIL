#!/bin/bash
date >> /Users/agoldfarb/Desktop/Loudness/dates.txt
echo "ME" >> /Users/agoldfarb/Desktop/Loudness/dates.txt
/Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/agoldfarb/Desktop/Loudness/loudness.py ME
mv /Users/agoldfarb/Desktop/Loudness/svg/*.svg /Volumes/Divisions/Loudness/svg
#open /Users/agoldfarb/Desktop/Archive/LF/Dan.app