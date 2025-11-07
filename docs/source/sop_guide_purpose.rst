Purpose of the Procedure
========================

.. important::
   This section is a fundamental building block of any SOP

The 'Purpose' section of an SOP should provide a clear and concise statement of why the procedure exists and its intended role within the organisation/laboratory. It should outline the specific goals the procedure aims to achieve, and explain how it contributes to broader workflows, services, or regulatory requirements. This helps users understand the value and relevance of the procedure in context.

Depending on the type of procedure, the purpose may describe:

- The operational or clinical need the procedure addresses
- The outcomes or deliverables it is designed to produce
- Its position within a larger workflow or diagnostic service

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Purpose
   
   The purpose of this procedure is to assemble and analyse sequence data generated from next-generation sequencing (NGS) of HIV samples to produce high-quality consensus genomes from which antiviral resistance can be inferred. This procedure forms part of the HIV genomic testing workflow, following sequencing and preceding clinical reporting.

   It defines a standardised bioinformatics workflow for the processing, assembly, and interpretation of HIV genomic data, ensuring accuracy, reproducibility, and clinical reliability in antiviral resistance prediction.

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Purpose

   Add content for lab procedure scope here. 

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*
         
   .. rubric:: Purpose
   
   Add content for training procedure scope here.

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Purpose

   Bioinformatics pipelines are composed of code (software), which will require updating over time as bugs are identified and fixed and new features are added. In the cases where this involves code being produced within the Luma Genomics Unit (LGU), this should be subject to a review before updates are pushed to production systems.

   This SOP covers the processes by which (a) proposals for changes are made, reviewed, and changes actioned; and (b) resulting changes are reviewed to ensure consistency and adherence to organisational policies and standards.

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Purpose

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
