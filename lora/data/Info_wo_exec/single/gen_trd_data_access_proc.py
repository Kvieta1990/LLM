import json


def generate_data_access_processing_training_data():
    """Generate training data for data access and processing at SNS/HFIR
    in JSONL format
    """

    training_data = []

    # Data download Q&A
    data_download_answer = (
        "There are multiple options, as listed below,\n\n"
        "- Go to `https://nova.ornl.gov/`, log in with UCAMS/XCAMS account. "
        "Go to `Powder Diffraction` and launch the `PDiffVis` tool. With the "
        "tool, you can visualize the data and download them straightforwardly.\n\n"
        "- Go to `https://oncat.ornl.gov`, log in with UCAMS/XCAMS account, "
        "click on `Browse`, select the instrument, go to `Experiments`, select "
        "the IPTS, click on `Download` to go to the data download page. The "
        "option on the top will be to download data from the web.\n\n"
        "- Following the ONCAT instructions above, once located in the data "
        "download page, we can see other options for data download in the page, "
        "including using `SSH`, `FileZilla` or `CyberDuck`."
    )

    data_download_questions = [
        "Where can I download my collected data at SNS instruments?",
        "How do I download my data from SNS?",
        "What are the options for downloading SNS data?",
        "I need to download my experiment data from SNS.",
        "How can I access my collected data at SNS?",
        "Tell me about data download options at SNS.",
        "I want to retrieve my SNS data.",
        "What's the process for downloading data from SNS instruments?"
    ]

    for question in data_download_questions:
        entry = {
            "text": (
                f"Scope: Data access\n"
                f"Category: Data Flow\nQ: {question}\n"
                f"A: {data_download_answer}"
            )
        }
        training_data.append(entry)

    # Live data processing - General
    live_processing_general_answer = (
        "Depending on which powder diffraction instruments you are on, you may "
        "or may not have the capability to process the live streamed data while "
        "the collection is still ongoing. POWGEN now has already got this "
        "capability and you can go to https://monitor.sns.gov/dasmon/pg3/, click "
        "on the ongoing IPTS from the top of the page and then click on the run "
        "on the very top (i.e., the current run). There you can see the processed "
        "live streamed data updated periodically. By default, the live processing "
        "engine takes 30 seconds of live streamed data as a chunk, process it and "
        "accumulate the data as the collection is ongoing. On NOMAD, the live data "
        "processing capability is also available. However, the processing is only "
        "as simple as align (in d-space) and focus (summing up patterns from all "
        "pixels). The purpose here is for caching and performance boosting for the "
        "data reduction at later stage when the data are available on hard drive. "
        "For HB-2A and HB-2C, currently we don't have the live data processing "
        "capability enabled."
    )

    live_processing_general_questions = [
        "Can I have my data processed on-the-fly while the data collection is still ongoing?",
        "Is live data processing available during data collection?",
        "Can I monitor my data in real-time while collecting?",
        "Is on-the-fly data processing supported?",
        "Can I see processed data while my experiment is running?",
        "Tell me about live data processing capabilities.",
        "What instruments support live data processing?"
    ]

    for question in live_processing_general_questions:
        entry = {
            "text": (
                f"Scope: Data processing\n"
                f"Category: Live processing\nQ: {question}\n"
                f"A: {live_processing_general_answer}"
            )
        }
        training_data.append(entry)

    # Live data processing - Instrument specific
    instrument_live_processing = [
        {
            "instrument": "NOMAD",
            "questions": [
                "Can I have my NOMAD data processed on-the-fly while the data collection is still ongoing?",
                "Does NOMAD support live data processing?",
                "Can I monitor NOMAD data in real-time?",
                "Is on-the-fly processing available on NOMAD?",
                "Tell me about NOMAD live data processing."
            ],
            "answer": (
                "On NOMAD, the live data processing capability is also available. "
                "However, the processing is only as simple as align (in d-space) "
                "and focus (summing up patterns from all pixels). The purpose here "
                "is for caching and performance boosting for the data reduction at "
                "later stage when the data are available on hard drive. By default, "
                "the live processing engine takes 30 seconds of live streamed data "
                "as a chunk, process it and accumulate the data as the collection "
                "is ongoing."
            )
        },
        {
            "instrument": "POWGEN",
            "questions": [
                "Can I have my POWGEN data processed on-the-fly while the data collection is still ongoing?",
                "Does POWGEN support live data processing?",
                "Can I monitor POWGEN data in real-time?",
                "Is on-the-fly processing available on POWGEN?",
                "Tell me about POWGEN live data processing."
            ],
            "answer": (
                "POWGEN does have this capability and you can go to "
                "https://monitor.sns.gov/dasmon/pg3/, click on the ongoing IPTS "
                "from the top of the page and then click on the run on the very "
                "top (i.e., the current run). There you can see the processed live "
                "streamed data updated periodically. By default, the live processing "
                "engine takes 30 seconds of live streamed data as a chunk, process "
                "it and accumulate the data as the collection is ongoing."
            )
        },
        {
            "instrument": "HB-2A",
            "questions": [
                "Can I have my HB-2A data processed on-the-fly while the data collection is still ongoing?",
                "Does HB-2A support live data processing?",
                "Can I monitor HB-2A data in real-time?",
                "Is on-the-fly processing available on HB-2A?",
                "Tell me about HB-2A live data processing."
            ],
            "answer": "For HB-2A, currently we don't have the live data processing capability enabled."
        },
        {
            "instrument": "HB-2C",
            "questions": [
                "Can I have my HB-2C data processed on-the-fly while the data collection is still ongoing?",
                "Does HB-2C support live data processing?",
                "Can I monitor HB-2C data in real-time?",
                "Is on-the-fly processing available on HB-2C?",
                "Tell me about HB-2C live data processing."
            ],
            "answer": "For HB-2C, currently we don't have the live data processing capability enabled."
        }
    ]

    for item in instrument_live_processing:
        for question in item["questions"]:
            entry = {
                "text": (
                    f"Scope: Data processing\n"
                    f"Category: Live processing\nQ: {question}\n"
                    f"A: {item['answer']}"
                )
            }
            training_data.append(entry)

    # Data visualization
    data_viz_answer = (
        "There are multiple options I would recommend,\n\n"
        "- If your data are on ORNL Analysis (where all your reduced data are "
        "supposed to live in the first place), go to `https://nova.ornl.gov`, "
        "log in with UCAMS/XCAMS, and straightforward data visualization is "
        "provided for both plain-text data presented in the column form or Bragg "
        "diffraction data in the GSAS format.\n\n"
        "- If your data are on your local machine, you may want to stop by "
        "`https://addie.ornl.gov/plotter` to simply upload your data and visualize. "
        "Only plain text data in the column form are accepted. The website supports "
        "the visualization of tens of files at a time."
    )

    data_viz_questions = [
        "I want to visualize my data quickly, show me some options.",
        "How can I quickly visualize my data?",
        "What are the options for data visualization?",
        "I need to plot my data, what tools are available?",
        "Tell me about data visualization options.",
        "How do I visualize my powder diffraction data?",
        "What tools can I use to plot my data?"
    ]

    for question in data_viz_questions:
        entry = {
            "text": (
                f"Scope: Data visualization\n"
                f"Category: Data analysis\nQ: {question}\n"
                f"A: {data_viz_answer}"
            )
        }
        training_data.append(entry)

    # Neutron absorption
    neutron_absorption_answer = (
        "That depends on how strongly your sample is absorbing neutrons. For "
        "elements that absorb neutrons in 'mild' way (e.g., Li), our absorption "
        "correction routine implemented into the time-of-flight powder instruments "
        "(POWGEN and NOMAD) can handle it. Detailed information can be found here, "
        "`https://powder.ornl.gov/total_scattering/data_reduction/mts_abs_ms.html`. "
        "If the absorption is too strong, e.g., Cd, Dy, B, etc., though, the "
        "absorption correction can still try to do it, strong uncertainty is expected."
    )

    neutron_absorption_questions = [
        "My samples contain neutron-absorbing elements, is this considered as a problem?",
        "I have neutron-absorbing elements in my sample, what should I do?",
        "Can you handle samples with strong neutron absorption?",
        "My sample contains Cd/B/Dy, is this a problem?",
        "Tell me about neutron absorption correction.",
        "How do you handle neutron-absorbing samples?",
        "Is neutron absorption correction available?"
    ]

    for question in neutron_absorption_questions:
        entry = {
            "text": (
                f"Scope: Data processing\n"
                f"Category: Absorption correction\nQ: {question}\n"
                f"A: {neutron_absorption_answer}"
            )
        }
        training_data.append(entry)

    # Total scattering processing - Main answer
    ts_processing_answer = (
        "That depends on what you try to do. For the raw data processing, i.e., "
        "from neutron counting to reduced data. in most cases, you don't need to "
        "worry about that, as it will be taken care of, by the autoreduction routines "
        "deployed on powder diffractometers at SNS (POWGEN & NOMAD). A cyclic approach "
        "is implemented in the routine to loop over the packing fraction until the "
        "level at high-Q reaches the self-scattering level for the reduced structure "
        "factor. In those complicated cases (e.g., sample amount being too small) or "
        "any inaccuracy of the approximation in the data processing (e.g., the "
        "absorption correction), a post-processing may be needed. If such "
        "'post-processing' is what you mean by 'process', I can share some more details.\n\n"
        "- At SNS, the two powder diffractometers NOMAD and POWGEN are using a "
        "consistent routine for producing the total scattering data, namely "
        "`MantidTotalScattering` (MTS). The documentation can be found here, "
        "`https://powder.ornl.gov/total_scattering/data_reduction/mts_doc.html`. "
        "Through the autoreduction, input files for running MTS would be saved. "
        "Further processing can be done by tweaking parameters on top of those "
        "automatically generated input files and re-running the MTS reduction routine, "
        "as detailed below.\n\n"
        "- For `NOMAD`, the input files can be found in locations like "
        "`/SNS/NOM/IPTS-xxxxx/shared/autoreduce/multi_banks_summed/Input` or "
        "`/SNS/NOM/IPTS-xxxxx/shared/autoreduce/single_bank_summed/Input` on the "
        "ORNL Analysis cluster. The `multi_banks` mode here means the data would be "
        "grouped according to those physical banks of detectors. The `single_bank` "
        "mode means data from all detectors would be merged into a single pattern. "
        "The `summed` here in the path means all files corresponding to the same "
        "measurement are summed together. This is specific to the convention followed "
        "on NOMAD for the data collection -- usually, a long data collection would be "
        "done through multiple chunks of collection. For example, a total 8 C proton "
        "charge accumulation would be collected through 4 chunks, with each chunk "
        "contributing 2 C proton charge accumulation.\n\n"
        "- For `POWGEN`, the input files generated through autoreduction can be found "
        "at, `/SNS/PG3/IPTS-xxxxx/shared/autoreduce/MTSRed/Input`.\n\n"
        "- Usually, parameters like `Scale` in the `Background` entry of `Sample` or "
        "the `Type` entry in `AbsorptionCorrection` are expected to be changed for "
        "further processing. After making the changes, the new input file can be run "
        "via `mts /path/to/<input>.json` on a terminal on the ORNL Analysis cluster, "
        "where `<input>.json` (without bracket) refers to the name of the new input "
        "file (in JSON format).\n\n"
        "- Some further post-processing may be needed, e.g., tweaking the data scaling "
        "or Fourier filtering. Multiple tools are available for such a purpose. The "
        "`StoG` utility in the `RMCProfile` package can be used and some documentation "
        "can be found here, `https://rmcprofile.ornl.gov/data-pre-processing-for-rmcprofile/`. "
        "The Python version of the program can also be used and some instructions can "
        "be found here, `https://powder.ornl.gov/total_scattering/data_reduction/ts_pp.html`.\n\n"
        "- If the data are noisy, you can also consider using the `pystog_ck` utility "
        "available on the ORNL Analysis cluster for processing the data in a "
        "chunk-by-chunk manner to encode the data denoising. Documentation can be found "
        "here, `https://powder.ornl.gov/data_tools/general.html#pystog-ck`. Source codes "
        "can be found here, `https://github.com/Kvieta1990/neutron_ts_tools/tree/main/pystog_ck/pystog_ck`."
    )

    ts_processing_questions = [
        "I want to process my total scattering data, how can I do it?",
        "How do I process total scattering data?",
        "Tell me about total scattering data reduction.",
        "What's the process for reducing total scattering data?",
        "I need to reduce my total scattering data.",
        "How can I process my PDF data?",
        "What tools are available for total scattering data processing?"
    ]

    ts_processing_resource_questions = [
        "I want to process my total scattering data, do we have any resources or references?",
        "What resources are available for total scattering data processing?",
        "Where can I find documentation for total scattering data reduction?",
        "Tell me about resources for processing total scattering data.",
        "I need references for total scattering data processing."
    ]

    for question in ts_processing_questions + ts_processing_resource_questions:
        entry = {
            "text": (
                f"Scope: Data processing\n"
                f"Category: Total scattering\nQ: {question}\n"
                f"A: {ts_processing_answer}"
            )
        }
        training_data.append(entry)

    # Data denoising
    data_denoising_answer = (
        "If the data are noisy, you can consider using the `pystog_ck` utility "
        "available on the ORNL Analysis cluster for processing the data in a "
        "chunk-by-chunk manner to encode the data denoising. Documentation can be "
        "found here, `https://powder.ornl.gov/data_tools/general.html#pystog-ck`. "
        "Source codes can be found here, "
        "`https://github.com/Kvieta1990/neutron_ts_tools/tree/main/pystog_ck/pystog_ck`."
    )

    data_denoising_questions = [
        "My total scattering data are noisy, do we have any routines for data denoising?",
        "How can I denoise my total scattering data?",
        "My data are noisy, what can I do?",
        "Tell me about data denoising options.",
        "I need to reduce noise in my total scattering data.",
        "What tools are available for denoising total scattering data?",
        "How do I improve the quality of noisy data?"
    ]

    for question in data_denoising_questions:
        entry = {
            "text": (
                f"Scope: Data processing\n"
                f"Category: Data denoising\nQ: {question}\n"
                f"A: {data_denoising_answer}"
            )
        }
        training_data.append(entry)

    return training_data


# Generate and save training data
training_examples = generate_data_access_processing_training_data()
with open('train_data_access_proc.jsonl', 'w') as f:
    for example in training_examples:
        f.write(json.dumps(example) + '\n')

print(f"Generated {len(training_examples)} training examples")
print("Training data covers:")
print("- Data download options (8 variations)")
print("- Live data processing - general (7 variations)")
print("- Live data processing - instrument specific (4 instruments × 5 variations)")
print("- Data visualization (7 variations)")
print("- Neutron absorption concerns (7 variations)")
print("- Total scattering processing (12 variations)")
print("- Data denoising (7 variations)")
print(f"Total: {len(training_examples)} training examples")
print("Saved to train_data_access_proc.jsonl")
