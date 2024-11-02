import os
import re

def generate_projects_html(projects_directory, template_file="projects/template_projects.html", output_file="projects.html"):
    # Lecture du fichier template pour projects.html
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    # Contenu HTML dynamique pour les projets
    projects_content = ""

    # Parcours de chaque dossier de projet
    for project_folder in sorted(os.listdir(projects_directory)):
        project_path = os.path.join(projects_directory, project_folder)

        # S'assurer qu'il s'agit bien d'un dossier
        if os.path.isdir(project_path):
            # Chemin de l'image principale
            image_path = os.path.join(project_path, "main_image.jpg")
            # Chemin du fichier de titre
            title_path = os.path.join(project_path, "title.txt")

            # Vérifie l'existence de l'image principale
            if os.path.exists(image_path):
                # Lecture et formatage du titre
                title = ""
                if os.path.exists(title_path):
                    with open(title_path, "r", encoding="utf-8") as f:
                        title = f.read().strip()

                # Formattage du titre pour le nom de fichier
                formatted_title = re.sub(r'\s+', '-', title.lower())
                formatted_title = re.sub(r'[^\w\-]', '', formatted_title)  # Supprime caractères spéciaux

                # Ajout du HTML pour chaque projet en tant que lien
                projects_content += f"""
        <a href="{formatted_title}.html" class="project" id="{project_folder}">
            <h1 class="project-title">{title}</h1>
            <img src="{os.path.join('projects', project_folder, 'main_image.jpg')}" alt="{title}" class="project-image">
        </a>
                """

    # Remplace le marqueur dans le template par le contenu des projets
    final_html = template_html.replace("{{ projects_content }}", projects_content)

    # Écriture dans le fichier HTML final pour projects
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"{output_file} généré avec succès.")

def generate_about_html(about_directory, template_file="about/template_about.html", output_file="about.html"):
    # Lecture du fichier template pour about.html
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    # Lecture du fichier texte pour le contenu de la page
    description_path = os.path.join(about_directory, "description.txt")
    description_content = ""
    if os.path.exists(description_path):
        with open(description_path, "r", encoding="utf-8") as f:
            description_content = f.read().strip()

    # Définition du chemin de l'image
    image_path = os.path.join(about_directory, "picture.jpeg")
    image_src = os.path.join(about_directory, "picture.jpeg") if os.path.exists(image_path) else ""

    # Remplacement des marqueurs dans le template pour about.html
    final_html = template_html.replace("{{ description_content }}", description_content)
    final_html = final_html.replace("{{ image_src }}", image_src)

    # Écriture dans le fichier HTML final pour about
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"{output_file} généré avec succès.")


# Appels des fonctions pour générer les fichiers HTML
generate_projects_html("projects")
generate_about_html("about")
