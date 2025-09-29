#!/bin/bash

repo_name="neutrons"
model_name="mistral_pd"

if git ls-remote https://huggingface.co/y8z1990/${repo_name} >/dev/null 2>&1; then
    echo "✅ Repository '$repo_name' already exists"
else
    hf repo create $repo_name
fi

hf upload $repo_name ./${model_name}.gguf ${model_name}.gguf

cat >README.md <<EOF
---
license: apache-2.0
tags:
- gguf
- ollama
- fine-tuned
base_model: mistral-7b
---

# ${model_name}

Fine-tuned model for neutron powder diffraction.

## Usage with Ollama

\`\`\`bash
# Download
ollama pull ${model_name}

# Run
ollama run $REPO_ID
\`\`\`
EOF

hf upload ${repo_name} ./README.md README.md
