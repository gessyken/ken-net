import os, time, shutil, http.server, socketserver

# Creation des varaibles contenant les contenus des fichiers su projet

contenu_html_index = " // Ici votre html" 

contenu_css = " // Ici votre css personalise  "

contenu_js = " // Ici votre Javascript personalise "

# Fonction pour obtenir le chemin du bureau sur tous les OS
def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Creation des dossiers (structure d'un projet KEN-NET)

def create_project_main_folder(project_name, barre):
    barre.set_description("Creation du project ...")
    project_path = os.path.join(get_desktop_path(), project_name)
    os.makedirs(project_path, exist_ok=True)

def create_assets_folder(project_name, barre):
    barre.set_description("Creation du dossier assets ...")
    assets_path = os.path.join(get_desktop_path(), project_name, "assets")
    os.makedirs(assets_path, exist_ok=True)

def create_medias_folder(project_name, barre):
    barre.set_description("Creation du dossier medias ...")
    medias_path = os.path.join(get_desktop_path(), project_name, "medias")
    os.makedirs(medias_path, exist_ok=True)

def create_css_folder(project_name, barre):
    barre.set_description("Creation du dossier css ...")
    css_path = os.path.join(get_desktop_path(), project_name, "assets", "css")
    os.makedirs(css_path, exist_ok=True)

def create_js_folder(project_name, barre):
    barre.set_description("Creation du dossier js ...")
    js_path = os.path.join(get_desktop_path(), project_name, "assets", "js")
    os.makedirs(js_path, exist_ok=True)


# Creation des fichiers du projet

def create_index_html_file(project_name, barre):
    barre.set_description("Creation du fichier index.html ...")
    project_path = os.path.join(get_desktop_path(), project_name)
    shutil.copy("index.html", project_path)
    
def create_style_css_file(project_name, barre):
    barre.set_description("Creation du fichier style.css ...")
    css_file_path = os.path.join(get_desktop_path(), project_name, "assets", "css", "style.css")
    with open(css_file_path, 'w') as f:
        f.write(contenu_css)

def create_main_js_file(project_name, barre):
    barre.set_description("Creation du fichier main.js ...")
    js_file_path = os.path.join(get_desktop_path(), project_name, "assets", "js", "main.js")
    with open(js_file_path, 'w') as f:
        f.write(contenu_js)

def create_bootstrap_css_file(project_name, barre):
    barre.set_description("Insertion de bootstrap css ...")
    css_dest_path = os.path.join(get_desktop_path(), project_name, "assets", "css")
    shutil.copy("assets/css/bootstrap.min.css", css_dest_path)

def create_bootstrap_js_file(project_name, barre):
    barre.set_description("Insertion de bootstrap js ...")
    js_dest_path = os.path.join(get_desktop_path(), project_name, "assets", "js")
    shutil.copy("assets/js/bootstrap.min.js", js_dest_path)

def copy_media_images(project_name, barre):
    barre.set_description("Insertion des medias ...")
    medias_dest_path = os.path.join(get_desktop_path(), project_name, "medias")
    shutil.copy("medias/ken-net.png", medias_dest_path)

def copy_readme_file(project_name, barre):
    barre.set_description("Insertion du readme ...")
    project_path = os.path.join(get_desktop_path(), project_name)
    shutil.copy("README.md", project_path)

def git_init(project_name):
    project_path = os.path.join(get_desktop_path(), project_name)
    os.chdir(project_path)
    os.system("git init")

def start_server(project_name):
    project_path = os.path.join(get_desktop_path(), project_name)
    os.chdir(project_path)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        httpd.serve_forever()
