wm title . "Emailer errors:"
text .mytext -yscrollcommand {.s set}
.mytext insert 1.0 [exec cat /tmp/nataq_emailer_logfile]
.mytext configure  -state disabled
scrollbar .s -orient vertical -command {.mytext yview}
pack .s -side right -fill y
pack .mytext -expand yes -fill both
