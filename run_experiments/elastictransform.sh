#!/bin/bash

cd /bigdata/users/ve490-fall23/lyf/SPR/
source /bigdata/users/ve490-fall23/anaconda3/bin/activate
conda activate spr

aug=elastictransform

echo "start running experiment $aug"
python -m scripts.run --public --game pong --augmentation $aug --momentum-tau 1.
