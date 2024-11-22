import os
import re

def generate_projects_html(projects_directory, template_file="projects/template_projects.html", output_file="projects.html"):
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    projects_content = ""
    project_folders = sorted(os.listdir(projects_directory), reverse=True)

    for project_folder in project_folders:
        project_path = os.path.join(projects_directory, project_folder)

        if os.path.isdir(project_path):
            title = project_folder.split('.', 1)[-1].replace('-', ' ')
            formatted_title = re.sub(r'\s+', '-', title.lower())
            formatted_title = re.sub(r'[^\w\-]', '', formatted_title)
            image_path = os.path.join(project_path, "01.jpg")

            if os.path.exists(image_path):
                projects_content += f"""
        <a href="{formatted_title}.html" class="project" id="{project_folder}">
            <p class="project-title" style="text-align: center;">{title}</p>
            <img src="{os.path.join('projects', project_folder, '01.jpg')}" alt="{title}" class="project-image">
        </a>
                """
                generate_project_page(project_path, formatted_title, title)

    final_html = template_html.replace("{{ projects_content }}", projects_content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"{output_file} généré avec succès.")

def generate_project_page(project_path, formatted_title, title, template_file="projects/template_project.html"):
    # Lire le template de la page de projet
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()

    description_file = os.path.join(project_path, "description.txt")
    description = ""

    if os.path.exists(description_file):
        with open(description_file, "r", encoding="utf-8") as f:
            description = f.read().strip()

    valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}
    images = [
        img for img in sorted(os.listdir(project_path))
        if os.path.splitext(img)[1].lower() in valid_extensions
    ]

    slider_images_html = "\n".join(
        f'<img src="{os.path.join("projects", os.path.basename(project_path), img)}" alt="Image {i+1}" class="slider-image{" active" if i == 0 else ""}" onclick="openLightbox({i})">'
        for i, img in enumerate(images)
    )

    # Remplacer les marqueurs dans le template par les données spécifiques au projet
    project_html = template_html
    project_html = project_html.replace("{{ project_title }}", title.capitalize())
    project_html = project_html.replace("{{ project_description }}", description)
    project_html = project_html.replace("{{ slider_images }}", slider_images_html)

    project_file = f"{formatted_title}.html"
    with open(project_file, "w", encoding="utf-8") as f:
        f.write(project_html)

    print(f"{project_file} généré avec succès.")

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
