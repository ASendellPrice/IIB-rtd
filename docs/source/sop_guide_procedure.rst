Procedure
=========

.. important::
   This section is a fundamental building block of any SOP
   
The 'Procedure' section of an SOP should provide a detailed, step-by-step description of how to carry out the specific tasks or processes outlined in the SOP. This section should be clear, concise, and easy to follow, ensuring that personnel can perform the procedure consistently and accurately.

The content of the procedure section will vary considerably depending on the nature of the SOP.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics QC Procedure

   *Example SOP content for a bioinformatics QC pipeline*
   
   .. include:: sop_guide_procedure_bioinformaticsqc.rst

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Procedure
   
   Add content

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Procedure
   
   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Procedure
   
   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Procedure
   
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
