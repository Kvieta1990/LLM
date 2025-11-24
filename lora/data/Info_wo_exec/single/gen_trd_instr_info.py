import json


def generate_instrument_selection_training_data():
    """Generate training data for instrument selection and specifications
    in JSONL format
    """

    training_data = []

    # Instrument selection Q&A pairs
    instrument_selection = [
        {
            "questions": [
                "I want to measure high resolution Bragg diffraction pattern, which instruments at ORNL should I choose?",
                "Which ORNL instruments are best for high resolution Bragg diffraction?",
                "What are the high resolution Bragg diffraction options at ORNL?",
                "I need to do high resolution Bragg diffraction, which ORNL beamline should I use?",
                "Recommend an ORNL instrument for high resolution Bragg diffraction measurements."
            ],
            "answer": "ORNL hosts several high resolution Bragg diffractometers, including both those constant wavelength (CW) and time-of-flight beamlimes. HB-2A (Powder) or HB-2C (WAND^2) are options at HFIR, and POWGEN is the option at SNS."
        },
        {
            "questions": [
                "I want to measure total scattering data, which instruments at ORNL should I choose?",
                "Which ORNL instruments can measure total scattering?",
                "What are my options for total scattering measurements at ORNL?",
                "I need to collect total scattering data at ORNL, which instrument?",
                "Recommend an ORNL beamline for total scattering experiments."
            ],
            "answer": "NOMAD and POWGEN at SNS can be used for taking the total scattering measurements. NOMAD is with higher flux so the amount of samples required is less than that for POWGEN. For example, a quartz capillary with the diameter of 3 mm can be used on NOMAD for holding samples in some sample environment but such a small sample container is not supported on POWGEN. If magnetic PDF is to be measured, HB-2A at HFIR can also be considered."
        },
        {
            "questions": [
                "I want to measure pair distribution function, which instruments at ORNL should I choose?",
                "Which ORNL instruments are suitable for PDF measurements?",
                "What are the pair distribution function measurement options at ORNL?",
                "I need to measure PDF at ORNL, which beamline should I use?",
                "Recommend an instrument for pair distribution function analysis at ORNL."
            ],
            "answer": "NOMAD and POWGEN at SNS can be used for taking the pair distribution function (PDF) measurements. NOMAD is with higher flux so the amount of samples required is less than that for POWGEN. For example, a quartz capillary with the diameter of 3 mm can be used on NOMAD for holding samples in some sample environment but such a small sample container is not supported on POWGEN. If magnetic PDF is to be measured, HB-2A at HFIR can also be considered."
        },
        {
            "questions": [
                "I want to measure PDF, which instruments at ORNL should I choose?",
                "Which ORNL instruments can do PDF?",
                "PDF measurements at ORNL - which instrument?",
                "I need PDF data from ORNL, where should I go?",
                "Best ORNL beamline for PDF experiments?"
            ],
            "answer": "NOMAD and POWGEN at SNS can be used for taking the total scattering measurements. NOMAD is with higher flux so the amount of samples required is less than that for POWGEN. For example, a quartz capillary with the diameter of 3 mm can be used on NOMAD for holding samples in some sample environment but such a small sample container is not supported on POWGEN. If magnetic PDF is to be measured, HB-2A at HFIR can also be considered."
        },
        {
            "questions": [
                "I want to measure magnetic PDF, which instruments at ORNL should I choose?",
                "Which ORNL instruments are available for magnetic PDF measurements?",
                "What are my options for magnetic pair distribution function at ORNL?",
                "I need to measure magnetic PDF, which ORNL beamline?",
                "Recommend an instrument for magnetic PDF experiments at ORNL."
            ],
            "answer": "NOMAD and POWGEN at SNS can be used for taking the magnetic PDF measurements. NOMAD is with higher flux so the amount of samples required is less than that for POWGEN. For example, a quartz capillary with the diameter of 3 mm can be used on NOMAD for holding samples in some sample environment but such a small sample container is not supported on POWGEN. HB-2A at HFIR can also be considered for the magnetic PDF measurements."
        },
        {
            "questions": [
                "I want to measure magnetic pair distribution function, which instruments at ORNL should I choose?",
                "Which ORNL instruments can measure magnetic pair distribution function?",
                "What are the options for magnetic pair distribution function measurements at ORNL?",
                "I need magnetic pair distribution function data, which ORNL instrument?",
                "Best beamline at ORNL for magnetic pair distribution function?"
            ],
            "answer": "NOMAD and POWGEN at SNS can be used for taking the magnetic PDF measurements. NOMAD is with higher flux so the amount of samples required is less than that for POWGEN. For example, a quartz capillary with the diameter of 3 mm can be used on NOMAD for holding samples in some sample environment but such a small sample container is not supported on POWGEN. HB-2A at HFIR can also be considered for the magnetic PDF measurements."
        }
    ]

    # Sample container Q&A pairs
    sample_containers = [
        {
            "questions": [
                "What sample containers are commonly used on NOMAD?",
                "What types of sample holders does NOMAD use?",
                "Tell me about NOMAD sample containers.",
                "What containers can I use for my NOMAD experiment?",
                "Sample container options for NOMAD?"
            ],
            "answer": "On NOMAD, there are two typical containers that are commonly used. For low background sample environments such as the `shifter`, a quartz capillary with the diameter of 3 mm or a PAC can (made of vanadium) with the diameter of 6 mm can be used. The PAC can with the diameter of 8 mm can also be used but may not be that often. For high background sample environments such as furnace (for high temperature) and cryostat (for low temperature), only PAC cans are used. For an optimal data collection, we should have the sample filling about 2 cm height in the container to fully take advantage of the full beam exposure."
        },
        {
            "questions": [
                "What sample containers are commonly used on POWGEN?",
                "What types of sample holders does POWGEN use?",
                "Tell me about POWGEN sample containers.",
                "What containers can I use for my POWGEN experiment?",
                "Sample container options for POWGEN?"
            ],
            "answer": "On POWGEN, there are three types of containers that are commonly used, namely the PAC can (made of vanadium) with the diameter of 6 mm, 8 mm and 10 mm. For an optimal data collection, we should have the sample filling about 4-5 cm height in the container to fully take advantage of the full beam exposure."
        },
        {
            "questions": [
                "What sample containers are commonly used on HB-2A?",
                "What types of sample holders does HB-2A use?",
                "Tell me about HB-2A sample containers.",
                "What containers can I use for my HB-2A experiment?",
                "Sample container options for HB-2A?"
            ],
            "answer": "On HB-2A, quite a few types of containers are available, including those Au and Cu standard cans, Al and Cu Tip-Top cans and vanadium standard cans. Specification of container sizes can be found here, https://neutrons.ornl.gov/powder/users. There is a tool on ADDIE web platform (https://addie.ornl.gov/hb2a_can_sel) for helping users with the container selection."
        },
        {
            "questions": [
                "What sample containers are commonly used on HB-2C?",
                "What types of sample holders does HB-2C use?",
                "Tell me about HB-2C sample containers.",
                "What containers can I use for my HB-2C experiment?",
                "Sample container options for HB-2C?"
            ],
            "answer": "On HB-2C, both Al and vanadium cans are available. For Al cans, available options of diameter are 4 mm, 6 mm, 8 mm and 10 mm. For vanadium cans, available options of diameter are 3 mm, 6 mm, 8 mm and 10 mm. The beam height is about 5 cm and optimally we want to fill the can to similar height to take the full advantage of the full beam exposure. One can get a feel about how much samples are needed according to the size specification here."
        }
    ]

    # Sample amount Q&A pairs
    sample_amounts = [
        {
            "questions": [
                "How much sample do we need for a reasonable NOMAD measurement?",
                "What is the minimum sample amount for NOMAD?",
                "How much material is required for a NOMAD experiment?",
                "Sample quantity needed for NOMAD measurements?",
                "What sample volume do I need for NOMAD?"
            ],
            "answer": "On NOMAD, there are two typical containers that are commonly used. For low background sample environments such as the `shifter`, a quartz capillary with the diameter of 3 mm or a PAC can (made of vanadium) with the diameter of 6 mm can be used. The PAC can with the diameter of 8 mm can also be used but may not be that often. For high background sample environments such as furnace (for high temperature) and cryostat (for low temperature), only PAC cans are used. For an optimal data collection, we should have the sample filling about 2 cm height in the container to fully take advantage of the full beam exposure. One can get a feel about the amount of samples needed for a typical measurement on NOMAD according to the size specification. Small amount of samples is doable but that is a case-by-case decision (depending on, e.g., how strongly the sample scatters neutrons), or the measurement will be considered as proof-of-principle only."
        },
        {
            "questions": [
                "How much sample do we need for a reasonable POWGEN measurement?",
                "What is the minimum sample amount for POWGEN?",
                "How much material is required for a POWGEN experiment?",
                "Sample quantity needed for POWGEN measurements?",
                "What sample volume do I need for POWGEN?"
            ],
            "answer": "On POWGEN, there are three types of containers that are commonly used, namely the PAC can (made of vanadium) with the diameter of 6 mm, 8 mm and 10 mm. For an optimal data collection, we should have the sample filling about 4-5 cm height in the container to fully take advantage of the full beam exposure. One can get a feel about the amount of samples needed for a typical measurement on NOMAD according to the size specification."
        },
        {
            "questions": [
                "How much sample do we need for a reasonable HB-2A measurement?",
                "What is the minimum sample amount for HB-2A?",
                "How much material is required for an HB-2A experiment?",
                "Sample quantity needed for HB-2A measurements?",
                "What sample volume do I need for HB-2A?"
            ],
            "answer": "On HB-2A, quite a few types of containers are available, including those Au and Cu standard cans, Al and Cu Tip-Top cans and vanadium standard cans. Specification of container sizes can be found here, https://neutrons.ornl.gov/powder/users. There is a tool on ADDIE web platform (https://addie.ornl.gov/hb2a_can_sel) for helping you with the container selection, depending on how much sample you have for the measurement."
        },
        {
            "questions": [
                "How much sample do we need for a reasonable HB-2C measurement?",
                "What is the minimum sample amount for HB-2C?",
                "How much material is required for an HB-2C experiment?",
                "Sample quantity needed for HB-2C measurements?",
                "What sample volume do I need for HB-2C?"
            ],
            "answer": "On HB-2C, both Al and vanadium cans are available. For Al cans, available options of diameter are 4 mm, 6 mm, 8 mm and 10 mm. For vanadium cans, available options of diameter are 3 mm, 6 mm, 8 mm and 10 mm. The beam height is about 5 cm and optimally we want to fill the can to similar height to take the full advantage of the full beam exposure. One can get a feel about how much samples are needed according to the size specification here."
        }
    ]

    # Instrument specification Q&A pairs
    instrument_specs = [
        {
            "instrument": "HB-2C",
            "questions": [
                "Where can I learn the instrument specification about HB-2C?",
                "Where can I find HB-2C instrument information?",
                "Tell me about HB-2C specifications and capabilities.",
                "Where is the HB-2C user guide?",
                "I need information about the HB-2C instrument."
            ],
            "general_info": "https://neutrons.ornl.gov/wand",
            "capabilities": "https://neutrons.ornl.gov/wand/capabilities",
            "user_guide": "https://neutrons.ornl.gov/wand/users"
        },
        {
            "instrument": "NOMAD",
            "questions": [
                "Where can I learn the instrument specification about NOMAD?",
                "Where can I find NOMAD instrument information?",
                "Tell me about NOMAD specifications and capabilities.",
                "Where is the NOMAD user guide?",
                "I need information about the NOMAD instrument."
            ],
            "general_info": "https://neutrons.ornl.gov/nomad",
            "capabilities": "https://neutrons.ornl.gov/nomad/science",
            "user_guide": "https://neutrons.ornl.gov/nomad/users"
        },
        {
            "instrument": "POWGEN",
            "questions": [
                "Where can I learn the instrument specification about POWGEN?",
                "Where can I find POWGEN instrument information?",
                "Tell me about POWGEN specifications and capabilities.",
                "Where is the POWGEN user guide?",
                "I need information about the POWGEN instrument."
            ],
            "general_info": "https://neutrons.ornl.gov/powgen",
            "capabilities": "https://neutrons.ornl.gov/powgen/publications",
            "user_guide": "https://neutrons.ornl.gov/powgen/users"
        },
        {
            "instrument": "HB-2A",
            "questions": [
                "Where can I learn the instrument specification about HB-2A?",
                "Where can I find HB-2A instrument information?",
                "Tell me about HB-2A specifications and capabilities.",
                "Where is the HB-2A user guide?",
                "I need information about the HB-2A instrument."
            ],
            "general_info": "https://neutrons.ornl.gov/powder",
            "capabilities": "https://neutrons.ornl.gov/powder/capabilities & https://neutrons.ornl.gov/powder/highlights",
            "user_guide": "https://neutrons.ornl.gov/powder/users"
        }
    ]

    # Generate training data for instrument selection
    for item in instrument_selection:
        for question in item["questions"]:
            entry = {
                "text": (
                    f"Scope: Instrument selection\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {item['answer']}"
                )
            }
            training_data.append(entry)

    # Generate training data for sample containers
    for item in sample_containers:
        for question in item["questions"]:
            entry = {
                "text": (
                    f"Scope: Sample preparation\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {item['answer']}"
                )
            }
            training_data.append(entry)

    # Generate training data for sample amounts
    for item in sample_amounts:
        for question in item["questions"]:
            entry = {
                "text": (
                    f"Scope: Sample preparation\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {item['answer']}"
                )
            }
            training_data.append(entry)

    # Generate training data for instrument specifications
    for item in instrument_specs:
        for question in item["questions"]:
            answer = (
                f"The general instrument information for {item['instrument']} can be found here, "
                f"{item['general_info']}. Specifically, showcases of capabilities can be found here, "
                f"{item['capabilities']}. User guidance about sample preparation, instrument control "
                f"and data access can be found here, {item['user_guide']}."
            )
            entry = {
                "text": (
                    f"Scope: Instrument information\n"
                    f"Category: Experimentation\nQ: {question}\n"
                    f"A: {answer}"
                )
            }
            training_data.append(entry)

    return training_data


# Generate and save training data
training_examples = generate_instrument_selection_training_data()
with open('train_instr_info.jsonl', 'w') as f:
    for example in training_examples:
        f.write(json.dumps(example) + '\n')

print(f"Generated {len(training_examples)} training examples")
print("Training data covers:")
print("- Instrument selection questions (6 topics × 5 variations)")
print("- Sample container questions (4 instruments × 5 variations)")
print("- Sample amount questions (4 instruments × 5 variations)")
print("- Instrument specification questions (4 instruments × 5 variations)")
print(f"Total: {len(training_examples)} training examples")
print("Saved to train_instr_info.jsonl")
