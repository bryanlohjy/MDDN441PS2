#!/bin/bash
set -ex

python /usr/local/anaconda/extras/smartgrid.py \
  --use-imagemagick \
  --input-glob 'temp/cropped_cage/*' \
  --aspect-ratio 1.92 \
  --model xception \
  --drop-to-fit \
  --output-path 'temp/smartgrid'