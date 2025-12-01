Procedure
=========

.. important::
   This section is a fundamental building block of any SOP
   
The 'Procedure' section of an SOP should provide a detailed, step-by-step description of how to carry out the specific tasks or processes outlined in the SOP. This section should be clear, concise, and easy to follow, ensuring that personnel can perform the procedure consistently and accurately.

The content of the procedure section will vary considerably depending on the nature of the SOP.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics QC Procedure
   
   .. include:: example_bioinformatics.rst


.. dropdown:: 👩‍🔬 Staff Training Procedure
   
   .. include:: example_training.rst


.. dropdown:: 🧪 Laboratory Procedure
   
   .. include:: example_lab.rst


.. dropdown:: 💻 Code Update & Review Procedure

   .. include:: example_code_review.rst


.. dropdown:: ✅ Validation Procedure

   .. include:: example_validation.rst


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
