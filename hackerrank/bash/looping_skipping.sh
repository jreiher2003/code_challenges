#!/bin/bash 
# colour1="red"
# colour2="light blue"
# colour3="dark green"
# for X in "$colour1" "$colour2" "$colour3"
# do
#     echo $X
# done

X=0
while [ $X -le 20 ]
do
    echo $X
    X=$((X+1))
done

#!/bin/bash
files="$(ls)"
web_files=`ls public_html`
echo "$files"      # we need the quotes to preserve embedded newlines in $files
echo "$web_files"  # we need the quotes to preserve newlines 
X=`expr 3 \* 2 + 4` # expr evaluate arithmatic expressions. man expr for details.
echo "$X"