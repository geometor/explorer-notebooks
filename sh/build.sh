prefix=$1
cat $( find $prefix-*.png | sort ) | ffmpeg -y -r 16 -i - $prefix.mp4 ; mpv -fs -loop=yes $prefix.mp4
