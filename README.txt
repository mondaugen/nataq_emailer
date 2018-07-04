Send emails containing sound files to many people

How to use:

Make a CSV file (comma separated values) where each line is:

<name (first and last)>, <email>, <path to soundfile>, <track name>, <track composer>

The following is an example:

*** BEGIN FILE ***
Joe Doe, n.alois.esterer@gmail.com, test/1 d x.wav, hyundai sonata, chopin
Nàmé with âçcènts, n.alois.esterer@gmail.com, test/a b c.wav, rap battle, ludwig van
another name, nicholas.esterer@gmail.com, test/d e f.wav, déspositø, justin biber
*** END FILE ***

Make a file called emailmessage.txt, the following is an example

*** BEGIN FILE ***

Bonjour {NAME},

Voici ton enregistrement.

a plus,
 
Nataq

*** END FILE ***

The {NAME} text will be replaced with the name in the first column of each row
of the CSV file.

Now you need to set up your gmail account:

make a file called fromemail.txt that contains only your email. For me, this would be

*** BEGIN FILE ***
nicholas.esterer@gmail.com
*** END FILE ***

also make a file called fromemailpass.txt that contains the password to your gmail account. For me, this would be (with a fake password of course)

*** BEGIN FILE ***
mypassword
*** END FILE ***

Finally, set up proc_all_files.py so that it adds the album art and track ID tags. You will see some variables all in captial letters at the top of the file. Here's an explanation:

# The file containg the comma separated values (performer name, file name, etc.)
LISTFILE="./test_list.csv"
# The file containg the image to be included with the sound file.
ALBUM_PICTURE="./triangle.jpg"
# The album name
ALBUM_NAME="The greatest album of all time"
# The year of the album
DATE=1999

Finally, to send all the emails, do, in a terminal:

python proc_all_files.py
