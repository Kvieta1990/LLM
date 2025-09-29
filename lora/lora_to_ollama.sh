#!/bin/bash

# +-+-+-+-+-+-+-+-+-+-+-+
# Input parameters
# +-+-+-+-+-+-+-+-+-+-+-+
converter_path="/Users/y8z/Dev/LLM/llama.cpp"
model_out_name="mistral_pd"

# Initialize mamba and activate the environment.
eval "$(mamba shell hook --shell bash)"
mamba activate mlx

# Fine tuning. The generated adapter files will be saved to the `adapters` directory.
# The `adapters` directory is not necessarily existing - the routine will create it.
mlx_lm.lora --train \
    --model mistralai/Mistral-7B-Instruct-v0.2 \
    --data data --batch-size 4 \
    --iters 2000

[ -d "models" ] || mkdir models

# Fuse the adapter to the model.
mlx_lm.fuse --model mistralai/Mistral-7B-Instruct-v0.2 --save-path ./models/mistral_pd --adapter-path ./adapters/

# Use the converter script from the following repo to convert the fused mlx model to the ollama format.
#
# https://github.com/ggerganov/llama.cpp
#
python ${converter_path}/convert_hf_to_gguf.py ./models/mistral_pd --outfile ./models/mistral_pd.gguf --outtype q8_0

cat <<EOL >Modelfile
FROM ./models/mistral_pd.gguf
EOL

ollama create ${model_out_name} -f Modelfile
ollama list
