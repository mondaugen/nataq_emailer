# stuff is passed in as environment variables
# FILENAME path to sound file
# ALBUM_PICTURE path to the album art
# TITLE the song title
# ARTIST the performer
# ALBUM album title
# DATE the date of performance
FFMPEG="$(dirname $0)/ffmpeg_linux"
format=mp3
title_stub=$(python -c "print('.'.join(\"${FILENAME}\".split('.')[:-1]))")
tmp_out_file="${title_stub}_.${format}" 
out_file="${title_stub}.${format}" 
#echo "${FILENAME}"
#echo "${out_file}"
${FFMPEG} -y -i "${FILENAME}" -c:a libmp3lame -b:a 320k "${tmp_out_file}"

${FFMPEG} -y -i "${tmp_out_file}" -i "${ALBUM_PICTURE}" -codec copy -map 0:0 -map 1:0 -id3v2_version 3 \
    -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" \
    -metadata Title="${TITLE}" \
    -metadata Artist="${ARTIST}" \
    -metadata Album="${ALBUM}" \
    -metadata Date="${DATE}" \
    "${out_file}"

echo "${out_file}"
