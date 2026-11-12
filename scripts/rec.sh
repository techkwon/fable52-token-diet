#!/bin/zsh
# usage: rec.sh <task> <pipeline> [seconds]  -> rec/<task>-<pipeline>.mp4
B=<project>/samples
T=$1; P=$2; S=${3:-16}
F=$B/runs/$T/$P/index.html
O=$B/rec/tmp-$T-$P; mkdir -p $B/rec
node $B/scripts/record.mjs $F $O $S || exit 1
ffmpeg -y -loglevel error -f concat -safe 0 -i $O/frames.ffconcat -vf "fps=30,scale=1280:800:flags=lanczos,format=yuv420p" -c:v libx264 -crf 16 -preset medium -t $S $B/rec/$T-$P.mp4
cp $O/last.png $B/rec/$T-$P.png; cp $O/report.json $B/rec/$T-$P.json; rm -rf $O
ffprobe -v error -show_entries format=duration -of csv=p=0 $B/rec/$T-$P.mp4
