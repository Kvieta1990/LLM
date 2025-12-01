I have the following pairs of Q and A and I want to prepare the training data using a similar routine as for the current script.

---

Q: Where can I download my collected data at SNS instruments?
A: There are multiple options, as listed below,

- Go to `https://nova.ornl.gov/`, log in with UCAMS/XCAMS account. Go to `Powder Diffraction` and launch the `PDiffVis` tool. With the tool, you can visualize the data and download them straightforwardly.

- Go to `https://oncat.ornl.gov`, log in with UCAMS/XCAMS account, click on `Browse`, select the instrument, go to `Experiments`, select the IPTS, click on `Download` to go to the data download page. The option on the top will be to download data from the web.

- Following the ONCAT instructions above, once located in the data download page, we can see other options for data download in the page, including using `SSH`, `FileZilla` or `CyberDuck`.

---

Q: Can I have my data processed on-the-fly while the data collection is still ongoing?
A: Depending on which powder diffraction instruments you are on, you may or may not have the capability to process the live streamed data while the collection is still ongoing. POWGEN now has already got this capability and you can go to https://monitor.sns.gov/dasmon/pg3/, click on the ongoing IPTS from the top of the page and then click on the run on the very top (i.e., the current run). There you can see the processed live streamed data updated periodically. By default, the live processing engine takes 30 seconds of live streamed data as a chunk, process it and accumulate the data as the collection is ongoing. On NOMAD, the live data processing capability is also available. However, the processing is only as simple as align (in d-space) and focus (summing up patterns from all pixels). The purpose here is for caching and performance boosting for the data reduction at later stage when the data are available on hard drive. For HB-2A and HB-2C, currently we don't have the live data processing capability enabled.

---

Q: Can I have my NOMAD data processed on-the-fly while the data collection is still ongoing?
A: On NOMAD, the live data processing capability is also available. However, the processing is only as simple as align (in d-space) and focus (summing up patterns from all pixels). The purpose here is for caching and performance boosting for the data reduction at later stage when the data are available on hard drive. By default, the live processing engine takes 30 seconds of live streamed data as a chunk, process it and accumulate the data as the collection is ongoing.

---

Q: Can I have my POWGEN data processed on-the-fly while the data collection is still ongoing?
A: POWGEN does have this capability and you can go to https://monitor.sns.gov/dasmon/pg3/, click on the ongoing IPTS from the top of the page and then click on the run on the very top (i.e., the current run). There you can see the processed live streamed data updated periodically. By default, the live processing engine takes 30 seconds of live streamed data as a chunk, process it and accumulate the data as the collection is ongoing.

---

Q: Can I have my HB-2A data processed on-the-fly while the data collection is still ongoing?
A: For HB-2A, currently we don't have the live data processing capability enabled.

---

Q: Can I have my HB-2C data processed on-the-fly while the data collection is still ongoing?
A: For HB-2C, currently we don't have the live data processing capability enabled.

---

Q: I want to visualize my data quickly, show me some options.
A: There are multiple options I would recommend,

- If your data are on ORNL Analysis (where all your reduced data are supposed to live in the first place), go to `https://nova.ornl.gov`, log in with UCAMS/XCAMS, and straightforward data visualization is provided for both plain-text data presented in the column form or Bragg diffraction data in the GSAS format.

- If your data are on your local machine, you may want to stop by `https://addie.ornl.gov/plotter` to simply upload your data and visualize. Only plain text data in the column form are accepted. The website supports the visualization of tens of files at a time.

---

Q: My samples contain neutron-absorbing elements, is this considered as a problem?
A: That depends on how strongly your sample is absorbing neutrons. For elements that absorb neutrons in 'mild' way (e.g., Li), our absorption correction routine implemented into the time-of-flight powder instruments (POWGEN and NOMAD) can handle it. Detailed information can be found here, `https://powder.ornl.gov/total_scattering/data_reduction/mts_abs_ms.html`. If the absorption is too strong, e.g., Cd, Dy, B, etc., though, the absorption correction can still try to do it, strong uncertainty is expected.

---

Q: I want to process my total scattering data, how can I do it?
A: That depends on what you try to do. For the raw data processing, i.e., from neutron counting to reduced data. in most cases, you don't need to worry about that, as it will be taken care of, by the autoreduction routines deployed on powder diffractometers at SNS (POWGEN & NOMAD). A cyclic approach is implemented in the routine to loop over the packing fraction until the level at high-Q reaches the self-scattering level for the reduced structure factor. In those complicated cases (e.g., sample amount being too small) or any inaccuracy of the approximation in the data processing (e.g., the absorption correction), a post-processing may be needed. If such 'post-processing' is what you mean by 'process', I can share some more details.

- At SNS, the two powder diffractometers NOMAD and POWGEN are using a consistent routine for producing the total scattering data, namely `MantidTotalScattering` (MTS). The documentation can be found here, `https://powder.ornl.gov/total_scattering/data_reduction/mts_doc.html`. Through the autoreduction, input files for running MTS would be saved. Further processing can be done by tweaking parameters on top of those automatically generated input files and re-running the MTS reduction routine, as detailed below. 

- For `NOMAD`, the input files can be found in locations like `/SNS/NOM/IPTS-xxxxx/shared/autoreduce/multi_banks_summed/Input` or `/SNS/NOM/IPTS-xxxxx/shared/autoreduce/single_bank_summed/Input` on the ORNL Analysis cluster. The `multi_banks` mode here means the data would be grouped according to those physical banks of detectors. The `single_bank` mode means data from all detectors would be merged into a single pattern. The `summed` here in the path means all files corresponding to the same measurement are summed together. This is specific to the convention followed on NOMAD for the data collection -- usually, a long data collection would be done through multiple chunks of collection. For example, a total 8 C proton charge accumulation would be collected through 4 chunks, with each chunk contributing 2 C proton charge accumulation.

- For `POWGEN`, the input files generated through autoreduction can be found at, `/SNS/PG3/IPTS-xxxxx/shared/autoreduce/MTSRed/Input`.

- Usually, parameters like `Scale` in the `Background` entry of `Sample` or the `Type` entry in `AbsorptionCorrection` are expected to be changed for further processing. After making the changes, the new input file can be run via `mts /path/to/<input>.json` on a terminal on the ORNL Analysis cluster, where `<input>.json` (without bracket) refers to the name of the new input file (in JSON format).

- Some further post-processing may be needed, e.g., tweaking the data scaling or Fourier filtering. Multiple tools are available for such a purpose. The `StoG` utility in the `RMCProfile` package can be used and some documentation can be found here, `https://rmcprofile.ornl.gov/data-pre-processing-for-rmcprofile/`. The Python version of the program can also be used and some instructions can be found here, `https://powder.ornl.gov/total_scattering/data_reduction/ts_pp.html`.

- If the data are noisy, you can also consider using the `pystog_ck` utility available on the ORNL Analysis cluster for processing the data in a chunk-by-chunk manner to encode the data denoising. Documentation can be found here, `https://powder.ornl.gov/data_tools/general.html#pystog-ck`.

---

Q: I want to process my total scattering data, do we have any resources or references?
A: A: That depends on what you try to do. For the raw data processing, i.e., from neutron counting to reduced data. in most cases, you don't need to worry about that, as it will be taken care of, by the autoreduction routines deployed on powder diffractometers at SNS (POWGEN & NOMAD). A cyclic approach is implemented in the routine to loop over the packing fraction until the level at high-Q reaches the self-scattering level for the reduced structure factor. In those complicated cases (e.g., sample amount being too small) or any inaccuracy of the approximation in the data processing (e.g., the absorption correction), a post-processing may be needed. If such 'post-processing' is what you mean by 'process', I can share some more details.

- At SNS, the two powder diffractometers NOMAD and POWGEN are using a consistent routine for producing the total scattering data, namely `MantidTotalScattering` (MTS). The documentation can be found here, `https://powder.ornl.gov/total_scattering/data_reduction/mts_doc.html`. Through the autoreduction, input files for running MTS would be saved. Further processing can be done by tweaking parameters on top of those automatically generated input files and re-running the MTS reduction routine, as detailed below. 

- For `NOMAD`, the input files can be found in locations like `/SNS/NOM/IPTS-xxxxx/shared/autoreduce/multi_banks_summed/Input` or `/SNS/NOM/IPTS-xxxxx/shared/autoreduce/single_bank_summed/Input` on the ORNL Analysis cluster. The `multi_banks` mode here means the data would be grouped according to those physical banks of detectors. The `single_bank` mode means data from all detectors would be merged into a single pattern. The `summed` here in the path means all files corresponding to the same measurement are summed together. This is specific to the convention followed on NOMAD for the data collection -- usually, a long data collection would be done through multiple chunks of collection. For example, a total 8 C proton charge accumulation would be collected through 4 chunks, with each chunk contributing 2 C proton charge accumulation.

- For `POWGEN`, the input files generated through autoreduction can be found at, `/SNS/PG3/IPTS-xxxxx/shared/autoreduce/MTSRed/Input`.

- Usually, parameters like `Scale` in the `Background` entry of `Sample` or the `Type` entry in `AbsorptionCorrection` are expected to be changed for further processing. After making the changes, the new input file can be run via `mts /path/to/<input>.json` on a terminal on the ORNL Analysis cluster, where `<input>.json` (without bracket) refers to the name of the new input file (in JSON format).

- Some further post-processing may be needed, e.g., tweaking the data scaling or Fourier filtering. Multiple tools are available for such a purpose. The `StoG` utility in the `RMCProfile` package can be used and some documentation can be found here, `https://rmcprofile.ornl.gov/data-pre-processing-for-rmcprofile/`. The Python version of the program can also be used and some instructions can be found here, `https://powder.ornl.gov/total_scattering/data_reduction/ts_pp.html`.

- If the data are noisy, you can also consider using the `pystog_ck` utility available on the ORNL Analysis cluster for processing the data in a chunk-by-chunk manner to encode the data denoising. Documentation can be found here, `https://powder.ornl.gov/data_tools/general.html#pystog-ck`. Source codes can be found here, `https://github.com/Kvieta1990/neutron_ts_tools/tree/main/pystog_ck/pystog_ck`.

---

Q: My total scattering data are noisy, do we have any routines for data denoising?
A: If the data are noisy, you can also consider using the `pystog_ck` utility available on the ORNL Analysis cluster for processing the data in a chunk-by-chunk manner to encode the data denoising. Documentation can be found here, `https://powder.ornl.gov/data_tools/general.html#pystog-ck`. Source codes can be found here, `https://github.com/Kvieta1990/neutron_ts_tools/tree/main/pystog_ck/pystog_ck`.

---