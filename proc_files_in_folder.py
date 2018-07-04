# -*- coding: utf-8 -*-

import os, subprocess

LOGFILENAME='/tmp/nataq_emailer_logfile'
opt={
    'SFENDING':'wav',
    'SFPATH':'stuff for the test/Test CMPL 2018',
    'CSVFILE':'stuff for the test/camper info.csv',
    'META_DATE':2018,
    'META_ALBUM_NAME':'Camp musical Père Lindsay été 2018',
    'META_ALBUM_PICTURE':'stuff for the test/cmpl2018.png',
    'EMAIL_MESSAGE':'emailmessage.txt',
    'FROM_EMAIL':'nicholas.esterer@gmail.com',
    'EMAIL_PASSWORD':'password',
    'EMAIL_SUBJECT':'Test message',
}

# Open log file
logfile=open(LOGFILENAME,'w')

for k in opt.keys():
    if k in os.environ.keys():
        opt[k] = os.environ[k]

# load csv file containing names and emails to dictionary
# NOTE: This doesn't work if 2 people have the same name (in that case though
# they probably would have a unique ID)
emails=dict()
with open(opt['CSVFILE'],'r') as f:
    for line in f:
        name,email=line.split(',')
        email=email.strip()
        emails[name]=email

# load and convert soundfiles, store them in a dictionary under the name
# entry
soundfiles=dict()
for sfname in os.listdir(opt['SFPATH']):
    # Assert wav file
    if sfname.split('.')[-1].lower() == opt['SFENDING']:
        # get names from filename
        logfile.write('original file: %s\n' % (sfname,))
        sfname_='.'.join(sfname.split('.')[:-1])
        names=sfname_.split('_')
        # Convert soundfile and attach metadata
        meta_cmd="""\
                TITLE="{names}" \
                ARTIST="{names}" \
                ALBUM="{opt[META_ALBUM_NAME]}" \
                DATE="{opt[META_DATE]}" \
                ALBUM_PICTURE="{opt[META_ALBUM_PICTURE]}" \
                FILENAME="{filename}" \
                {prog}
                """.format(opt=opt,
                        names=', '.join(names),
                        filename=os.path.join(opt['SFPATH'],sfname),
                        prog=os.path.join(os.getcwd(),'add_meta.sh'))
        conv_filename=subprocess.check_output(meta_cmd,shell=True).strip()
        for name in names:
            if name in soundfiles.keys():
                soundfiles[name].append(conv_filename)
            else:
                soundfiles[name]=[conv_filename]

# Send emails with attachment(s) to each name

for name in emails.keys():
    # look up soundfiles to attach
    try:
        sfs=soundfiles[name]
    except KeyError:
        logfile.write("Error: couldn't find soundfiles for name \"%s\"\n" %(name,))
        continue

    logfile.write('attachments: ')
    for sf in sfs:
        logfile.write('%s ' %(sf,))
    logfile.write('\n')
    email = emails[name]

    # send email with all attachments attached
    email_cmd="""\
            NAME="{name}" \
            FROM_EMAIL="{opt[FROM_EMAIL]}" \
            EMAIL_ADDRESS="{email}" \
            EMAIL_MESSAGE="{opt[EMAIL_MESSAGE]}" \
            EMAIL_PASSWORD="{opt[EMAIL_PASSWORD]}" \
            EMAIL_SUBJECT="{opt[EMAIL_SUBJECT]}" \
            python {emailer_script} \
            """.format(opt=opt,
                    name=name,
                    email=email,
                    emailer_script=os.path.join(os.getcwd(),'send_song_in_email.py'))
    # Add files to attach as arguments to emailer_script
    for sf in sfs:
        email_cmd += '"%s" ' % (sf,)
    try:
        os.system(email_cmd)
    except subprocess.CalledProcessError as e:
        logfile.write("Error executing command: %s\n" % (email_cmd,))

logfile.close()
