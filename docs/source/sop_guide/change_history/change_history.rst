Change History
==============

.. important::
   **Recording of change history is a requirement under ISO 15189:2022 (Management System Requirements, Document Control).** This section should therefore be included in an SOP if the laboratory/organisation does not make use of an electronic Quality Management System (eQMS) that records changes to controlled documents.

The 'Change History' section of an SOP consists of a list of entries detailing the changes made since the publication of version 1 of a controlled document. Each entry should record:

- Whether the change was *minor* or *major*:
   - **Minor change:** Any minimal update that does not alter the meaning or intent of the SOP 
     (e.g. typographical corrections, formatting adjustments, clarifications of wording).
   - **Major change:** Any substantive update that affects the procedure, responsibilities, or scope of the SOP.
- The **date of the change**.
- The **version implemented**.
- The **authorising person/role**.

.. note::
  Consider implementing a **threshold rule** for classifying changes. For example, if 10 minor change requests have been accumulated since the last major version, the next update must be classified as a *major change* and a new version number assigned.

-------

**Example content:**

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
