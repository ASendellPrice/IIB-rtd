Roles & Responsibilities
-----------------------

.. important::
   This section is a fundamental building block of any SOP

The 'Roles & Responsibilities' section of an SOP outlines the specific duties and accountability of individuals or teams involved in the execution, oversight, and authorisation of the procedure. Role titles (e.g. Bioinformatician, Lab Technician, Quality Manager, Head of Laboratory etc) should be used rather than individual names to ensure the SOP remains current even when staff change.

Depending on the procedure, this section should describe:

- **Roles involved:** Identify all personnel or teams responsible for performing, reviewing, or approving steps within the procedure.

- **Responsibilities:** Describe the specific duties for each role (e.g., performing laboratory procedures, data processing, quality control, result authorisation, report authorisation etc).

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Roles & Responsibilities

   **Bioinformatician:**
   
   - Responsible for the end-to-end execution and monitoring of the QC pipeline, ensuring all steps are performed according to the SOP.

   - Assess sequencing data quality and generate QC reports summarising key metrics for each run.
   
   - Identify and escalate QC issues with sequencing runs or individual samples to senior laboratory staff for review and potential resequencing.
   
   - Maintain accurate documentation of QC results and pipeline performance for audit and reporting purposes.

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Roles & Responsibilities

   Add content for training procedure roles here.

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Roles & Responsibilities

   Add content for lab procedure roles here.

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Roles & Responsibilities

   Add content for code update & review procedure roles here.

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Roles & Responsibilities

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
