#!/bin/bash

# show commands and stop if there is an error
set -ex

# this command makes a single image of whatever was not deleted
python /usr/local/anaconda/extras/smartgrid.py \
  --input-glob 'resized/*' \
  --aspect-ratio 1.92 \
  --drop-to-fit \
  --output-path smartgrid
