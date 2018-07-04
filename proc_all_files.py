import os
import subprocess

# The file containg the comma separated values (performer name, file name, etc.)
LISTFILE="./test_list.csv"
# The file containg the image to be included with the sound file.
ALBUM_PICTURE="./triangle.jpg"
# The album name
ALBUM_NAME="The greatest album of all time"
# The year of the album
DATE=1999

with open(LISTFILE,"r") as f:
    for l in f:
        fields=[fi.strip() for fi in l.split(",")]
        meta_cmd="""\
                TITLE="{fields[3]}" \
                ARTIST="{fields[0]}" \
                ALBUM="{ALBUM_NAME}" \
                COMPOSER="{fields[4]}" \
                DATE="{DATE}" \
                ALBUM_PICTURE="{ALBUM_PICTURE}" \
                FILENAME="{fields[2]}" \
                ./add_meta.sh
                """.format(fields=fields,ALBUM_NAME=ALBUM_NAME,ALBUM_PICTURE=ALBUM_PICTURE,DATE=DATE)
        conv_filename=subprocess.check_output(meta_cmd,shell=True).strip()
        print("Sending file: %s" % (conv_filename,))
        email_cmd="""\
                NAME="{fields[0]}" \
                FILENAME="{FILENAME}" \
                EMAIL_ADDRESS="{fields[1]}" \
                python send_song_in_email.py \
                """.format(fields=fields,FILENAME=conv_filename)
        try:
            os.system(email_cmd)
        except subprocess.CalledProcessError as e:
            sys.stderr.write("Error executing command: %s\n" % (e.cmd,))
            continue
        print("File sent")
