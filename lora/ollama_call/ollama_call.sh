#!/bin/bash

python ollama_main.py --model mistral_pd \
    --max-tokens 50 \
    --prompt "table: 1-10015132-16
    columns: Player, No., Nationality, Position, Years in Toronto, School/Club Team
    Q: What is terrence ross' nationality
    A: "
