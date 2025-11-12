Definitions
===========

This section of an SOP should include definitions of scientific, technical, and procedural terms used throughout the document. Providing clear definitions ensures that all staff members interpret terminology consistently and reduces the risk of misunderstanding. Definitions should also cover any abbreviations or acronyms that are specific to the SOP.

-----

.. rubric:: Example content

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*

   .. rubric:: Definitions

   .. list-table::
      :header-rows: 1
      :widths: 20 80

      * - Term
        - Definition
      * - FASTQ
        - A text-based file format that stores both nucleotide sequences and their associated quality scores.
      * - FASTA
        - A sequence file format containing nucleotide or protein sequences without quality data.
      * - BAM/CRAM
        - Binary and compressed alignment formats that store sequencing reads mapped to a reference genome.
      * - VCF (Variant Call Format)
        - A standard text file format used to store genetic variants identified in sequence data.
      * - Minor Variant
        - A genetic variant detected at a frequency below that of the dominant (consensus) allele, typically between 20–50%.
      * - LIMS (Laboratory Information Management System)
        - Software used to manage sample metadata and analytical results.

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Definitions

   Add content

.. dropdown:: 🔬 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Definitions

   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Definitions

   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Definitions

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
