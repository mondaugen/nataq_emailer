# only mp3 works with id3 tags
format=aif
if [ test.wav != test.$format ]; then
ffmpeg -i test.wav test.${format}
fi
#
ffmpeg -i test.${format} -i triangle.jpg -codec copy -map 0:0 -map 1:0 -id3v2_version 3 \
    -metadata title="Cool guy music" \
    test_.${format}
