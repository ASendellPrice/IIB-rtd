Interferences & Limitations
===========================

This section should outline any factors that may affect the reliability, accuracy, or applicability of the procedure. Identifying interferences and limitations helps ensure that results are interpreted correctly and that the procedure is used within its validated scope.

What to Include
---------------

- **Detection or Performance Limits:** Define the boundaries of the procedure’s capability (e.g. sensitivity, specificity, minimum/maximum measurable values, or operational thresholds).

- **Interfering Factors:** List any substances, conditions, or external influences that may compromise performance. Examples include contaminants, environmental conditions, equipment variability, or data quality issues.

- **Dependencies:** Note any reliance on tools, equipment, software, reagents, or personnel expertise that could introduce limitations or compatibility concerns.

--------

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Change history
   
   The procedure is validated to detect HIV drug resistance mutations present at a minimum variant allele frequency of 5% in samples with a minimum sequencing coverage depth of 100x across the pol gene region. Variants below this threshold may not be reliably detected.

   Samples with significant contamination (e.g. bacterial DNA, human genomic DNA) or mixed infections may yield inaccurate results due to interference with read mapping and variant calling. It is recommended to assess sample purity prior to analysis.

   The pipeline relies on specific versions of software tools (e.g. BWA v0.7.17, FreeBayes v1.3.2). Using incompatible versions may lead to unexpected behaviour or errors.

   This procedure has been validated for Illumina-generated paired-end FASTQ data from clinical HIV samples. It is not validated for other sequencing platforms (e.g. Oxford Nanopore, PacBio) or sample types (e.g. environmental samples).

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Interferences & Limitations
   
   Add content

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Interferences & Limitations
   
   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Interferences & Limitations
   
   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Interferences & Limitations
   
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
