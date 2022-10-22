curyear=`date +'%Y'`
for i in `seq 1996 "$curyear"`
do
	echo $i
	cat data.txt | python3 code/parse.py $i > $i.html
	sleep 5
done

for i in `seq 199 202`
do
	echo $i
	cat data.txt | python3 code/parse.py $i > "${i}0s".html
	sleep 5
done

cat data.txt | python3 code/parse.py -1 > all.html