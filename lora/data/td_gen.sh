#!/bin/bash

ENV_NAME=base

# Activate proper environment
source /Users/y8z/miniforge3/etc/profile.d/conda.sh
conda activate $ENV_NAME

echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
echo "The conda environment $ENV_NAME has been activated."
echo "Python location: $(which python)"
echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"

# Run through the training, test and validation data generation.
python gen_mt_train_data_ollama.py --input train.jsonl
python gen_mt_train_data_ollama.py --input test.jsonl
python gen_mt_train_data_ollama.py --input valid.jsonl

conda deactivate
