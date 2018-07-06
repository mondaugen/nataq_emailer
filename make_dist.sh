mkdir -p .dist
cp add_meta.sh proc_all_files.py README.txt send_song_in_email.py emailer
curl 'https://evermeet.cx/ffmpeg/ffmpeg-4.0.1.7z' > /tmp/ffmpeg-4.0.1.7z
zip -r emailer emailer
