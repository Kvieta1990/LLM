import json


def generate_addie_training_data():
    """Generate training data for neutron and X-ray scattering calculations
    in JSONL format
    """

    # Properties to calculate
    calculation_properties = [
        "neutron absorption",
        "neutron resonance absorption",
        "neutron scattering strength",
        "X-ray scattering strength",
        "weight of pair contribution in the overall scattering",
        "Faber Ziman coefficient",
        "self scattering level"
    ]

    # Simulation and planning properties
    simulation_properties = [
        "plan my scattering measurements",
        "simulate Bragg diffraction patterns",
        "simulate instrument Bragg diffraction patterns",
        "simulate neutron total scattering patterns",
        "simulate X-ray total scattering patterns",
        (
            "estimate how long I should measure my samples for Bragg "
            "diffraction or total scattering"
        ),
        (
            "estimate the uncertainty level of the powder diffraction "
            "for my samples"
        )
    ]

    # Combine all properties
    all_properties = calculation_properties + simulation_properties

    # Create properties list for the response
    properties_list = "\n".join([f"• {prop}" for prop in all_properties])

    # Updated response template - ALL responses include properties
    response_template = (
        f"[ADDIE] Please go to website, https://addie.ornl.gov/helpsheet. "
        f"Available properties to be calculated include,\n\n{properties_list}"
    )

    # Incomplete requests (no composition specified)
    incomplete_patterns = [
        "I want to calculate the {prop} for my sample.",
        "I need {prop} data for my material.",
        "How do I calculate {prop} for my sample?",
        "I have a sample and want to know its {prop}.",
        "I need help with {prop} calculations.",
        "Can you help me calculate {prop}?",
        "I want to analyze the {prop} of my sample.",
        "I need {prop} values for my research.",
        "How do I determine {prop}?",
        "I have a complex alloy, can you help with {prop}?",
        "I want to find the {prop} of my material.",
        "I want to have some ideas about {prop}.",
        "Help me with {prop}.",
        "Help me with {prop} calculation.",
        "Can you help me with {prop}.",
        "Can you help me with {prop} calculation.",
        "I want to know about {prop}.",
        "I want to know about {prop} for my material."
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

    # Specific patterns for simulation and planning
    simulation_patterns = [
        "I want to {prop}.",
        "I need to {prop}.",
        "How do I {prop}?",
        "Can you help me {prop}?",
        "Help me {prop}.",
        "I want to know how to {prop}.",
        "I need assistance to {prop}.",
        "What tools can help me {prop}?",
        "I'm trying to {prop}.",
        "I need help with {prop}.",
        "What's the best way to {prop}?",
        "I want guidance on {prop}.",
        "I need information about {prop}."
    ]

    training_data = []

    # Generate examples for calculation properties
    for prop in calculation_properties:
        # Incomplete requests
        for pattern in incomplete_patterns:
            question = pattern.format(prop=prop)
            entry = {
                "text": (
                    f"Scope: General question about neutron/X-ray scattering\n"
                    f"Category: Calculation\nQ: {question}\n"
                    f"A: {response_template}"
                )
            }
            training_data.append(entry)

        # Complete requests
        for pattern in complete_patterns:
            question = pattern.format(prop=prop)
            entry = {
                "text": (
                    f"Scope: General question about neutron/X-ray scattering\n"
                    f"Category: Calculation\nQ: {question}\n"
                    f"A: {response_template}"
                )
            }
            training_data.append(entry)

    # Generate examples for simulation and planning properties
    for prop in simulation_properties:
        for pattern in simulation_patterns:
            question = pattern.format(prop=prop)
            entry = {
                "text": (
                    f"Scope: General question about neutron/X-ray scattering\n"
                    f"Category: Simulation/Planning\nQ: {question}\n"
                    f"A: {response_template}"
                )
            }
            training_data.append(entry)

    # Add mixed property requests
    mixed_patterns = [
        (
            "Calculate neutron absorption and X-ray scattering strength "
            "for my sample."
        ),
        (
            "I need both neutron scattering strength and Faber Ziman "
            "coefficient."
        ),
        (
            "What are the neutron absorption and self scattering level "
            "for my material?"
        ),
        "Calculate multiple scattering properties for my sample.",
        "I need comprehensive scattering analysis.",
        "Get all neutron properties for my material.",
        "Calculate both neutron and X-ray properties.",
        (
            "I want to simulate Bragg diffraction patterns and estimate "
            "measurement time."
        ),
        (
            "Help me plan my measurements and simulate total scattering "
            "patterns."
        ),
        "I need to simulate patterns and estimate uncertainty levels.",
        (
            "Can you help me plan measurements and calculate neutron "
            "absorption?"
        ),
        (
            "I want to simulate diffraction patterns and calculate "
            "scattering strength."
        )
    ]

    for pattern in mixed_patterns:
        entry = {
            "text": (
                f"Scope: General question about neutron/X-ray scattering\n"
                f"Category: Calculation\nQ: {pattern}\n"
                f"A: {response_template}"
            )
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
print("- 7 calculation properties")
print("- 7 simulation/planning properties")
print("- ALL requests include available properties list")
print("- Various ways to ask for calculations and simulations")
print("- Mixed property requests")
print("- Output in JSONL format")
print("Saved to train_addie.jsonl")
