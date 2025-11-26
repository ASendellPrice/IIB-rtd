Procedure
=========

.. important::
   This section is a fundamental building block of any SOP
   
The 'Procedure' section of an SOP should provide a detailed, step-by-step description of how to carry out the specific tasks or processes outlined in the SOP. This section should be clear, concise, and easy to follow, ensuring that personnel can perform the procedure consistently and accurately.

The content of the procedure section will vary considerably depending on the nature of the SOP.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics QC Procedure
   
   .. include:: sop_guide_procedure_bioinformatics_qc.rst


.. dropdown:: 👩‍🔬 Staff Training Procedure
   
   .. include:: sop_guide_procedure_training_procedure.rst


.. dropdown:: 🧪 Laboratory Procedure
   
   .. include:: sop_guide_procedure_lab_procedure.rst


.. dropdown:: 💻 Code Update & Review Procedure
   
   .. include:: sop_guide_procedure_code_review.rst


.. dropdown:: ✅ Verification Procedure

   .. include:: sop_guide_procedure_verification.rst


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
