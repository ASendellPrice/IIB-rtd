.. _sop_guide_equipment_reagents:

Equipment & Reagents
====================

.. important::

   This section is suitable for laboratory procedures. For desk-based procedures use the :ref:`Resources & Tools <sop_guide_resources_tools>` section instead.

This section should list all physical items required to perform the procedure, ensuring compliance with safety standards and proper preparation before starting.

Depending on the procedure, this may include:

- **Equipment:** Instruments or devices required (e.g., centrifuges, pipettes, PCR thermocyclers, sequencing platforms, etc.).

- **Consumables:** Reagents, kits, or materials consumed during the procedure.

- **Personal Protective Equipment (PPE):** Gloves, lab coats, goggles, or other safety gear.

- **Calibration/Validation Requirements:** Any checks or certifications needed before equipment use.

- **Storage Conditions:** Requirements for reagents or materials (e.g., refrigeration, light protection).

- **Waste Disposal:** Procedures for safe disposal of reagents, consumables, or contaminated materials.

-------

.. rubric:: Example content:

.. dropdown:: 🧬 Bioinformatics Procedure

  This section is **not suitable** for laboratory procedures. Please use the `Resources & Tools <sop_guide_resources_tools>` section instead.

.. dropdown:: 👩‍🔬 Training Procedure
  
  *Example SOP content for a training procedure*

  .. rubric:: Equipment & Reagents
  
  Add content for training procedure here.

.. dropdown:: 🧪 Laboratory Procedure

  *Example SOP content for a laboratory procedure*

  .. rubric:: Equipment & Reagents
  
  Add content for laboratory procedure here.

.. dropdown:: 💻 Code Update & Review Procedure

  *Example SOP content for a code update and review procedure*
  
  This section is **not suitable** for a code update and review procedure. Please use the :ref:`Equipment & Reagents <sop_guide_equipment_reagents>` section instead.

.. dropdown:: ✅ Verification Procedure

  This section is **not suitable** for verification and validation procedures. Please use the `Resources & Tools <sop_guide_resources_tools>` section instead.

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
