import pandas as pd

# Define color mapping for ontology prefixes
ontology_colors = {
    "mesh": "primary",
    "NCIT": "danger",
    "OBI": "success",
    "SIO": "warning",
    "OBCS": "info",
    "default": "secondary"
}

# Load glossary intro text
with open("resources/glossary_intro_text.txt", "r") as intro_file:
    intro_text = intro_file.read()

# Load Excel file containing terms to include and their definitions etc
df = pd.read_excel("resources/iso_terms.xlsx")

# Create output RST file
with open("docs/source/glossary.rst", "w", encoding="utf-8") as f:
    f.write(intro_text + "\n\n")

    # Inject search box
    f.write(".. raw:: html\n\n")
    f.write('   <input type="text" id="glossarySearch" placeholder="Search glossary..." style="width: 100%; padding: 8px; margin-bottom: 16px; font-size: 1em;">\n\n')

    for _, row in df.iterrows():
        term = str(row.get("Term", "")).strip()
        definition = str(row.get("Definition", "")).strip()
        example = str(row.get("Example usage", "")).strip()
        bio_def = str(row.get("Bioinformatics translation", "")).strip()
        bio_example = str(row.get("Bioinformatics example sentence", "")).strip()
        ontology_refs = str(row.get("Ontological reference(s)", "")).strip()
        ontology_links = str(row.get("Link to reference", "")).strip()

        # Write dropdown block
        f.write(f".. dropdown:: {term}\n\n")
        f.write(f"   {definition}\n\n")

        if example:
            f.write(f"   **Example usage:**  \n   *“{example}”*\n\n")

        if bio_def and bio_def.lower() != "nan":
            f.write(f"   .. admonition:: **💻 Bioinformatics translation**\n      :class: tip\n\n")
            f.write(f"      {bio_def}\n\n")
            if bio_example and bio_example.lower() != "nan":
                f.write(f"      **Example usage:**  \n      *“{bio_example}”*\n\n")

        # Format ontology pills using raw HTML (inline layout)
        if (
            ontology_refs
            and ontology_links
            and ontology_refs.lower() != "nan"
            and ontology_links.lower() != "nan"
        ):
            ref_items = [r.strip() for r in ontology_refs.split("|")]
            link_items = [l.strip() for l in ontology_links.split("|")]

            if len(ref_items) == len(link_items) and all(ref_items) and all(link_items):
                f.write("   **Ontological references:**\n\n")
                f.write("   .. raw:: html\n\n")
                f.write("      ")
                for ref, link in zip(ref_items, link_items):
                    if "[" in ref and "]" in ref:
                        label = ref.split("[")[0].strip()
                        ont_def = ref.split("[")[1].strip(" ]")
                        prefix = label.split(":")[0].strip()
                        color = ontology_colors.get(prefix, ontology_colors["default"])
                        html = f'<a class="sd-badge sd-bg-{color} sd-text-white" href="{link}" title="{ont_def}">{label}</a>'
                        f.write(f"{html} ")
                f.write("\n\n")

    # Inject JavaScript for live filtering
    f.write(".. raw:: html\n\n")
    f.write("""   <script>
     document.getElementById('glossarySearch').addEventListener('input', function () {
       const query = this.value.toLowerCase();
       const dropdowns = document.querySelectorAll('.dropdown');
       dropdowns.forEach(drop => {
         const label = drop.querySelector('.dropdown-title');
         if (label && label.textContent.toLowerCase().includes(query)) {
           drop.style.display = '';
         } else {
           drop.style.display = 'none';
         }
       });
     });
   </script>\n""")
