.. _sop_guide_resources_tools:

Resources & Tools
=================

.. important::

  Use **either** the *Resources & Tools* section (for desk-based procedures) **or** the :ref:`Equipment & Reagents <sop_guide_equipment_reagents>` section (for laboratory procedures).

This section should list all resources and tools required to carry out the procedure. It ensures that users have access to the necessary infrastructure, information, and permissions before starting.

Depending on the procedure, this may include:

- **Software:** Applications, platforms, or tools required (e.g., computer software, analysis platforms, training systems etc).

- **Data & Information Sources:** Databases, datasets, records, or reference materials needed to complete the task.

- **Access Requirements:** Permissions, accounts, or network access necessary to use the resources.

- **Documentation & Guidance:** Manuals, policies, guidelines, or online references that support correct use of tools.

- **Hardware:** Computers, servers, workstations, or other devices required for the procedure.

-------

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

  *Example SOP content for a bioinformatics QC procedure*

  .. rubric:: Resources & Tools

  The following equipment and software are required to perform quality control of sequencing datasets:
  
  **Hardware:**

  - PC or equivalent workstation capable of accessing the laboratory’s production server.

  **Software:**
  
  - SSH client software (e.g. PuTTY, Windows Subsytem for Linux (WSL), MobaXterm) for connecting to the laboratory’s production server.
  
  - Production version of the QC pipeline installed and configured on the production server.
  
  **Network access:** 
  
  - Access to the laboratory’s network with the sequence server mapped as a network drive.

  - User account with adequate permissions to read/write sequencing data and QC outputs.

.. dropdown:: 👩‍🔬 Training Procedure

  *Example SOP content for a training procedure*

  .. rubric:: Resources & Tools

  Add content for training procedure resources here.

.. dropdown:: 🧪 Laboratory Procedure

  This section is **not suitable** for laboratory procedures. Please use the :ref:`Equipment & Reagents <sop_guide_equipment_reagents>` section instead.

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
