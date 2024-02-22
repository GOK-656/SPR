#!/bin/bash

cd /bd_targaryen/users/ve490-fall23/lyf/SPR
source /bd_targaryen/users/ve490-fall23/lyf/miniconda3/bin/activate
conda activate spr

game=$1
aug=$2
seed=$3

echo "start running experiment $aug with seed $seed on $game"
python -m scripts.run --public --game $game --augmentation $aug --momentum-tau 1. --seed $seed
