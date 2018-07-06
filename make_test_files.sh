IFS="
"
files="
a b c.wav
d e f.wav
1 d x.wav
"

mkdir -p test
for f in $files
do
    echo "$f"
    echo "${f// /_}"
    sox -n "test/${f// /_}" synth 2 sine $(( $RANDOM % 300 ))
    cp test/"${f// /_}" "test/$f"
done
