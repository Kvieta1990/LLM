import json


def generate_remote_experiment_training_data():
    """Generate training data for remote experiment control at SNS and HFIR
    in JSONL format
    """

    # Standard answer for general remote experiment questions
    general_answer = (
        "The remote experiment capability is available at SNS and HFIR. "
        "Please log in ORNL Analysis cluster at `analysis.sns.gov` using "
        "either web browser or Thinlinc. Go to `Applications` -> "
        "`Remote Experiments` and select your instrument. This will launch "
        "the connection to the remote experiment machine where we can launch "
        "a terminal and type `css` to start the EPICS instrument control "
        "software."
    )

    # Instruments with confirmed remote capability
    confirmed_instruments = {
        'SNS': {
            'NOMAD': 'BL-1B NOMAD',
            'POWGEN': 'BL-11A POWGEN'
        },
        'HFIR': {
            'HB2A': 'HB-2A POWDER',
            'HB2C': 'HB-2C WAND'
        }
    }

    # Instruments with uncertain remote capability
    uncertain_sns_instruments = [
        'ARCS', 'BASIS', 'CNCS', 'CORELLI', 'EQSANS', 'FNPB', 'HYSPEC',
        'LIQREF', 'MAGREF', 'MANDI', 'NSE', 'SEQUOIA', 'SNAP', 'TOPAZ',
        'USANS', 'VENUS', 'VISION', 'VULCAN'
    ]

    uncertain_hfir_instruments = [
        'BIOSANS', 'CTAX', 'DEMAND', 'GPSANS', 'HIDRA', 'IMAGINE',
        'MARS', 'PTAX', 'TAX', 'VERITAS'
    ]

    uncertain_answer = (
        "Remote experimentation capability may be available for the "
        "instrument, but I am not hundred percent sure. I am trained to be "
        "a powder diffraction AI. Sorry for my narrow knowledge base, if I "
        "have to say that."
    )

    # General question patterns
    general_patterns = [
        "Is it possible to remotely control my experiments at SNS or HFIR?",
        "How do I perform a remote experiment at SNS or HFIR?",
        "How do I remotely control my experiments at SNS or HFIR?",
        "Can I control my experiment remotely at SNS or HFIR?",
        "What is the process for remote experiments at SNS or HFIR?",
        "How do I access remote experiment capabilities at SNS or HFIR?",
        "Is remote control available for experiments at SNS or HFIR?",
        "Tell me about remote experiment control at SNS or HFIR.",
        "I want to control my experiment remotely at SNS or HFIR.",
        "Help me with remote experiment control at SNS or HFIR.",
        "What are the remote experiment options at SNS or HFIR?",
        "How can I remotely monitor my experiment at SNS or HFIR?"
    ]

    # Instrument-specific question patterns
    instrument_patterns = [
        "I have an experiment happening on {instrument} at {facility} and I want to control it from remotely, how should I do this?",
        "How do I remotely control my experiment on {instrument} at {facility}?",
        "Can I control {instrument} at {facility} remotely?",
        "What is the remote access procedure for {instrument} at {facility}?",
        "I need to remotely access {instrument} at {facility}.",
        "Help me control my {instrument} experiment at {facility} remotely.",
        "Remote control for {instrument} at {facility}?",
        "I want to remotely monitor my experiment on {instrument} at {facility}.",
        "How do I connect to {instrument} at {facility} for remote control?",
        "What's the process for remote experiment on {instrument} at {facility}?"
    ]

    training_data = []

    # Generate general questions
    for pattern in general_patterns:
        entry = {
            "text": (
                f"Scope: Remote experiment control\n"
                f"Category: Experimentation\nQ: {pattern}\n"
                f"A: {general_answer}"
            )
        }
        training_data.append(entry)

    # Generate questions for confirmed instruments
    for facility, instruments in confirmed_instruments.items():
        for instrument, menu_name in instruments.items():
            specific_answer = (
                "The remote experiment capability is available at SNS and "
                "HFIR. Please log in ORNL Analysis cluster at "
                "`analysis.sns.gov` using either web browser or Thinlinc. "
                f"Go to `Applications` -> `Remote Experiments` and select "
                f"`{menu_name}`. This will launch the connection to the "
                "remote experiment machine where we can launch a terminal "
                "and type `css` to start the EPICS instrument control "
                "software."
            )

            for pattern in instrument_patterns:
                question = pattern.format(
                    instrument=instrument,
                    facility=facility
                )
                entry = {
                    "text": (
                        f"Scope: Remote experiment control\n"
                        f"Category: Experimentation\nQ: {question}\n"
                        f"A: {specific_answer}"
                    )
                }
                training_data.append(entry)

    # Generate questions for uncertain SNS instruments
    for instrument in uncertain_sns_instruments:
        for pattern in instrument_patterns:
            question = pattern.format(
                instrument=instrument,
                facility='SNS'
            )
            entry = {
                "text": (
                    f"Scope: Remote experiment control\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {uncertain_answer}"
                )
            }
            training_data.append(entry)

    # Generate questions for uncertain HFIR instruments
    for instrument in uncertain_hfir_instruments:
        for pattern in instrument_patterns:
            question = pattern.format(
                instrument=instrument,
                facility='HFIR'
            )
            entry = {
                "text": (
                    f"Scope: Remote experiment control\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {uncertain_answer}"
                )
            }
            training_data.append(entry)

    return training_data


# Generate and save training data
training_examples = generate_remote_experiment_training_data()
with open('train_remote_expt.jsonl', 'w') as f:
    for example in training_examples:
        f.write(json.dumps(example) + '\n')

print(f"Generated {len(training_examples)} training examples")
print("Training data covers:")
print("- General remote experiment questions")
print("- 4 confirmed instruments (2 SNS + 2 HFIR)")
print("- 18 uncertain SNS instruments")
print("- 10 uncertain HFIR instruments")
print("- Various question patterns for each instrument")
print("- Output in JSONL format")
print("Saved to train_remote_expt.jsonl")
