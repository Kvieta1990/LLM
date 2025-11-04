import json

def generate_addie_training_data():
    """Generate training data for neutron and X-ray scattering calculations in JSONL format"""

    # Properties to calculate
    properties = [
        "neutron absorption",
        "neutron resonance absorption", 
        "neutron scattering strength",
        "X-ray scattering strength",
        "weight of pair contribution in the overall scattering",
        "Faber Ziman coefficient",
        "self scattering level"
    ]

    # Create properties list for the response
    properties_list = "\n".join([f"• {prop}" for prop in properties])
    
    # Updated response template - ALL responses include properties
    response_template = f"Please go to website, https://addie.ornl.gov/helpsheet. Available properties to be calculated include,\n\n{properties_list}"

    # Incomplete requests (no composition specified)
    incomplete_patterns = [
        "I want to calculate the {prop} for my sample.",
        "I need {prop} data for my material.",
        "How do I calculate {prop} for my sample?",
        "I have a sample and want to know its {prop}.",
        "I need help with {prop} calculations.",
        "Can you help me calculate {prop}?",
        "I want to analyze the {prop} of my sample.",
        "How do I use ADDIE for {prop} analysis?",
        "I need {prop} values for my research.",
        "How do I determine {prop}?",
        "I have a complex alloy, can you help with {prop}?",
        "I want to find the {prop} of my material."
    ]

    # Complete requests with composition
    complete_patterns = [
        "Calculate {prop} for my sample.",
        "What's the {prop} for my material?",
        "I want to calculate {prop} for my sample composition.",
        "{prop} calculation for my material.",
        "Get {prop} for my sample.",
        "I need to calculate {prop} for my specific material.",
        "What about my sample's {prop}?",
        "My material needs {prop} calculation.",
        "Determine the {prop} of my sample.",
        "Find {prop} for my material.",
        "Get the {prop} value for my sample.",
        "What is the {prop} of my material?"
    ]

    training_data = []

    # Generate incomplete request examples for each property
    for prop in properties:
        for pattern in incomplete_patterns:
            question = pattern.format(prop=prop)
            
            # Create JSONL entry with properties list
            entry = {
                "text": f"Scope: General question about neutron/X-ray scattering\nContext: Calculation\nQ: {question}\nA: {response_template}"
            }
            training_data.append(entry)

    # Generate complete request examples - NOW ALSO INCLUDING PROPERTIES
    for prop in properties:
        for pattern in complete_patterns:
            question = pattern.format(prop=prop)
            
            # Create JSONL entry with properties list (same as incomplete)
            entry = {
                "text": f"Scope: General question about neutron/X-ray scattering\nContext: Calculation\nQ: {question}\nA: {response_template}"
            }
            training_data.append(entry)

    # Add some mixed property requests
    mixed_patterns = [
        "Calculate neutron absorption and X-ray scattering strength for my sample.",
        "I need both neutron scattering strength and Faber Ziman coefficient.",
        "What are the neutron absorption and self scattering level for my material?",
        "Calculate multiple scattering properties for my sample.",
        "I need comprehensive scattering analysis.",
        "Get all neutron properties for my material.",
        "Calculate both neutron and X-ray properties."
    ]

    for pattern in mixed_patterns:
        # Create JSONL entry with properties list
        entry = {
            "text": f"Scope: General question about neutron/X-ray scattering\nContext: Calculation\nQ: {pattern}\nA: {response_template}"
        }
        training_data.append(entry)

    return training_data


# Generate and save training data
training_examples = generate_addie_training_data()
with open('train_addie.jsonl', 'w') as f:
    for example in training_examples:
        f.write(json.dumps(example) + '\n')

print(f"Generated {len(training_examples)} training examples")
print("Training data covers:")
print("- 7 different scattering properties")
print("- ALL requests include available properties list")
print("- Various ways to ask for calculations")
print("- Mixed property requests")
print("- Output in JSONL format")
print("Saved to train_addie_complete.jsonl")
