Data Type & Analysis Selection
==============================

This section should describe the type of input data the computational procedure is designed to handle and validated to process. Explain how the data determines the choice of analysis methods, tools, and parameters used within the procedure.

What to Include:

- **Data Format:** Specify the format(s) of input data (e.g. FASTQ, BAM, VCF), sequencing technology (e.g. Illumina, Oxford Nanopore, PacBio), and any relevant characteristics (e.g. read length, paired-end vs single-end).

- **Sample suitability:** Describe the types of samples or organisms the data is expected to represent (e.g. human clinical samples, bacterial isolates, viral genomes).

- **Analysis Selection:** Describe how the data type influences the selection of analysis tools, algorithms, and parameters. For example, certain variant callers may be optimised for short reads versus long reads.

-----

.. admonition:: Example – HIV Antiviral Resistance Pipeline
   :class: tip

   This procedure is designed to process 150bp paired-end FASTQ files generated using the Illumina NextSeq platform. Each sample should have two FASTQ files (.fastq or .fastq.gz) representing the forward and reverse reads.

   The pipeline is specifically optimised and validated to process this data type and read length. Samples generated using other sequencing technologies (e.g. Oxford Nanopore, PacBio) or read lengths are not validated for analysis using this procedure.
   
   The input data should represent clinical HIV samples derived from patient plasma.

   The choice of analysis tools and parameters is optimised for the specified data type. For example, the read mapper is configured to handle the high mutation rate of HIV, and variant calling thresholds are set to detect low-frequency resistance mutations typical in viral populations. Long-read data from Oxford Nanopore or PacBio platforms are not supported by this procedure due to differences in error profiles and read characteristics.
