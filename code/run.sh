for i in {1996..2022}
do
	echo $i
	python3 parse.py $i > $i.html
	sleep 5
done