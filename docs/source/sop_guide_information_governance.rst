Information Governance
======================

.. important::
  This section must be included in SOPs where data containing personally identifiable information (PII), genetic data, or other sensitive information is accessed, generated, or stored. It ensures compliance with institutional policies, legal frameworks, and ethical standards.

The 'Information Governance' section of an SOP should outline how information generated, accessed, or stored during the procedure is handled. Depending on the procedure, this may include:

- **Data Protection & Privacy:** Specify how personal or sensitive data is handled in line with relevant regulations (e.g., GDPR in the UK/EU, HIPAA in the US etc.).
- **Genetic Data Governance:** Define how genomic sequences, variant data, and metadata are stored, anonymised, and shared.
- **Confidentiality:** Define who has access to the information and how confidentiality is maintained.
- **Access Control:** State what permissions, accounts, or authentication are required to access data or systems.
- **Retention & Disposal:** Outline how long data must be retained and the approved methods for secure disposal.
- **Audit & Traceability:** Describe how information use is logged, monitored, and traceable for compliance purposes.
- **Ethical Use:** Ensure information is used only for its intended purpose (e.g., surveillance, diagnostics, research) and in accordance with institutional policies.
- **Third-Party Systems:** Identify any external platforms or services used (e.g., GISAID, NCBI), and confirm compliance with contractual or legal obligations.

-------

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*
   
   .. rubric:: Information governance
   
   Patient and sequencing data must be handled in accordance with Information Governance and Data Protection policies. Personally identifiable information (PII) must never be stored outside secure, access-controlled systems (e.g., LIMS). Data transfers must occur only via approved, encrypted connections, and users must ensure that all analysis systems and accounts are password-protected and access-controlled.

.. dropdown:: 👩‍🔬 Staff Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Information governance
   
   Add content

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Information governance
   
   Add content

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Information governance
   
   Add content

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Information governance
   
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
