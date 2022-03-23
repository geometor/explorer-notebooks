#!/usr/bin/env bash
find * -maxdepth 0 -name '*.png' | sort | sed 's/^/file /' > gif.lst
find ranges -name '*.png' | grep -v zoom | sort | sed 's/^/file /' >> gif.lst
find ranges -name '*.png' | grep zoom | sort | sed 's/^/file /' >> gif.lst

 
ffmpeg -y -f concat -r 1 -i gif.lst -s 960x540 build.gif

sxiv -bfa  build.gif

