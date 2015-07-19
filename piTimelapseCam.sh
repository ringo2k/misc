#!/bin/sh

DURATION=36000000 	# in ms
PICTIME=5000   	# in ms

echo "starting timelapse picam shooting with following paramters"

echo "duration: $DURATION ms" 
echo "time for each picture: $PICTIME ms" 

mkdir pictures

raspistill -o pictures/a%04d.jpg -t $DURATION -tl $PICTIME
