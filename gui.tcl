package require Tk
#toplevel
set entry_width 40
set entry_height 10
set label_width 15
wm title . "Nataq's Emailer"

frame .f_subject
label .l_subject -text "Subject:"  \
    -anchor e
entry .e_subject -width $entry_width
pack .l_subject .e_subject -side left -in .f_subject

frame .f_album_name
label .l_album_name -text "Album Name:"  \
    -anchor e
entry .e_album_name -width $entry_width
pack .l_album_name .e_album_name -side left -in .f_album_name

frame .f_recording_year
label .l_recording_year -text "Recording Year (optional)"  \
    -anchor e
entry .e_recording_year -width $entry_width
pack .l_recording_year .e_recording_year -side left -in .f_recording_year

frame .f_from_email
label .l_from_email -text "Sender's Email:"  \
    -anchor e
entry .e_from_email -width $entry_width
pack .l_from_email .e_from_email -side left -in .f_from_email

frame .f_from_email_pass
label .l_from_email_pass -text "Sender's Email Password:" \
     \
    -anchor e
entry .e_from_email_pass -width $entry_width -show *
pack .l_from_email_pass .e_from_email_pass \
    -side left -in .f_from_email_pass

set path_to_sfs ""
proc choose_path_to_sfs {} {
    set path_to_sfs [tk_chooseDirectory \
        -title "Choose path to soundfiles..." ]
    #puts $path_to_sfs
    .e_sfpath delete 0 end
    .e_sfpath insert 0 $path_to_sfs
}

frame .f_sfpath
label .l_sfpath -text "Path to Soundfiles:" \
    -anchor e
button .b_sfpath -text "Choose Soundfiles" -command choose_path_to_sfs
entry .e_sfpath -width $entry_width
pack .l_sfpath .e_sfpath .b_sfpath \
    -side left -in .f_sfpath

set path_to_csv ""
proc choose_path_to_csv {} {
    set path_to_csv [tk_getOpenFile \
        -title "Choose path to name and email list..."  \
        -filetypes {{{CSV Files} {.csv .CSV}}} ]
    #puts $path_to_csv
    .e_csvpath delete 0 end
    .e_csvpath insert 0 $path_to_csv
}

frame .f_csvpath
label .l_csvpath -text "Path to Name and Email File (CSV)" \
    -anchor e
button .b_csvpath -text "Choose CSV File" -command choose_path_to_csv
entry .e_csvpath -width $entry_width
pack .l_csvpath .e_csvpath .b_csvpath \
    -side left -in .f_csvpath

set path_to_img ""
proc choose_path_to_img {} {
    set path_to_img [tk_getOpenFile \
        -title "Choose path to name and email list..."  \
        -filetypes {{{PNG Files} {.png .PNG}} \
            {{JPEG Files} {.jpg .jpeg .JPG .JPEG}}} ]
    #puts $path_to_img
    .e_album_art delete 0 end
    .e_album_art insert 0 $path_to_img
}

frame .f_album_art
label .l_album_art -text "Path to Album Art (jpg or png)" \
    -anchor e
button .b_album_art -text "Choose Image" \
    -command choose_path_to_img
entry .e_album_art -width $entry_width
pack .l_album_art .e_album_art .b_album_art \
    -side left -in .f_album_art

set path_to_msg ""
proc choose_path_to_msg {} {
    set path_to_msg [tk_getOpenFile \
        -title "Choose path to name and email list..."  \
        -filetypes {{{CSV Files} {.msg .CSV}}} ]
    #puts $path_to_msg
    .e_msgpath delete 0 end
    .e_msgpath insert 0 $path_to_msg
}

frame .f_msgpath
label .l_msgpath -text "Path to Name and Email File (CSV)" \
    -anchor e
button .b_msgpath -text "Choose CSV File" -command choose_path_to_msg
entry .e_msgpath -width $entry_width
pack .l_msgpath .e_msgpath .b_msgpath \
    -side left -in .f_msgpath

frame .f_send
button .b_send -text "Send and Quit" \
    -command send_and_quit
pack .b_send -in .f_send


set frames { \
    .f_subject  \
    .f_album_name  \
    .f_recording_year \
    .f_from_email  \
    .f_from_email_pass  \
    .f_sfpath \
    .f_csvpath \
    .f_album_art \
    .f_send
}

pack {*}$frames \
    -side top

set labels {
    .l_subject 
    .l_album_name 
    .l_recording_year 
    .l_from_email 
    .l_from_email_pass 
    .l_sfpath 
    .l_csvpath
    .l_album_art
}

set maxlen 0
foreach x $labels {
    set len_ [string length [$x cget -text ]]
    if {$len_ > $maxlen} { set maxlen $len_ }
}


#foreach x $labels {
#    $x configure -width $maxlen 
#}

# When finished, print out environment variables
proc send_and_quit {} {
puts [format {
    SFPATH="%s" CSVFILE="%s" META_DATE="%s" \
    META_ALBUM_NAME="%s" META_ALBUM_PICTURE="%s" \
    EMAIL_MESSAGE="%s" \
    FROM_EMAIL="%s" \
    EMAIL_PASSWORD="%s" \
    EMAIL_SUBJECT="%s" \
} [.e_sfpath get] \
  [.e_csvpath get] \
  [.e_recording_year get] \
  [.e_album_name get] \
  [.e_album_art get] \
  []]
destroy .
}

# don't override, just do it when send and quit pressed
# wm protocol . WM_DELETE_WINDOW before_exit
