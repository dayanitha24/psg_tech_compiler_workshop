

python3 $1 > /tmp/test.c
gcc /tmp/test.c -o /tmp/test

python3 $2 > /tmp/1.out
/tmp/test > /tmp/2.out

cmp --silent /tmp/1.out /tmp/2.out || echo "C and python files are different"
