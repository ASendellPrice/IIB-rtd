Glossary of ISO terms
=====================

Here you will find definitions for common ISO 15189-related terms.

.. dropdown:: Acceptability criteria 

   Predefined specifications or limits used to determine whether a result, process, or product is considered fit for purpose. Must be documented before testing, e.g., control values must fall within a certain range, PCR efficiency must meet specified thresholds.

   **Example usage:**  
   Acceptability criteria for the qPCR assay required that positive control Ct values fall within ±1.0 of the established mean and that the negative control showed no amplification before results were approved.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Predefined quality control (QC) or performance thresholds applied to sequencing data and pipelines. Examples include minimum read quality (e.g., Phred ≥ 30), acceptable mapping/alignment rate (e.g., ≥ 90%), and validated benchmark performance (e.g., sensitivity, specificity, and PPV for variant calling). May also cover reproducibility and runtime expectations for bioinformatics workflows.

      **Example usage:**  
      *“Acceptability criteria required that at least 90% of exome target bases achieved a minimum coverage of 20×”*

.. dropdown:: Accreditation

   Formal recognition by an authoritative body that a laboratory or organisation is competent to perform specific tests or activities in accordance with established standards (e.g., ISO 15189).

   **Example usage:**  
   The laboratory received ISO 15189 accreditation for molecular diagnostics, confirming it met all requirements for quality management, personnel competence, and technical performance.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition.

      **Example usage:**  
      *“See wetlab example.”*

.. dropdown:: Adequacy

   Suitability of resources, processes, or systems to achieve intended objectives. In ISO 15189, adequacy is judged against documented requirements.

   **Example usage:**  
   The adequacy of the PCR thermocycler and reagents was verified to ensure accurate amplification across all samples.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, adequacy refers to whether computational infrastructure (e.g., storage, CPU/GPU resources), methods, pipelines, and reference datasets are sufficient to perform analyses reliably and accurately. For example, assessing whether available compute resources can handle whole-genome sequencing data or whether reference databases are comprehensive enough to detect updated resistance mutations.

      **Example usage:**  
      *“The reference genome and variant database were reviewed for adequacy to ensure they included updated known resistance mutations in pathogen datasets, enabling accurate detection and reporting.”*

.. dropdown:: Authorisation

   Official permission granted by a competent person or authority to perform a specific activity, release results, or operate equipment in accordance with established procedures.

   **Example usage:**  
   The clinical scientist provided authorisation to release patient RNA-seq results after verifying QC metrics and reviewing the final report.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      nan

      **Example usage:**  
      *“nan”*

.. dropdown:: Calibration (Calibration Requirements)

   Operation establishing the relationship between instrument indications and reference standards (ISO VIM). Calibration ensures that measurements are accurate, traceable, and reliable.

   **Example usage:**  
   Calibration of the qPCR instrument was performed using standard reference materials to ensure accurate viral load quantification.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, calibration focuses on benchmarking algorithms or tools against reference datasets rather than hardware. Examples include calibrating variant quality scores, adjusting machine-learning thresholds, or normalizing QC metrics using gold-standard datasets to ensure accurate and reliable results.

      **Example usage:**  
      *“Calibration of the variant quality score model was performed using Genome in a Bottle reference calls to ensure accurate variant classification.”*

.. dropdown:: Change Control

   A formal process within the Quality Management System (QMS) for managing modifications to documents, procedures, equipment, or systems. It ensures that any changes are reviewed, approved, implemented, and documented in a controlled manner to maintain quality and compliance.

   **Example usage:**  
   Missing

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      The formal management of changes to computational workflows, analysis pipelines, software tools, reference genomes, or databases. Change control ensures that updates are systematically reviewed, validated, approved, and documented before implementation, to prevent unintended impact on results and maintain reproducibility.

      **Example usage:**  
      *“Change control was required when updating the reference genome for Mycobacterium tuberculosis to a new version, ensuring that the updated reference, pipeline re-validation, and impact on drug-resistance mutation reporting were fully documented before implementation.”*

.. dropdown:: Change Request (Document Control)

   A formal request submitted to modify a controlled document (e.g., SOP, validation protocol). Change requests must include justification, details of the proposed modification, and undergo review and approval before implementation. All approved change requests must be recorded in the Quality Management System (QMS).

   **Example usage:**  
   A change request was submitted to update the DNA extraction SOP to use a new extraction kit

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“A change request was submitted to update the server IP address specified in the SOP following a change in the server configuration.”*

.. dropdown:: Checklists (under Audits)

   Structured tools used to verify compliance with requirements, procedures, or standards during audits. Checklists help ensure that all critical elements are reviewed consistently.

   **Example usage:**  
   A checklist was used during the internal audit to confirm that sample labeling, reagent storage, and instrument maintenance complied with SOPs.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“During pipeline audits, a checklist ensured that software versions, reference databases, QC metrics, and documentation were reviewed for compliance with quality standards.”*

.. dropdown:: Clinical Accuracy

   Degree to which test results correctly reflect the clinical status of the patient (ISO 15197, CLSI). Clinical accuracy goes beyond analytical correctness to measure how well results correspond to actual patient condition.

   **Example usage:**  
   Clinical accuracy of the HIV viral load assay was confirmed by comparing measured values with patient outcomes and treatment response

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, clinical accuracy applies to diagnostic pipelines, ensuring that results reflect true patient status—for example, detecting a pathogen in sequencing data corresponds to an actual infection. It evaluates the clinical relevance of bioinformatics analyses beyond analytical performance metrics.

      **Example usage:**  
      *“Clinical accuracy of the TB genomics pipeline was confirmed by comparing detected Mycobacterium tuberculosis sequences and resistance markers with patient microbiology results, ensuring reported variants reflected true infection and drug resistance status.”*

.. dropdown:: Clinical Decision Limits

   Predefined values of a biomarker or measurement used for clinical decision-making (ISO 15189).

   **Example usage:**  
   A clinical decision limit of 20 copies/mL, corresponding to the assay’s lower limit of quantitation, was applied for reporting HIV viral load; results below this threshold were reported as “detected but not quantifiable.”

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, clinical decision limits are predefined thresholds applied to computational results—such as variant allele frequencies, read depths, or genome assembly metrics—to guide reporting and clinical interpretation. Variants or signals below these limits are not reported because they cannot be reliably distinguished from errors or background noise.

      **Example usage:**  
      *“A clinical decision limit was applied to variant allele frequencies, where only variants present above 20% were reported, as lower-frequency variants could not be reliably distinguished from sequencing or pipeline errors.”*

.. dropdown:: Commutability

   Property of a reference material to behave like patient samples across different measurement procedures, ensuring that results are comparable and meaningful.

   **Example usage:**  
   Reference plasma samples showed commutability by producing results consistent with patient specimens across multiple viral load assays.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, commutability refers to whether reference datasets behave comparably to real patient samples across analysis pipelines. For example, synthetic spike-ins were assessed for commutability to ensure they accurately mimicked biological variability.

      **Example usage:**  
      *“The synthetic reference dataset lacked commutability and did not represent patient sample variability, highlighting limitations for benchmarking variant detection pipelines.”*

.. dropdown:: Comparability

   Ability to compare results across different laboratories, methods, or time points, within defined limits of agreement. Ensures that measurements are consistent and interpretable in different contexts.

   **Example usage:**  
   Comparability of viral load results was confirmed by re-analyzing the same patient samples in three independent laboratories using the same SOPs.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, comparability refers to ensuring that results from different pipelines, datasets, or centres can be aligned and interpreted consistently. This is achieved through standardized data formats, shared reference datasets, harmonized QC metrics, and agreed cut-offs or settings for computational tools.

      **Example usage:**  
      *“Comparability of variant calling results across three sequencing centres was ensured by using shared reference datasets, harmonized QC metrics, and agreed tool settings and cut-offs”*

.. dropdown:: Competence 

   Demonstrated ability to apply knowledge, skills, and experience to achieve intended results (ISO/IEC 17025:2017; ISO 15189:2022). Includes performing assays, maintaining instruments, following SOPs and safety/QC protocols, and executing analyses with awareness of limitations. Competence must be documented and maintained, e.g., through training records, competency assessments, DOPs, and competency profiles (see competence record).

   **Example usage:**  
   Laboratory staff demonstrated competence by planning and performing PCR assays, conducting QC checks, operating instruments correctly, and interpreting results while adhering to SOPs and acknowledging assay limitations.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, competence is the ability to design, execute, and interpret analyses—such as quality control, pipeline selection, statistical testing, and data interpretation—while understanding the limitations of the tools, datasets, and methods used.

      **Example usage:**  
      *“Competence was demonstrated by designing a new pathogen genomics pipeline to meet clinical requirements, selecting appropriate analysis tools, performing QC checks, and interpreting results while considering the limitations of datasets and algorithms.”*

.. dropdown:: Competence record

   Demonstrated ability to apply knowledge, skills, and experience to achieve intended results (ISO/IEC 17025:2017; ISO 15189:2022). Includes performing assays, maintaining instruments, following SOPs and safety/QC protocols, and executing analyses with awareness of limitations. Competence must be documented and maintained, e.g., through training records, competency assessments, direct observation of procedures (DOPs), and competency profiles.

   **Example usage:**  
   Laboratory staff competence was demonstrated through DOPs and competency profiles, showing accurate execution of laboratory procedures—including extraction, library preparation, and assay setup—proper instrument maintenance, adherence to SOPs, and compliance with safety and QC protocols.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, competence is the demonstrated ability to apply knowledge, skills, and experience to achieve intended results in computational analyses. This includes designing and executing analyses, developing and running pipelines, managing software, reference datasets, and computing infrastructure (hardware and storage), performing quality control checks, and interpreting results with awareness of the limitations of tools, methods, and datasets. Competence must be documented and maintained, e.g., through training records, competency assessments, direct observation of procedures (DOPs), and competency profiles.

      **Example usage:**  
      *“Competence in bioinformatics was demonstrated by the ability to perform routine computational tasks—including pipeline execution, data preprocessing, QC checks, and result interpretation—while managing software, reference datasets, and computing infrastructure, as assessed through documented observation of procedures (DOPs), competency profiles, and formal training records.”*

.. dropdown:: Consensus Data

   Results agreed upon by multiple experts, methods, or laboratories, often serving as a benchmark. In ISO, consensus data underpin reference values or validation and must be determined systematically.

   **Example usage:**  
   Consensus data from three independent laboratories were used to establish the reference range for viral load measurements.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, consensus data can be a gold-standard variant set derived from multiple pipelines or jointly curated annotations, used to validate new methods or resolve ambiguous results. For example, the Genome in a Bottle (GIAB) variant set serves as consensus data for benchmarking human variant-calling pipelines.

      **Example usage:**  
      *“The TB variant-calling pipeline was benchmarked against a consensus dataset compiled from multiple sequencing centers to ensure accuracy and reproducibility of detected resistance mutations.”*

.. dropdown:: Contamination 

   Unintended presence of material, organism, or signal that compromises results.

   **Example usage:**  
   Contamination was detected when non-template controls showed higher-than-expected read counts, indicating cross-sample contamination during nucleic acid extraction.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, contamination refers to unwanted reads, cross-sample index misassignments, or sequences from off-target organisms that can affect analysis.

      **Example usage:**  
      *“Contamination was detected when off-target pathogen reads, such as influenza sequences, appeared in SARS-CoV-2 samples, indicating cross-sample contamination.”*

.. dropdown:: Controls (Positive / Negative)

   Specimens with known characteristics used to verify that a test, assay, or procedure is performing correctly. Positive controls contain the target analyte and should yield a positive result, while negative controls lack the analyte and should yield a negative result. Controls help identify assay failures, contamination, or procedural errors.

   **Example usage:**  
   Positive and negative controls were included in each DNA extraction run to verify extraction efficiency and ensure the absence of contamination.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, controls are datasets used to verify pipeline performance and detect errors. Positive controls include datasets with expected variants or signals, which can be real experimental data or in silico–generated datasets simulating expected features. Negative controls, such as empty libraries, no-template runs, or in silico blanks, are used to detect contamination or spurious results.

      **Example usage:**  
      *“Positive control datasets containing known SNVs were used to confirm variant calling accuracy, while no-template runs served as negative controls to detect contamination.”*

.. dropdown:: Correction Factors

   Factors applied to correct for known systematic biases or effects in measurements, ensuring that reported values more accurately reflect the true quantity or state.

   **Example usage:**  
   Correction factors were applied to qPCR results to adjust for variations in viral load measurements due to instrument drift and sample dilution.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“Correction factors were applied to sequencing data to normalize read counts (e.g., TPM/RPKM), adjust for batch effects, and correct error rates in variant calling.”*

.. dropdown:: Corrective Action

   Action taken to eliminate the cause of a detected non-conformance or other undesirable situation. The aim is to prevent recurrence rather than simply address the immediate issue.

   **Example usage:**  
   Corrective actions address the root cause of failed QC results, contamination events, or SOP deviations — for example, retraining staff or revising procedures after a control failure.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, corrective actions may be triggered by pipeline failures, untraceable results, or deviations from documented workflows. They go beyond fixing the symptom — addressing the underlying cause through procedural updates, training, or improved documentation.

      **Example usage:**  
      *“A corrective action was implemented by updating the SOP to require version-controlled reference genomes to ensure traceability and reproducibility.”*

.. dropdown:: Cross Audit

   A peer-to-peer audit carried out between collaborating organisations or departments to ensure consistent application of quality standards and identify areas for improvement.

   **Example usage:**  
   A cross audit between two hospital laboratories compared sample handling and reporting procedures to align best practices.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“A cross audit between two genomic centres reviewed variant-calling pipelines to ensure consistent validation and traceability across sites.”*

.. dropdown:: Development

   A structured process of designing, creating, and refining new methods, assays, systems, or workflows. Under ISO 15189, development must follow controlled and documented stages — including design input, design output, verification, validation, and implementation — to ensure the final product or method meets defined performance specifications and intended use.

   **Example usage:**  
   Development of a new RNA extraction protocol was carried out under design control, with verification against existing methods and validation using clinical samples to confirm performance suitability.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      A structured process of designing, creating, and refining new methods, assays, systems, or workflows. Under ISO 15189, development must follow controlled and documented stages — including design input, design output, verification, validation, and implementation — to ensure the final product or method meets defined performance specifications and intended use. In bioinformatics, development often follows agile software development principles.

      **Example usage:**  
      *“Development of the HIV bioinformatics pipeline was performed under design control, with verification using synthetic datasets and validation against reference genomes to ensure accurate detection of known resistance variants and reliable prediction of their clinical impact.”*

.. dropdown:: Deviations

   A documented departure from an approved laboratory procedure, specification, or expected result. Deviations may arise from skipped steps, use of incorrect reagents, instrument malfunction, or environmental control failures. All deviations must be recorded in the QMS, investigated for root cause, and addressed through corrective or preventive actions (CAPA).

   **Example usage:**  
   A deviation was recorded when an extraction was performed using a reagent lot that had not been approved under the current SOP.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      A documented departure from an approved computational procedure, specification, or expected outcome. Examples include use of unvalidated software versions, incorrect reference genomes, or failure to follow the defined pipeline workflow. Deviations must be recorded, investigated, and resolved through CAPA to maintain reproducibility, traceability, and compliance.

      **Example usage:**  
      *“A deviation was recorded when the analyst used a reference genome build that was not specified in the validated pipeline SOP.”*

.. dropdown:: Discrepancy

   Documented difference between observed and expected results, processes, or records.

   **Example usage:**  
   The measured DNA concentration of a sample differed from the value recorded during initial quantification, triggering a review of sample handling and pipetting

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      A documented difference between expected and observed results, workflows, or data. This includes mismatches between SOP instructions and actual pipeline parameters, between expected QC values and observed results, or between repeated pipeline runs.

      **Example usage:**  
      *“Pipeline parameters did not match SOP instructions, QC metrics fell outside expected thresholds, or reruns of the same analysis produced differing variant counts.”*

.. dropdown:: Document Control

   A formal process to ensure documents are reviewed, approved, distributed, updated, and archived within a quality management system (QMS).

   **Example usage:**  
   Document control procedures ensured obsolete DNA extraction SOPs were archived and only current versions were used.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      A formal process to manage and track pipeline documentation, including SOPs, scripts, and configuration files, ensuring only approved and current versions are used.

      **Example usage:**  
      *“Document control procedures ensured the SOP was updated to include the latest validated version of a specific pipeline.”*

.. dropdown:: External Audit

   An audit conducted by an independent organisation, such as an accreditation body or regulatory authority, to verify compliance with standards (e.g., ISO 15189, ISO 17025).

   **Example usage:**  
   An external audit by UKAS assessors confirmed that all testing processes met ISO 15189 requirements.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“An external ISO audit included review of computational processes, confirming that data handling, validation, and documentation met accreditation standards.”*

.. dropdown:: External Quality Assessment (EQA)

   Formal evaluation of a laboratory’s or analytical service’s performance through participation in external comparison programmes such as UK NEQAS or equivalent schemes. EQA verifies that internal quality control procedures, methods, and analytical outputs remain accurate, reliable, and consistent with external benchmarks.

   **Example usage:**  
   The laboratory participated in a UK NEQAS Molecular EQA scheme for Mycobacteria molecular detection and resistance testing, processing simulated sputum samples to assess detection accuracy and rifampicin resistance prediction. Participation verified the lab’s performance against national benchmarks.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Evaluation of a bioinformatics pipeline or analysis by comparing outputs with external datasets, peer labs, benchmarking challenges, or gold-standard datasets.

      **Example usage:**  
      *“The bioinformatics team participated in an inter-laboratory EQA exercise by re-analyzing datasets from the UK NEQAS Molecular SARS-CoV-2 variant typing scheme and comparing variant calls against gold-standard references. This confirmed pipeline accuracy for variant identification.”*

.. dropdown:: Finding

   Result of an evaluation against requirements, identifying conformity, non-conformity, or opportunities for improvement.

   **Example usage:**  
   An audit finding noted that sample storage temperatures were not consistently recorded.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“An audit finding noted that pipeline versions were not recorded in the report.”*

.. dropdown:: Functional Specification

   A document detailing what a system, process, or component must achieve, without prescribing how it should be done.

   **Example usage:**  
   The functional specification for a DNA extraction process required consistent yield and purity across sample types.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      A document specifying the expected inputs, outputs, performance, and features of a pipeline or software tool, without dictating implementation.

      **Example usage:**  
      *“The functional specification for the pipeline required it to accept FASTQ input and produce annotated VCF output within defined runtime parameters.”*

.. dropdown:: Improved Performance

   Demonstrated enhancement in the efficiency, effectiveness, or reliability of a process following a change. Improvement must be measured against predefined indicators.

   **Example usage:**  
   Improved performance was demonstrated by shorter turnaround times and reduced sample handling errors after workflow optimization.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Demonstrated enhancement in the efficiency, accuracy, or reliability of a bioinformatics pipeline or analysis following a change. Improvement must be measured against predefined metrics.

      **Example usage:**  
      *“Improved performance was demonstrated by reducing false positive variant calls by 20% and adding new functionality for structural variant detection after pipeline optimization.”*

.. dropdown:: Incident

   An occurrence that led or could lead to non-conformance, error, or deviation from expected results.

   **Example usage:**  
   An incident occurred when a sample was mislabeled, resulting in an incorrect test assignment and an out-of-TAT result.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“An incident occurred when a misconfigured pipeline parameter caused incorrect variant calls across multiple samples.”*

.. dropdown:: Inconsistencies

   Lack of uniformity or agreement in data, documents, or results. ISO expects identification and resolution of inconsistencies.

   **Example usage:**  
   Inconsistencies were found between duplicate PCR reactions, prompting a review of sample handling procedures.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“Inconsistencies were identified between pipeline documentation and the parameters actually applied.”*

.. dropdown:: Installation Qualification (IQ)

   Documented verification that equipment is installed correctly and meets the manufacturer’s specifications. Part of the validation process (IQ/OQ/PQ).

   **Example usage:**  
   Installation qualification confirmed that a new PCR machine was set up according to the manufacturer’s instructions.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Documented verification that software, pipelines, and supporting compute infrastructure are installed correctly and meet expected specifications. Part of the validation process (IQ/OQ/PQ).

      **Example usage:**  
      *“Installation qualification confirmed that the pipeline and HPC environment, including all dependencies and compute nodes, were correctly configured.”*

.. dropdown:: Interferences

   Influence from a substance, signal, or condition that alters the true measurement.

   **Example usage:**  
   Interferences from primer-dimers or nonspecific amplification affected qPCR quantification accuracy.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Influence from contaminating sequences, technical artefacts, cross-talk, or algorithmic bias that distorts analysis results.

      **Example usage:**  
      *“Interferences from index hopping introduced artefactual reads into the dataset.”*

.. dropdown:: Internal Audit

   A systematic, independent evaluation conducted within an organisation to determine whether activities and related results comply with planned arrangements and meet quality management system (QMS) requirements.

   **Example usage:**  
   An internal audit reviewed sample tracking and equipment calibration logs to confirm compliance with the laboratory’s quality procedures.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“An internal audit reviewed pipeline traceability, code version control, and validation records to ensure compliance with documented SOPs.”*

.. dropdown:: Internal Quality Control

   Procedures performed within the laboratory’s routine operations to monitor ongoing performance and detect errors in real time. Often involves control samples run alongside test samples.

   **Example usage:**  
   Daily instrument controls, reagent blanks, and positive/negative controls were included in each qPCR run.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Procedures within routine data analysis to monitor pipeline performance and detect errors or anomalies in real time.

      **Example usage:**  
      *“QC metrics and control datasets were analyzed alongside sample data to identify unexpected coverage drops or variant calling errors.”*

.. dropdown:: Language

   System of terms, symbols, or structured vocabulary used for communication. In ISO contexts, clarity and consistency of language is critical for compliance.

   **Example usage:**  
   The laboratory ensured that terms like “validation” and “verification” were used consistently across SOPs and reports, maintaining clarity and traceability.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, language has dual meaning: human language (terminology in SOPs, ontologies) and programming language (R, Python). ISO focus is on controlled terminology, so “language” here means ensuring words are used consistently across SOPs and data dictionaries.

      **Example usage:**  
      *“nan”*

.. dropdown:: Management System

   A set of interrelated or interacting elements used to establish policies, objectives, and processes to achieve them. In laboratories, this typically includes the Quality Management System (QMS) and can extend to cover data analysis, documentation, software versioning, traceability, and validation/verification of pipelines.

   **Example usage:**  
   The management system was updated to include procedures for sample tracking and instrument calibration.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“The management system was updated to include documented procedures for software version control and data retention in bioinformatics workflows”*

.. dropdown:: Method / Procedure / Process

   Method: A systematic approach or technique used to achieve a specific objective.

Procedure: A defined series of steps to implement a method, usually documented in a Standard Operating Procedure (SOP).

Process: A broader set of interrelated activities that together achieve a final outcome, often encompassing multiple methods and procedures.

   **Example usage:**  
   Method: The qPCR amplification method was chosen to quantify SARS-CoV-2 viral RNA accurately.

Procedure: The SOP outlined the RNA extraction and cDNA synthesis procedure for all clinical samples.

Process: The laboratory follows an end-to-end pathogen detection process from sample receipt through sequencing and reporting.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“Method: The read alignment method using bwa mem was applied to map sequencing reads to the reference genome.

Procedure: The variant calling procedure involved sorting BAM files, marking duplicates, and running GATK HaplotypeCaller.

Process: The computational workflow constitutes a complete process from raw reads through QC, alignment, variant calling, annotation, and report generation.”*

.. dropdown:: Metrological Traceability

   In wet labs, metrological traceability is the gold standard for linking measurements (e.g., concentration) back to SI units through reference materials and calibrated instruments.

   **Example usage:**  
   Metrological traceability of viral load estimates was established using reference datasets linked to WHO international standards.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, metrological traceability refers to linking computed or digital results (e.g., expression levels, variant frequencies) back to reference standards, validated datasets, or algorithms, with documented uncertainty, thereby anchoring digital outputs to real-world measurement systems.

      **Example usage:**  
      *“Variant allele frequencies in pathogen genomics were benchmarked against Genome in a Bottle (GIAB) reference datasets to establish metrological traceability of computational measurements.”*

.. dropdown:: Near-miss

   An occurrence that could have caused harm or non-conformance but did not.

   **Example usage:**  
   A near-miss occurred when two samples were swapped, but the error was caught during the procedure.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“A near-miss occurred when an outdated HIV resistance database was nearly used, which would have missed a clinically relevant variant in a sample, but the issue was detected before reporting results.”*

.. dropdown:: Noise

   Unwanted variation or disturbance that obscures the measurement of the true signal. Noise can be random or systematic and may arise from instrument background signals, contamination, sample degradation, or environmental fluctuations.

   **Example usage:**  
   Background fluorescence from the plate reader contributed noise that was accounted for during viral load quantification.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Random sequencing errors or background reads not associated with the true signal (e.g., low-quality base calls, index hopping). Noise can also appear as spurious variation in high-dimensional datasets (e.g., dropout in single-cell RNA-seq).

      **Example usage:**  
      *“The signal-to-noise ratio was evaluated in SARS-CoV-2 sequencing data to filter out low-quality reads and minimize spurious variant calls”*

.. dropdown:: Non-conformance

   Non-fulfilment of a requirement. May arise from deviations, errors, or failures to meet specifications.

   **Example usage:**  
   A non-conformance was recorded when the laboratory technician deviated from the SOP during RNA extraction, potentially affecting downstream sequencing results.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“A non-conformance was identified when a non-validated reference database was used for pathogen genome annotation.”*

.. dropdown:: Patient Safety

   Reduction of risk of unnecessary harm to patients to an acceptable minimum (ISO 15189).

   **Example usage:**  
   Patient safety is maintained by following validated protocols, including proper labeling and handling, and using appropriate controls to prevent incorrect results or sample mix-ups that could lead to misdiagnosis.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“In clinical bioinformatics, patient safety involves ensuring that analyses and reports do not cause harm through misclassification, delays, or unclear communication, such as false negatives in pathogen detection.”*

.. dropdown:: Performance Qualification (PQ)

   Evidence that systems/processes perform as intended under routine (real-world) conditions.

   **Example usage:**  
   Performance qualification demonstrated that the sequencing pipeline maintained processing of ≥100 samples per day with stable accuracy and no missed service-level agreements (SLAs) over 30 consecutive days.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“For computational workflows, PQ demonstrates that a pipeline and infrastructure deliver consistent accuracy and throughput under production load with monitored stability. While the term “PQ” is rarely used outside regulated settings, the principle ensures reliable bioinformatics performance in routine use.”*

.. dropdown:: Performance Reporting

   Structured communication of performance against defined objectives or indicators, often using agreed metrics to track quality, efficiency, and reliability.

   **Example usage:**  
   Quarterly performance reporting summarized contamination rates, turnaround times, and repeat extraction frequencies against established targets.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Performance reporting in bioinformatics may take the form of periodic dashboards or reports summarizing key performance indicators such as mapping rate, turnaround time, re-analysis rate, pipeline failure rates, and variant calling accuracy, with trends highlighted and corrective actions documented.

      **Example usage:**  
      *“nan”*

.. dropdown:: Performance Review

   Formal evaluation of performance against predefined objectives, standards, or indicators, used to identify areas for improvement and ensure ongoing compliance with quality requirements

   **Example usage:**  
   The semi-annual performance review identified missed turnaround time (TAT) targets and triggered a capacity upgrade.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“A performance review of the pathogen genomics pipeline identified recurring pipeline failures and suboptimal mapping rates, leading to revalidation and infrastructure improvements as part of CAPA.”*

.. dropdown:: Performance Verification

   Confirmation that a system, method, or pipeline performs according to predefined requirements or specifications. Verification demonstrates that stated performance characteristics are achieved, but is narrower in scope than full validation (which assesses overall suitability for intended use).

   **Example usage:**  
   Performance verification confirmed that the PCR assay consistently detected target pathogens at the predefined limit of detection.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“Performance verification demonstrated that the pathogen genomics pipeline achieved the stated runtime and reproducibility, with sensitivity ≥95% and specificity ≥99% based on the Genome in a bottle (GIAB) test set.”*

.. dropdown:: Preparation

   Process of making something ready for use, often referring to specimens, reagents, or documents. Steps are controlled and documented to ensure reproducibility and traceability.

   **Example usage:**  
   Preparation involved creating reagent aliquots, labeling samples, and setting up specimens according to SOPs.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Process of making data ready for analysis, including file formatting, quality control filtering, adapter trimming, and metadata curation. Steps must be controlled and documented to ensure reproducibility.

      **Example usage:**  
      *“Preparation of the sequencing dataset included adapter trimming, QC filtering, file formatting, and metadata standardization before downstream analysis.”*

.. dropdown:: Preventive Actions

   Actions taken to eliminate the cause of a potential non-conformance, before it occurs. Preventive actions are proactive measures designed to reduce risk and improve system robustness.

   **Example usage:**  
   As a preventive action, the laboratory introduced dual sample labeling and independent verification steps to avoid potential mix-ups during DNA extraction.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“As a preventive action, we added pre-release smoke tests and immutable reference files to avoid silent regressions in the pathogen genomics pipeline. Other examples include enforcing version pinning, implementing storage redundancy, and using continuous integration (CI) checks to prevent configuration drift or silent failures.”*

.. dropdown:: Procedure

   Specified way to carry out an activity or process (ISO 9000).

   **Example usage:**  
   The DNA extraction procedure specifies centrifugation speeds, buffer compositions, and acceptance criteria for yield and purity.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Step-by-step instructions for performing a specific aspect of a bioinformatics workflow, with defined inputs, parameters, expected outputs, and traceable records.

      **Example usage:**  
      *“The QC procedure details how raw sequencing reads are checked for quality metrics, trimmed, adapters removed, deduplicated, and filtered before downstream analysis, with all steps and parameters documented to ensure reproducibility and traceability.”*

.. dropdown:: Process

   Series of interrelated or interacting activities that transform inputs into outputs.

   **Example usage:**  
   The DNA extraction and library preparation process converts tissue or blood samples into purified, sequencer-ready DNA libraries.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“The variant analysis process converts raw FASTQ reads into annotated VCF files through sequential steps including mapping, deduplication, variant calling, and variant interpretation.”*

.. dropdown:: Quality 

   Degree to which a set of inherent characteristics of an object fulfills requirements. It reflects fitness for intended use under a Quality Management System (QMS).

   **Example usage:**  
   The quality of the RNA extraction was assessed by measuring yield, purity, and integrity against predefined acceptance criteria.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Degree to which a computational analysis or dataset meets defined criteria for accuracy, reliability, and reproducibility under a QMS.

      **Example usage:**  
      *“The quality of the sequencing analysis was evaluated by comparing read depth, base quality scores, duplication rates, and alignment metrics to predefined acceptance thresholds.”*

.. dropdown:: Quality control 

   Operational techniques and activities used to fulfil quality requirements, ensuring results are consistent, valid, and reliable. Includes checks on reagents, instruments, calibration, and control samples, performed according to documented procedures and predefined thresholds.

   **Example usage:**  
   QC of RNA extraction included monitoring reagent performance, running positive and negative controls, and checking instrument calibration.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Operational checks applied to sequencing or analysis data to ensure accuracy and reliability, anchored to predefined, measurable criteria rather than informal filtering. May include adapter trimming, base-quality filtering, duplicate removal, and assessment of mapping rates.

      **Example usage:**  
      *“QC of RNA-seq reads included trimming adapters, filtering low-quality bases, removing duplicates, and evaluating mapping rates to confirm data suitability for downstream analysis.”*

.. dropdown:: Quality Indicators

   Quantitative measures used to monitor and evaluate how well a process meets predefined quality objectives. Indicators should be measurable, predefined, and regularly reviewed to support continuous improvement.

   **Example usage:**  
   Quality indicators in the laboratory included turnaround times, error rates, and frequency of repeat testing.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See plain definition

      **Example usage:**  
      *“In bioinformatics, quality indicators may include read mapping rates, error rates in variant calls, reproducibility scores, and user satisfaction with reports. These indicators should be predefined, measurable, and regularly reviewed to ensure pipeline performance and reliability.”*

.. dropdown:: Quality Management System (QMS)

   A structured set of policies, processes, procedures, and responsibilities used by an organization to ensure quality objectives are achieved, risks are managed, and compliance with applicable standards is maintained (ISO 9000/ISO 15189).

   **Example usage:**  
   The laboratory implemented a QMS encompassing SOPs, document control, internal audits, equipment calibration, and staff training to ensure reliable and reproducible molecular test results.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      nan

      **Example usage:**  
      *“nan”*

.. dropdown:: Reference

   A source that provides evidence or context for a decision, requirement, or comparison. In ISO, often refers to authoritative standards or datasets.

   **Example usage:**  
   Wet-lab references include international standards, reference ranges, or cited procedures used to interpret test results.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, reference materials include reference genomes, databases, or curated datasets used as benchmarks.

      **Example usage:**  
      *“Variant calls were compared against HIV references and HIV variant databases to detect known resistance mutations and validate accuracy.”*

.. dropdown:: Reference Material 

   Material that is sufficiently homogeneous and stable with respect to specified properties, established to be fit for its intended use in measurement. Certified Reference Materials (CRMs) have documented property values with stated uncertainty. Controls run within an experiment are not reference materials; only external standards with traceable properties qualify.

   **Example usage:**  
   A certified reference DNA sample was used to verify assay accuracy across multiple qPCR runs.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Material or datasets used to validate and verify bioinformatics pipelines, providing a known baseline for comparison. This includes gold-standard datasets (e.g., NA12878 genome from GIAB), well-characterized cell lines, or spike-in controls.

      **Example usage:**  
      *“The sequencing pipeline was verified using a Genome in a Bottle GIAB reference genome to confirm variant calling accuracy.”*

.. dropdown:: Reporting 

   Formal communication of laboratory test results in a controlled and traceable format, ensuring clarity, accuracy, and compliance with the Quality Management System (QMS).

   **Example usage:**  
   Reporting included generating a PDF report for clinicians summarizing HIV viral load, QC metrics, and validated assay results for resistance testing, enabling informed treatment decisions.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Controlled communication of analysis results in a reproducible and traceable format. Includes QC summaries, variant calls, predicted phenotypes, and structured outputs for stakeholders. May involve submission of variants to international databases. Ensures results are interpretable, accurate, and auditable within the QMS.

      **Example usage:**  
      *“Reporting of HIV sequencing data included resistance variants and predicted susceptibility to antiretroviral therapies, delivered as structured outputs (e.g., JSON for databases, PDF for clinicians), and included submission of variants to international databases such as HIVdb (Stanford HIV Drug Resistance Database).”*

.. dropdown:: Requirement for Reports

   ISO requires that reports include minimum information to ensure traceability and interpretability, such as sample/patient identification, methods, results, interpretations, and signatures.

   **Example usage:**  
   The requirement for reports mandated inclusion of sample identification, assay method, QC control results, measured viral load, and signature of the clinical scientist, ensuring results were traceable, verified, and suitable for clinical decision-making.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      ISO requires that computational analysis reports include minimum information such as software version, reference genome, pipeline parameters, QC metrics, and results interpretations to ensure reproducibility and compliance with the QMS.

      **Example usage:**  
      *“The requirement for reports mandated inclusion of software version and reference genome used, along with QC metrics, in the sequencing report.”*

.. dropdown:: Result Validity

   Extent to which a result can be considered sound, accurate, and supported by evidence. In ISO, validity is linked to adherence to validated methods, QC, and traceability.

   **Example usage:**  
   Result validity was ensured by verifying assay outputs against a certified reference material and confirming QC metrics were within acceptable ranges.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“Result validity is demonstrated when all computational analyses produce consistent, accurate, and reproducible outputs, using validated pipelines, appropriate reference data, and quality-controlled input, so that the results can be confidently used for clinical or public health decisions.”*

.. dropdown:: Review

   Systematic examination of activities, results, or documents against requirements. In ISO, a review means a documented, traceable sign-off that ensures accuracy, completeness, and compliance.

   **Example usage:**  
   All sequencing reports underwent independent review, with a second clinical scientist performing a counter-sign check to confirm the analysis before release.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, review applies to SOPs, pipeline code, and analysis reports, including code reviews and validation of outputs. Traceability is maintained via review logs, approvals, and audit trails to demonstrate compliance with validated standards and reproducibility.

      **Example usage:**  
      *“The updated influenza pipeline underwent code review by a second bioinformatician before deploying the updated pipeline.”*

.. dropdown:: Risk Analysis

   Systematic use of information to identify sources of risk and estimate their likelihood and impact (ISO 14971, ISO 31000).

   **Example usage:**  
   Risk analysis identified hazards in sample handling, including potential contamination during extraction, mislabeling of samples, degradation during transport, and improper storage conditions, allowing the laboratory to implement mitigation measures.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Risk analysis assesses risks in computational workflows, including pipeline failures, data loss, unauthorized access, misinterpretation of results, and algorithmic biases. It guides the implementation of risk controls and informs decision-making.

      **Example usage:**  
      *“Risk analysis identified the possibility of pipeline failure or data loss due to insufficient storage redundancy, leading to backup systems and version-controlled pipelines.”*

.. dropdown:: Risk Management

   Risk management involves identifying, evaluating, and mitigating hazards in laboratory processes, including sample handling errors, contamination, instrument failure, and assay deviations. Controls may include standardized SOPs, staff training, QC procedures, and maintenance schedules.

   **Example usage:**  
   Risk management in the laboratory included second-person checks to reduce the risk of sample mix-ups during lab procedures.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Risk management covers pipeline errors, software bugs, incorrect reference databases, misannotation, or reproducibility failures, and extends to data security and patient confidentiality when handling clinical data. Controls include version-controlled pipelines, automated QC checks, backups, and access restrictions.

      **Example usage:**  
      *“Risk management for the updated influenza pipeline included version-controlled code review and automated unit testing/continuous integration (CI) testing to reduce the risk of negative impact on results, such as producing erroneous or misleading outputs once deployed.”*

.. dropdown:: Sample 

   One or more items taken from a population or individual and intended to provide information about that population or individual (ISO 15189 / ISO 17025). In wet labs, this is usually the patient specimen or aliquot under test, such as whole blood, tissue biopsy, swab, urine, stool, or other biological material.

   **Example usage:**  
   Each sample was assigned a unique identifier before sequencing to ensure traceability between the physical specimen and associated laboratory records.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, sample can also refer to a dataset derived from a single biological specimen, such as FASTQ files, BAM files, or cell counts. In multi-omics studies, one specimen may generate multiple data types (DNA, RNA, protein), and careful tracking is needed to maintain traceability.

      **Example usage:**  
      *“For HIV resistance analysis, each sample dataset—including FASTQ and BAM files derived from a patient’s blood specimen—was tracked with a unique identifier, ensuring traceability and reproducibility across the pipeline, even when multiple data types (DNA, RNA) were generated from the same specimen.”*

.. dropdown:: Sample Quality

   Degree to which a sample is suitable for intended testing, including integrity, stability, and absence of contamination.

   **Example usage:**  
   Sample quality was assessed by measuring RNA integrity numbers (RIN) and total concentration to confirm suitability for sequencing.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Sample quality reflects whether sequencing data derived from a specimen is reliable. Metrics include read length, duplication rate, adapter contamination, and overall sequence integrity, guiding decisions for downstream analysis and reporting.

      **Example usage:**  
      *“Sample quality was evaluated by examining read length, duplication rate, adapter contamination, and overall sequence integrity to ensure reliable input for variant calling.”*

.. dropdown:: Scope

   Extent and boundaries of activities, analyses, or services covered by a document, SOP, or accreditation.

   **Example usage:**  
   The scope of this SOP covers DNA sequencing workflows using Illumina platforms only.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      See traditional definition

      **Example usage:**  
      *“The scope of this SOP covers analysis of Illumina DNA sequencing data, including quality control, alignment, and variant calling.”*

.. dropdown:: Selection

   Choosing appropriate methods, materials, or procedures to meet requirements.

   **Example usage:**  
   The laboratory documented the selection of an RNA extraction kit suitable for blood and tissue samples, with justification based on yield and purity requirements.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, selection means choosing reference genomes, algorithms, or parameters appropriate for the intended use. Often tied to justification of why a method was chosen.

      **Example usage:**  
      *“The selection of the GRCh38 reference genome was documented, including rationale for clinical suitability and compatibility with existing pipelines.”*

.. dropdown:: Selectivity

   Ability of a method to distinguish the analyte of interest from other components.

   **Example usage:**  
   The assay showed high selectivity by correctly distinguishing SARS-CoV-2 reads from background human RNA.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Ability of an analysis pipeline to detect the true signal in the presence of confounders, such as identifying a pathogen without false signals from host DNA.

      **Example usage:**  
      *“The bioinformatics pipeline demonstrated high selectivity by correctly identifying viral reads while excluding host and environmental sequences.”*

.. dropdown:: Sensitivity

   Ability of a method to correctly identify positives (true positive rate).

   **Example usage:**  
   The qPCR assay achieved a sensitivity of 98% for detecting the target gene

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Ability of a pipeline or algorithm to correctly identify true positives, expressed as the proportion of true variants or targets detected.

      **Example usage:**  
      *“The sequencing pipeline achieved a sensitivity of 98% for SNP detection in the GIAB dataset.”*

.. dropdown:: SI Units

   International System of Units — globally agreed reference units for measurement (ISO/IEC 80000).

   **Example usage:**  
   RNA concentration was measured as 50 ng/µL

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      SI units are used when linking digital results back to physical measurements, e.g., read depth reported as coverage per base pair, genome size in base pairs (bp), RNA yield in ng, or runtimes in seconds. Using SI units ensures interoperability and standardization across laboratories and pipelines.

      **Example usage:**  
      *“Sequencing read depth was reported as coverage per base pair.”*

.. dropdown:: Specificity

   Ability of a method to correctly identify negative results (true negative rate).

   **Example usage:**  
   The qPCR assay demonstrated 99% specificity, showing minimal cross-reactivity with non-target sequences.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Ability of a pipeline or algorithm to avoid false positives, correctly identifying true negatives. Applied in variant calling, classification, and pathogen screening.

      **Example usage:**  
      *“The sequencing pipeline demonstrated 99% specificity for SNP detection in the GIAB dataset.”*

.. dropdown:: Standard Operating Procedure (SOP)

   Controlled document describing the approved way to perform a specific activity (ISO 9000).

   **Example usage:**  
   The SOP for RNA extraction defines the protocol for isolating RNA from specific sample types, including reagents, incubation times, and yield assessment. The SOP was reviewed, approved, and version-controlled under document control.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, SOPs govern data handling, QC, analysis, reporting, and archiving. Falls under document control: must be versioned, reviewed, approved, and archived.

      **Example usage:**  
      *“The SOP for weekly system health checks defines procedures for monitoring software versions, disk usage, pipeline runtimes, and backup status. It is reviewed, approved, and version-controlled to ensure traceability and compliance with the QMS.”*

.. dropdown:: Storage Space

   Resources for preserving samples, records, or data safely and accessibly.

   **Example usage:**  
   Freezer storage space and conditions were monitored regularly to ensure sufficient capacity and that samples were maintained under appropriate conditions.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, storage space refers to digital storage for raw sequencing data, intermediate files, and results. ISO requires documented monitoring, capacity planning, and protection against data loss, such as regular backups and controlled access.

      **Example usage:**  
      *“Storage space for sequencing data was monitored monthly to ensure compliance with retention and data integrity policies.”*

.. dropdown:: Suitability

   Extent to which something is appropriate for its intended purpose. In ISO, suitability is often assessed during validation or verification, and in wet labs refers to whether materials, reagents, or reference standards are appropriate for their intended use.

   **Example usage:**  
   The RNA extraction kit was evaluated for suitability with blood and tissue samples to ensure efficient recovery and integrity of RNA.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Suitability refers to whether a pipeline, dataset, or reference genome is appropriate for the intended computational analysis.

      **Example usage:**  
      *“Suitability was ensured by choosing the appropriate reference genome based on the virus of interest and selecting a reference that met a closeness threshold relative to the sample sequence to maximize accuracy of variant calling.”*

.. dropdown:: Technical Knowledge

   Evidence-based understanding of principles, methods, and standards required to perform a task competently.

   **Example usage:**  
   Lab personnel performing next-generation sequencing must demonstrate technical knowledge of library preparation, sequencing assays, instrumentation, and associated quality control metrics to ensure reliable and reproducible results.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, technical knowledge includes understanding algorithms, data formats, QC principles, software development practices, programming languages (e.g., Python, R), workflow management systems, and compute infrastructure.

      **Example usage:**  
      *“During the development of a new analytical pipeline for SARS-CoV-2, the bioinformatician drew on their technical knowledge when selecting appropriate bioinformatics tools and reference genomes, implementing workflow management with Git, coding reproducible modules, and testing the pipeline using datasets representing both standard and edge cases to ensure reliability and reproducibility.”*

.. dropdown:: Traceability

   Ability to trace the history, application, or location of an object or activity (ISO 9000). In metrology, often linked to the chain of calibrations to standards.

   **Example usage:**  
   Traceability was maintained by logging each RNA sample’s extraction batch, operator, and reagent lot number, ensuring that any downstream result could be fully audited.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, traceability refers to linking results back to raw data, pipeline versions, parameters, reference files, and analysts, enabling reproducibility and auditability.

      **Example usage:**  
      *“Traceability of the variant call was maintained by linking the result to raw FASTQ files, pipeline version 3.2, and the reference genome build.”*

.. dropdown:: Training/ re-training 

   Process of developing (training) or updating (re-training) knowledge, skills, and behaviours to ensure competence. In ISO contexts, training applies to personnel — ensuring staff are competent to perform assigned tasks according to current procedures. Re-training occurs following updates to SOPs, new technology implementation, or identification of nonconformances.

   **Example usage:**  
   Staff were re-trained on the updated DNA extraction SOP following a change in reagent supplier to ensure consistent performance.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In ISO, training is for staff. In bioinformatics, “training” can also mean model training. Disambiguation is critical: training staff ensures competence in pipelines, while training models refers to machine learning. Re-training is triggered by SOP changes or nonconformance.

      **Example usage:**  
      *“Analysts were re-trained following the introduction of a new variant calling pipeline to ensure consistent and correct usage across the team.”*

.. dropdown:: Test (Examination method / procedure / process)

   A test (or examination, per ISO 15189) is the set of controlled operations that apply a defined method to a sample to generate a measurable result. In ISO terms, it represents the act of measurement or analysis performed under specified and validated conditions.

   **Example usage:**  
   A PCR assay is a test that amplifies and detects target DNA sequences to confirm the presence of a pathogen in a patient sample.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, a test refers to the analytical process that transforms raw sequencing or molecular data into interpretable results using defined computational methods.

      **Example usage:**  
      *“Variant calling is a bioinformatics test that identifies genomic variants from aligned sequencing data using a validated algorithm and parameters.”*

.. dropdown:: Tolerance

   Permissible range of variation in a measurement, value, or condition without invalidating the result (ISO VIM). Tolerance refers to acceptable deviations in experimental measurements or conditions that do not compromise the validity of results.

   **Example usage:**  
   A tolerance of ±5% in pipetted reagent volumes was allowed to account for minor variations without affecting assay performance.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, tolerance applies to predefined thresholds that results must stay within. Examples: acceptable mismatch rates in alignments, allowable run-time variance, or thresholds for QC metrics. It ensures outputs are still valid despite small variations.

      **Example usage:**  
      *“A tolerance of ±5% in mapping rate was allowed between replicate sequencing runs, and QC thresholds defined acceptable mismatch rates in alignments or allowable run-time variance.”*

.. dropdown:: Trueness 

   Closeness of agreement between the average of a large number of test results and a reference (true) value (ISO 5725). It reflects systematic error, not random error.

   **Example usage:**  
   The trueness of a qPCR assay was assessed by comparing measured concentrations of a reference standard to the certified target values.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Closeness of agreement between the average result produced by a bioinformatics pipeline and a reference (true) value (ISO 5725). Trueness reflects systematic error rather than random variation and is closely linked to bias.

      **Example usage:**  
      *“The trueness of a variant calling pipeline was assessed by comparing called variants against a gold-standard dataset, such as the Genome in a Bottle reference set, to identify and correct systematic biases in the analysis.”*

.. dropdown:: User 

   Individuals or organizations that use a product, service, or system (ISO 15189 / ISO 17025). Users can include patients, clinicians, researchers, or other stakeholders relying on laboratory outputs.

   **Example usage:**  
   Users of the laboratory include clinicians requesting RNA-seq analysis for patient cancer samples.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      An individual or organization that interacts with or relies on bioinformatics products, services, or systems. Users may include researchers accessing processed datasets, clinicians receiving variant reports, or other stakeholders using pipeline outputs for decision-making. User needs inform the design, documentation, and quality control of pipelines, software, and analysis workflows to ensure outputs are reliable, reproducible, and fit for purpose.

      **Example usage:**  
      *“Users of the SARS-CoV-2 analysis pipeline include virologists accessing curated variant datasets and clinicians using reports to inform treatment decisions.”*

.. dropdown:: User Requirement Specification (URS)

   A document that defines what the user needs from a system, device, or process, expressed in functional or performance terms (per ISO/IEC and software validation guidance). The URS forms the foundation for design, verification, and validation activities.

   **Example usage:**  
   The user requirement specification stated the pipeline must process FASTQ files and produce annotated VCFs within 48 hours.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, a URS defines what analysts, clinicians, or researchers require from a computational system — such as accepted input formats, expected outputs, performance targets, or reporting needs. It ensures pipelines are designed and validated to meet end-user expectations.

      **Example usage:**  
      *“The user requirement specification stated that the LIMS must track sample barcodes, record reagent batches, and generate audit reports accessible within 24 hours.”*

.. dropdown:: Validation

   Confirmation, through objective evidence, that requirements for a specific intended use are fulfilled (ISO 9000, VIM). Validation ensures that a method, assay, or procedure produces accurate, reliable, and reproducible results for its intended purpose.

   **Example usage:**  
   Validation of the RNA-seq pipeline confirmed it was suitable for accurately quantifying gene expression in FFPE cancer samples, supporting clinical decision-making by identifying the most appropriate therapy for individual patients.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      In bioinformatics, validation demonstrates that a pipeline, tool, or dataset is fit for purpose. It goes beyond technical correctness to confirm suitability for the stated analysis.

      **Example usage:**  
      *“A variant calling pipeline was validated by demonstrating sensitivity and specificity on gold-standard datasets, ensuring it is appropriate for clinical use.”*

.. dropdown:: Verification (Verification Plan, Schedule of Verification)

   Confirmation, through evidence, that a method, pipeline, or tool has been implemented correctly according to specifications (ISO 9000). Verification focuses on technical correctness and adherence to SOPs or design, rather than suitability for the broader intended purpose.

   **Example usage:**  
   The verification plan required re-running a standard dataset quarterly to ensure the assay consistently produced expected results.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      Verification of the updated SARS-CoV-2 pipeline confirmed that the new version still achieved its intended aims, producing expected results, maintaining sensitivity and specificity, and performing consistently on standard and edge-case datasets before deployment.

      **Example usage:**  
      *“nan”*

.. dropdown:: Workbench

   A designated workspace where specific tasks are performed in a controlled way. In ISO/QMS, a workbench is physical or digital, defined by its tools and controls.

   **Example usage:**  
   The RNA extraction workbench was organized and equipped to ensure consistent sample handling and minimize contamination.

   .. admonition:: **💻 Bioinformatics translation**
      :class: tip

      : A workbench can be a software platform (e.g., Galaxy, Chipster) or a compute environment/cluster where analyses are performed in a controlled and reproducible manner.

      **Example usage:**  
      *“The Galaxy workbench and HPC cluster were validated as controlled environments for reproducible SARS-CoV-2 data analysis.”*

