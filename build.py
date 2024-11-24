import os
import re

def generate_projects_html(projects_directory, template_file="projects/template_projects.html", output_file="projects.html"):
    # Charger le template pour projects.html
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    projects_content = ""
    project_folders = sorted(os.listdir(projects_directory), reverse=True)

    # Préparer une liste pour gérer la logique de bouclage
    projects = []
    for project_folder in project_folders:
        if os.path.isdir(os.path.join(projects_directory, project_folder)):
            title = project_folder.split('.', 1)[-1].replace('-', ' ')
            formatted_title = re.sub(r'\s+', '-', title.lower())
            formatted_title = re.sub(r'[^\w\-]', '', formatted_title)
            projects.append({"folder": project_folder, "title": title, "url": f"{formatted_title}.html"})

    # Boucle pour générer chaque projet
    for i, project in enumerate(projects):
        project_path = os.path.join(projects_directory, project["folder"])
        next_project = projects[(i + 1) % len(projects)]  # Boucle vers le premier projet
        image_path = os.path.join(project_path, "01.jpg")

        if os.path.exists(image_path):
            projects_content += f"""
        <a href="{project['url']}" class="project" id="{project['folder']}">
            <p class="project-title" style="text-align: center;">{project['title']}</p>
            <img src="{os.path.join('projects', project['folder'], '01.jpg')}" alt="{project['title']}" class="project-image">
        </a>
            """
            generate_project_page(project_path, project["url"].replace(".html", ""), project["title"], next_project)

    # Remplacer le contenu dynamique dans projects.html
    final_html = template_html.replace("{{ projects_content }}", projects_content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"{output_file} généré avec succès.")

def generate_project_page(project_path, formatted_title, title, next_project):
    template_file = "projects/template_project.html"

    # Charger le template
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    # Récupérer le contenu du fichier description.txt
    description_file = os.path.join(project_path, "description.txt")
    description = ""
    if os.path.exists(description_file):
        with open(description_file, "r", encoding="utf-8") as f:
            description = f.read().strip()

    # Récupérer les images
    images = [
        file_name for file_name in os.listdir(project_path)
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]
    slider_images = "\n".join(
        f'<img src="{os.path.join("projects", os.path.basename(project_path), image)}" alt="Image {i + 1}" class="slider-image{" active" if i == 0 else ""}" onclick="openLightbox({i})">'
        for i, image in enumerate(sorted(images))
    )

    # Lien vers le projet suivant
    next_project_html = f'<a href="{next_project["url"]}" class="next-project-link">Projet suivant</a>'

    # Remplacer les variables dans le template
    final_html = template_html.replace("{{ project_title }}", title.capitalize())
    final_html = final_html.replace("{{ project_description }}", description)
    final_html = final_html.replace("{{ slider_images }}", slider_images)
    final_html = final_html.replace("{{ next_project_link }}", next_project_html)

    # Nom du fichier HTML pour le projet
    output_file = f"{formatted_title}.html"

    # Sauvegarder le fichier
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

def generate_contact_html(contact_directory, template_file="contact/template_contact.html", output_file="contact.html"):
    # Lecture du fichier template pour about.html
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    # Lecture du fichier texte pour le contenu de la page
    description_path = os.path.join(contact_directory, "description.txt")
    description_content = ""
    if os.path.exists(description_path):
        with open(description_path, "r", encoding="utf-8") as f:
            description_content = f.read().strip()

    # Définition du chemin de l'image
    image_path = os.path.join(contact_directory, "picture.jpeg")
    image_src = os.path.join(contact_directory, "picture.jpeg") if os.path.exists(image_path) else ""

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
generate_contact_html("contact")
