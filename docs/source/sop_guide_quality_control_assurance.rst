Quality Control & Verification
==============================

This section should outline the quality control (QC) measures and verification steps implemented to ensure the accuracy, reliability, and reproducibility of the procedure described in the SOP. Clear documentation of QC practices helps maintain confidence in results and supports compliance with regulatory and accreditation standards.

This section may include:

- **Control Samples:** Use positive and negative controls, as well as samples of known characteristics (e.g. variant types, resistance markers, reference strains) to verify that the procedure consistently produces expected results.

- **Internal Quality Assurance (IQA) and External Quality Assurance (EQA):** Document participation in internal QC programs (e.g. repeatability checks, peer review of results) and external proficiency testing schemes to benchmark performance against other laboratories or organisations.

- **Software and Code Verification:** For computational workflows, include measures such as code review, unit testing, and continuous integration (CI) testing to ensure reproducibility, detect errors early, and maintain compatibility across versions.

- **Verification Procedures:** Outline the steps taken to verify the pipeline's performance.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Verification & Quality Control
   
   Quality control checks are integrated at multiple stages of the pipeline to ensure data integrity and accuracy of results. Key QC measures include:
   
   - **Input Data QC:** Raw sequencing reads undergo quality assessment using FastQC to evaluate metrics such as per-base sequence quality, GC content, and adapter contamination. Samples failing to meet predefined quality thresholds are flagged for review.
   
   - **Read Mapping QC:** Post-mapping statistics are generated using ...
  
   - **Variant Calling QC:** Variant calls are filtered based on quality scores, read depth, and allele frequency thresholds to minimize false positives. A minimum read depth of 30x and variant quality score of 20 are enforced.
   
   - **Pipeline Verification:** The pipeline is regularly validated using control datasets with known variants to ensure consistent performance. Discrepancies between expected and observed results trigger a review of pipeline parameters and software versions.
   
   - **Positive and Negative Controls:** Each batch of samples processed includes positive controls with known resistance mutations and negative controls to monitor for contamination and ensure the accuracy of variant detection.

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Verification & Quality Control
   
   Add content

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Verification & Quality Control
   
   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Verification & Quality Control
   
   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Verification & Quality Control
   
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
