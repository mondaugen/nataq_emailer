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
        for name in names:
            # look up email
            try:
                email = emails[name]
            except KeyError:
                logfile.write("Error: couldn't find name \"%s\" in CSV file\n" %(name,))
                continue
            # attach meta data
            meta_cmd="""\
                    TITLE="{name}" \
                    ARTIST="{names}" \
                    ALBUM="{opt[META_ALBUM_NAME]}" \
                    DATE="{opt[META_DATE]}" \
                    ALBUM_PICTURE="{opt[META_ALBUM_PICTURE]}" \
                    FILENAME="{filename}" \
                    {prog}
                    """.format(opt=opt,
                            name=name,
                            names=', '.join(names),
                            filename=os.path.join(opt['SFPATH'],sfname),
                            prog=os.path.join(os.getcwd(),'add_meta.sh'))
            conv_filename=subprocess.check_output(meta_cmd,shell=True).strip()
            logfile.write('attachment: %s\n' %(conv_filename,))
            # send email with it attached
            email_cmd="""\
                    NAME="{name}" \
                    FILENAME="{conv_filename}" \
                    FROM_EMAIL="{opt[FROM_EMAIL]}" \
                    EMAIL_ADDRESS="{email}" \
                    EMAIL_MESSAGE="{opt[EMAIL_MESSAGE]}" \
                    EMAIL_PASSWORD="{opt[EMAIL_PASSWORD]}" \
                    EMAIL_SUBJECT="{opt[EMAIL_SUBJECT]}" \
                    python {emailer_script} \
                    """.format(opt=opt,
                            name=name,
                            conv_filename=conv_filename,
                            email=email,
                            emailer_script=os.path.join(os.getcwd(),'send_song_in_email.py'))
            try:
                os.system(email_cmd)
            except subprocess.CalledProcessError as e:
                logfile.write("Error executing command: %s\n" % (email_cmd,))

logfile.close()
