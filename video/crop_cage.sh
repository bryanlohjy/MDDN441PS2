while IFS=, read -a line;
do
	INPUTPATH=./temp/downloads/${line[0]}
	OUTPUTPATH=./temp/cropped_cage/${line[0]}-${line[1]}.jpg
	FACEWIDTH=$((${line[3]}-${line[5]}))
	FACEHEIGHT=$((${line[4]}-${line[2]}))
	RESCALE_FACTOR=$(bc <<< "scale=2;(220/${FACEWIDTH})*100")
	SCALED_TOP=$(bc <<< "scale=2;${line[2]}*${RESCALE_FACTOR}/100")
	SCALED_LEFT=$(bc <<< "scale=2;${line[5]}*${RESCALE_FACTOR}/100")
	convert ${INPUTPATH} -crop ${FACEWIDTH}x${FACEHEIGHT}+${line[5]}+${line[2]} +repage -resize ${RESCALE_FACTOR}% ${OUTPUTPATH}
done < ./temp/face_recognition/cage_bounds.csv