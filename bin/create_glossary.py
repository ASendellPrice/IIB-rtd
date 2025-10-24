import pandas as pd

# Load glossary intro text
with open("resources/glossary_intro_text.txt", "r") as intro_file:
    intro_text = intro_file.read()

# Load Excel file containing terms to include and their definitions etc
df = pd.read_excel("resources/iso_terms.xlsx")

# Create output RST file
with open("docs/source/glossary.rst", "w") as f:
    f.write(intro_text + "\n")

    for _, row in df.iterrows():
        term = row["Term"]
        definition = row["Definition"]
        example = row["Example usage"]
        bio_def = row.get("Bioinformatics translation", "")
        bio_example = row.get("Bioinformatics example sentence", "")

        # Write dropdown block
        f.write(f".. dropdown:: {term}\n   :open:\n\n")
        f.write(f"   {definition.strip()}\n\n")
        f.write(f"   **Example usage:**  \n   {example.strip()}\n\n")

        if bio_def:
            f.write(f"   .. admonition:: **💻 Bioinformatics translation**\n      :class: tip\n\n")
            f.write(f"      {bio_def}\n\n")
            if bio_example:
                f.write(f"      **Example usage:**  \n      *“{bio_example}”*\n\n")
