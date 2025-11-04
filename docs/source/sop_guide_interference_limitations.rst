Interferences & Limitations
===========================

Describe known interferences, limitations, and potential sources of error that may impact the performance or accuracy of the procedure. Understanding these factors is crucial for interpreting results correctly and ensuring reliable operation.

What to Include:

- **Detection Limits:** Specify the sensitivity and specificity of the procedure, including any known limits of detection for relevant targets (e.g. minimum variant allele frequency, coverage depth).
- **Interfering Substances or Conditions:** Describe any substances, sample types, or conditions that may interfere with the analysis (e.g. contaminants, mixed infections, low-quality input data).
- **Software dependencies:** Note any software tools or versions that may introduce limitations or compatibility issues.
- **Scope of Validation:** Clarify the contexts in which the procedure has been validated.

-----

.. admonition:: Example – HIV Antiviral Resistance Pipeline
   :class: tip

   The procedure is validated to detect HIV drug resistance mutations present at a minimum variant allele frequency of 5% in samples with a minimum sequencing coverage depth of 100x across the pol gene region. Variants below this threshold may not be reliably detected.

   Samples with significant contamination (e.g. bacterial DNA, human genomic DNA) or mixed infections may yield inaccurate results due to interference with read mapping and variant calling. It is recommended to assess sample purity prior to analysis.

   The pipeline relies on specific versions of software tools (e.g. BWA v0.7.17, FreeBayes v1.3.2). Using incompatible versions may lead to unexpected behaviour or errors.

   This procedure has been validated for Illumina-generated paired-end FASTQ data from clinical HIV samples. It is not validated for other sequencing platforms (e.g. Oxford Nanopore, PacBio) or sample types (e.g. environmental samples).