#!/bin/bash
COUNTER=0
while :
do
        timeout 5 youtube-dl --no-part $1 --output data$COUNTER.mp4
        sleep 5
        ffmpeg -i data$COUNTER.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 $(pwd)/audio/data$COUNTER.wav
        rm data$COUNTER.mp4
        python speech-to-text.py --file $(pwd)/audio/data$COUNTER.wav
        rm $(pwd)/audio/data$COUNTER.wav
        let "COUNTER+=1"
done
