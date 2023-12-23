curyear=`date +'%Y'`

python3 code/index.py $curyear > index.html

for i in `seq 1996 "$curyear"`
do
	echo $i
	python3 code/parse.py $i data.txt > $i.html
	sleep 5
done

for i in `seq 199 202`
do
	echo $i
	python3 code/parse.py $i data.txt > "${i}0s".html
	sleep 5
done

python3 code/parse.py -1 data.txt > all.html
