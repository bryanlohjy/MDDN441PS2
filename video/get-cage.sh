set -ex
for YEAR in 2009 2010 2011 2013
do
	for PAGE in $(seq -f "%02g" 1 12)
	do
	# build the url 
	URL="http://niccageaseveryone.blogspot.co.nz/"$YEAR"/"$PAGE
		# fetch the images \
		wget \
			--adjust-extension \
			--no-directories \
			--convert-links \
			--backup-converted \
			--random-wait\
			--limit-rate=100k \
			--span-hosts \
			--directory-prefix=temp/downloads \
			--page-requisites \
			--timestamping \
			--execute robots=off \
			--accept=*.jpg \
			$URL
	done
done