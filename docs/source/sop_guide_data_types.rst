Data Type & Analysis Selection
==============================

.. important::
   This section should be included in SOPs where data is analysed or passes through a computational pipeline.

This section of an SOP should define the types of input the procedure is validated to process and explain how data characteristics determine the choice of analysis methods, tools, and parameters.

This section may include:

- **Data Format:** Specify the format(s) of input data (e.g. FASTQ, BAM, VCF), sequencing technology (e.g. Illumina, Oxford Nanopore, PacBio), and any relevant characteristics (e.g. read length, paired-end vs single-end).

- **Sample suitability:** Describe the types of samples or organisms the data is expected to represent (e.g. human clinical samples, bacterial isolates, viral genomes).

- **Analysis Selection:** Describe how the data type influences the selection of analysis tools, algorithms, and parameters. For example, certain variant callers may be optimised for short reads versus long reads.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Data Type & Analysis Selection
   
   This procedure is designed to process 150bp paired-end FASTQ files generated using Illumina sequencing platforms (e.g. MiSeq, NextSeq). Each sample should have two FASTQ files (.fastq or .fastq.gz) representing the forward and reverse reads.

   The QC pipeline is specifically optimised and validated to process this data type and read length. Samples generated using other sequencing technologies (e.g. Oxford Nanopore, PacBio) or read lengths are not validated for analysis using this procedure.
   
   The input data should be derived from microbial samples ; this procedure is not designed or validated for human sequencing datasets. Samples containing high levels of human derived reads will not pass QC thresholds. Analysis tools and pipeline parameters have been selected to align with the anticipated characteristics of microbial data. 


.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Data Type & Analysis Selection
   
   Add content

.. dropdown:: 🔬 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Data Type & Analysis Selection
   
   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Data Type & Analysis Selection
   
   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Data Type & Analysis Selection
   
   Add content

.. raw:: html

   <script>
     // Auto-close other dropdowns when one opens
     document.querySelectorAll('details').forEach((el) => {
       el.addEventListener('toggle', function () {
         if (el.open) {
           document.querySelectorAll('details').forEach((other) => {
             if (other !== el) {
               other.removeAttribute('open');
             }
           });
         }
       });
     });
   </script>
