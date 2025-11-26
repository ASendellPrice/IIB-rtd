Cross-References
----------------

.. important::
   This section is a fundamental building block of any SOP

The 'Cross-References' section of an SOP should list other controlled documents that support or relate to the procedure. Cross-references ensure that users can easily identify associated SOPs, validation documents, and equipment instructions necessary for performing the procedure correctly.

Depending on the procedure, cross-references may include:

- **Associated SOPs:** Related procedures that describe upstream or downstream processes, such as wet-lab procedures or reporting workflows.

- **Validation and verification documents:** References to documents establishing the analytical performance, accuracy, and reproducibility of the pipeline or procedure.  

- **Equipment or instrument SOPs:** Instructions for using specific laboratory instruments or software platforms required for the procedure.

- **Guidelines and standards:** Relevant internal or external guidelines, such as laboratory standards, regulatory requirements, or best practice documents.

.. attention::
   If the organisation does not have an electronic document management system (eQMS), cross-references should include version numbers and revision dates to ensure users access the correct version.

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics QC Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Cross-References

   The following documents support or are directly related to this procedure:

   +----------------+------------------------------------------------------------------------+------------+------------+
   | SOP Index      | Title                                                                  | Version    | Date       |
   +================+========================================================================+============+============+
   | SOP011         | Overview of HIV Characterisation for Resistance Mutations by NGS       | v1.2       | 2023-05-15 |
   +----------------+------------------------------------------------------------------------+------------+------------+
   | SOP045         | Using the NextSeq 550                                                  | v3.0       | 2022-11-10 |
   +----------------+------------------------------------------------------------------------+------------+------------+
   | SOP001EVV      | Validation of HIV Resistance Testing by NGS                            | v2.1       | 2023-01-20 |
   +----------------+------------------------------------------------------------------------+------------+------------+

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Cross-References

   Add text here.

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Cross-References

   Add text here.

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Cross-References

   The following documents support or are directly related to this procedure:

   +-------------------------+---------------------------------------------------------+------------+
   | SOP Index               | Title                                                   | Version    |
   +=========================+=========================================================+============+
   | DOC-ADVISOEXAMPLE-001   | LGU standards guidelines for Python                     | v1.2       |
   +-------------------------+---------------------------------------------------------+------------+
   | DOC-ADVISOEXAMPLE-002   | LGU standards guidelines for Nextflow                   | v1.2       |
   +-------------------------+---------------------------------------------------------+------------+

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Cross-references

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
