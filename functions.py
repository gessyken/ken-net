import os, time

# Creation des varaibles contenant les contenus des fichiers su projet

contenu_html_index = " // Ici votre html" 

contenu_css = " // Ici votre css personalise  "

contenu_js = " // Ici votre Javascript personalise "

# Creation des dossiers (structure d'un projet KEN-NET)

def create_project_main_folder(project_name, barre):
    barre.set_description("Creation du project ...")
    os.system("mkdir ~/Bureau/" + project_name)

def create_assets_folder(project_name, barre):
    barre.set_description("Creation du dossier assets ...")
    os.system("mkdir ~/Bureau/" + project_name + "/assets")

def create_medias_folder(project_name, barre):
    barre.set_description("Creation du dossier medias ...")
    os.system("mkdir ~/Bureau/" + project_name + "/medias")

def create_css_folder(project_name, barre):
    barre.set_description("Creation du dossier css ...")
    os.system("mkdir ~/Bureau/" + project_name + "/assets/css")

def create_js_folder(project_name, barre):
    barre.set_description("Creation du dossier js ...")
    os.system("mkdir ~/Bureau/" + project_name + "/assets/js")


# Creation des fichiers du projet

def create_index_html_file(project_name, barre):
    barre.set_description("Creation du fichier index.html ...")
    os.system("cp index.html ~/Bureau/{}/".format(project_name))
    
def create_style_css_file(project_name, barre):
    barre.set_description("Creation du fichier style.css ...")
    os.system("echo {} > ~/Bureau/{}/assets/css/style.css".format(contenu_css, project_name))

def create_main_js_file(project_name, barre):
    barre.set_description("Creation du fichier main.js ...")
    os.system("echo {} > ~/Bureau/{}/assets/js/main.js".format(contenu_js, project_name))

def create_bootstrap_css_file(project_name, barre):
    barre.set_description("Insertion de bootstrap css ...")
    os.system("cp assets/css/bootstrap.min.css ~/Bureau/{}/assets/css/".format(project_name))

def create_bootstrap_js_file(project_name, barre):
    barre.set_description("Insertion de bootstrap js ...")
    os.system("cp assets/js/bootstrap.min.js ~/Bureau/{}/assets/js/".format(project_name))

def copy_media_images(project_name, barre):
    barre.set_description("Insertion des medias ...")
    os.system("cp medias/ken-net.png ~/Bureau/{}/medias/".format(project_name))

def copy_readme_file(project_name, barre):
    barre.set_description("Insertion du readme ...")
    os.system("cp Readme.md ~/Bureau/{}/".format(project_name))

def git_init(project_name):
    os.system("cd  ~/Bureau/{}/ && git init".format(project_name))

def start_server(project_name):
    os.system("cd  ~/Bureau/{}/ && php -S 127.0.0.1:8000".format(project_name))
