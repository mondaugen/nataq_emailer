# only mp3 works with id3 tags
format=mp3
if [ test.wav != test.$format ]; then
ffmpeg -i test.wav -c:a libmp3lame -b:a 320k test.${format}
fi
#
ffmpeg -i test.${format} -i triangle.jpg -codec copy -map 0:0 -map 1:0 -id3v2_version 3 \
    -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" \
    -metadata Title="My title" \
    -metadata Artist="My Artist" \
    -metadata Album="My Album" \
    -metadata Composer="My Composer" \
    -metadata Date=1234 \
    test_.${format}
