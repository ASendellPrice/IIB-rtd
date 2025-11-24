Scope
=====

.. important::
   This section is a fundamental building block of any SOP

The 'Scope' section of an SOP should define the boundaries of the :ref:`procedure <procedure>` i.e. what it covers, what it excludes, and who it applies to. It ensures that users understand the exact context and applicability of the procedure, helping to prevent misuse or misinterpretation.

Depending on the type of procedure being documented, the scope may include:

- **Types of data or samples:** The specific data formats, sample types, equipment, or materials the procedure is designed for.

- **Technologies and methods:** The platforms, tools, or methodologies the procedure applies to.

- **Personnel:** The roles or individuals authorised to perform or oversee the procedure.

- **Limitations:** Any exclusions, constraints, or unsupported scenarios users should be aware of.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics QC procedure*
   
   .. rubric:: Scope
   
   This SOP applies to the quality control of 150bp paired-end FASTQ files generated using Illumina sequencing instruments (e.g. MiSeq, NextSeq) for microbial datasets only.  This SOP does not cover:

   - Quality control of non-microbial datasets;

   - Sequencing performed using alternative read lengths, library preparation workflows or non-Illumina platforms (e.g. Pac-Bio or Oxford Nanopore);

   - Downstream bioinformatic analyses beyond the initial QC evaluation.


.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Scope

   Add content for training procedure scope here.

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Scope

   Add content for lab procedure scope here.

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Scope

   This SOP is primarily concerned with ensuring that changes to software are authorised, moderated, and reviewed to ensure consistency with organisational policies on coding style. The following related processes are covered by other SOPs and are not included here:

   - Validation and verification of software and pipelines  
   - Development and tracking of coding competencies

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Scope
   
   Add content for verifcation procedure here.

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
