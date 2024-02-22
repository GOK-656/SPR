#!/bin/bash

cd /bd_targaryen/users/ve490-fall23/lyf/SPR
source /bd_targaryen/users/ve490-fall23/lyf/miniconda3/bin/activate
conda activate spr

game=$1
seed=$2

echo "start running experiment with seed $seed on $game with no aug"
python -m scripts.run --public --game $game --augmentation none --target-augmentation 0 --momentum-tau 0.01 --dropout 0.5 --seed $seed
