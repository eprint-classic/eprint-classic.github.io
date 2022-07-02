curyear=`date +'%Y'`
for i in `seq 1996 "$curyear"`
do
	echo $i
	python3 code/parse.py $i > $i.html
	sleep 5
done