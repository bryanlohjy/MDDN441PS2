while IFS=, read -a line;
do
	OUTPUTPATH=./outputs/cage-gif-frame${line[0]}.jpg
	TOPIMAGE=./${line[1]}
	BOTTOMIMAGE=./${line[2]}
 
	convert -size 220x440 xc:black  \
		\( ${TOPIMAGE} -resize 230x230 \) -geometry +0+0 -composite  \
		\( ${BOTTOMIMAGE} -resize 230x230 \) -geometry +0+220 -composite  \
		${OUTPUTPATH}
done < ./temp/sequencer/sequence.csv