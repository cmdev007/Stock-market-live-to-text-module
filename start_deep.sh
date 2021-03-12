#!/bin/bash
#COUNTER=0
# while :
# do
youtube-dl $1 -o - | ffmpeg -i - -f wav - | pv | python speech-to-text-deep.py
# done
