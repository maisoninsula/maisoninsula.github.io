import os

# Chemins vers les fichiers
description_file = "about/description.txt"
template_file = "about/template_about.html"
output_html_file = "about.html"

# Lire le contenu du fichier description.txt
with open(description_file, 'r', encoding='utf-8') as file:
    description_content = file.read()

# Lire le template HTML
with open(template_file, 'r', encoding='utf-8') as file:
    html_template = file.read()

# Remplacer les placeholders dans le template
html_content = html_template.replace("{{description}}", description_content)

# Écrire le fichier HTML généré
with open(output_html_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"{output_html_file} a été généré avec succès.")
