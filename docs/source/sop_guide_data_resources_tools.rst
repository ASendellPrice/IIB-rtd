Resources & Tools
=================

.. important::
  Add note

The 'Resources & Tools' section of an SOP should detail all resources and tools needed to carry out the procedure. Depending on the nature of the procedure, this may include:

- **Equipment:** Any hardware, instruments, or devices required to perform the procedure.

- **Software:** Any software applications, platforms, or tools necessary for the procedure.

- **Reference Data:** Any databases, reference genomes, or datasets required for analysis.

- **Access Requirements:** Any necessary permissions, accounts, or network access needed to use the resources.

- **Consumables:** Any reagents, kits, or materials required for the procedure (more relevant for lab-based SOPs).

-----

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

   *Example SOP content for a bioinformatics pipeline for detecting HIV antiviral resistance*

   .. rubric:: Resources & Tools

   The following equipment, software, and reference data are required to perform this procedure:

   - **Computer hardware:** PC or equivalent workstation capable of accessing the sequence server.

   - **Software:** SSH client software such as PuTTY, MobaXterm, or Windows Subsystem for Linux (WSL) for connecting to the laboratory’s sequence server.

   - **Network access:** Access to the laboratory’s network with the sequence server mapped as a network drive.

   - **Internet access:** Required to access the Stanford HIV Drug Resistance Database (https://hivdb.stanford.edu/). This database is selected because it is the current internationally recognised gold standard for HIV drug resistance typing.

.. dropdown:: 👩‍🔬 Training Procedure

   *Example SOP content for a training procedure*

   .. rubric:: Resources & Tools

   Add content for training procedure resources here.

.. dropdown:: 🧪 Laboratory Procedure

   *Example SOP content for a nucleic acid extraction procedure*

   .. rubric:: Resources & Tools

   Add content for lab procedure resources here.

.. dropdown:: 💻 Code Update & Review Procedure

   *Example SOP content for a code update and review procedure*

   .. rubric:: Resources & Tools

   The following hardware and software are required to perform this procedure: 

   - **Computer hardware:** PC or equivalent workstation that has access to the internet and the organisation version control platform (Gitlab).
   
   - **Software:** A text editor capable of making changes to code and committing them back to version control (e.g., VSCode); a web-browser capable of connecting to the organisation VCS (Gitlab).

.. dropdown:: ✅ Verification Procedure

   *Example SOP content for a verification procedure*

   .. rubric:: Resources & Tools

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
