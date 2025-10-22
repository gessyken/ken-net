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
    try:
        project_path = os.path.join(get_desktop_path(), project_name)
        os.makedirs(project_path, exist_ok=True)
    except Exception as e:
        print(f"Erreur lors de la creation du projet: {e}")

def create_assets_folder(project_name, barre):
    barre.set_description("Creation du dossier assets ...")
    try:
        assets_path = os.path.join(get_desktop_path(), project_name, "assets")
        os.makedirs(assets_path, exist_ok=True)
    except Exception as e:
        print(f"Erreur lors de la creation du dossier assets: {e}")

def create_medias_folder(project_name, barre):
    barre.set_description("Creation du dossier medias ...")
    try:
        medias_path = os.path.join(get_desktop_path(), project_name, "medias")
        os.makedirs(medias_path, exist_ok=True)
    except Exception as e:
        print(f"Erreur lors de la creation du dossier medias: {e}")

def create_css_folder(project_name, barre):
    barre.set_description("Creation du dossier css ...")
    try:
        css_path = os.path.join(get_desktop_path(), project_name, "assets", "css")
        os.makedirs(css_path, exist_ok=True)
    except Exception as e:
        print(f"Erreur lors de la creation du dossier css: {e}")

def create_js_folder(project_name, barre):
    barre.set_description("Creation du dossier js ...")
    try:
        js_path = os.path.join(get_desktop_path(), project_name, "assets", "js")
        os.makedirs(js_path, exist_ok=True)
    except Exception as e:
        print(f"Erreur lors de la creation du dossier js: {e}")


# Creation des fichiers du projet

def create_index_html_file(project_name, barre):
    barre.set_description("Creation du fichier index.html ...")
    try:
        project_path = os.path.join(get_desktop_path(), project_name)
        shutil.copy("index.html", project_path)
    except Exception as e:
        print(f"Erreur lors de la creation du fichier index.html: {e}")
    
def create_style_css_file(project_name, barre):
    barre.set_description("Creation du fichier style.css ...")
    try:
        css_file_path = os.path.join(get_desktop_path(), project_name, "assets", "css", "style.css")
        with open(css_file_path, 'w') as f:
            f.write(contenu_css)
    except Exception as e:
        print(f"Erreur lors de la creation du fichier style.css: {e}")

def create_main_js_file(project_name, barre):
    barre.set_description("Creation du fichier main.js ...")
    try:
        js_file_path = os.path.join(get_desktop_path(), project_name, "assets", "js", "main.js")
        with open(js_file_path, 'w') as f:
            f.write(contenu_js)
    except Exception as e:
        print(f"Erreur lors de la creation du fichier main.js: {e}")

def create_bootstrap_css_file(project_name, barre):
    barre.set_description("Insertion de bootstrap css ...")
    try:
        css_dest_path = os.path.join(get_desktop_path(), project_name, "assets", "css")
        shutil.copy("assets/css/bootstrap.min.css", css_dest_path)
    except Exception as e:
        print(f"Erreur lors de la copie de bootstrap css: {e}")

def create_bootstrap_js_file(project_name, barre):
    barre.set_description("Insertion de bootstrap js ...")
    try:
        js_dest_path = os.path.join(get_desktop_path(), project_name, "assets", "js")
        shutil.copy("assets/js/bootstrap.min.js", js_dest_path)
    except Exception as e:
        print(f"Erreur lors de la copie de bootstrap js: {e}")

def copy_media_images(project_name, barre):
    barre.set_description("Insertion des medias ...")
    try:
        medias_dest_path = os.path.join(get_desktop_path(), project_name, "medias")
        shutil.copy("medias/ken-net.png", medias_dest_path)
    except Exception as e:
        print(f"Erreur lors de la copie des medias: {e}")

def copy_readme_file(project_name, barre):
    barre.set_description("Insertion du readme ...")
    try:
        project_path = os.path.join(get_desktop_path(), project_name)
        shutil.copy("README.md", project_path)
    except Exception as e:
        print(f"Erreur lors de la copie du readme: {e}")

def git_init(project_name):
    try:
        project_path = os.path.join(get_desktop_path(), project_name)
        os.chdir(project_path)
        os.system("git init")
    except Exception as e:
        print(f"Erreur lors de l'initialisation Git: {e}")

def start_server(project_name):
    try:
        project_path = os.path.join(get_desktop_path(), project_name)
        os.chdir(project_path)
        handler = http.server.SimpleHTTPRequestHandler
        
        # Essayer plusieurs ports si 8000 est occupé
        ports = [8000, 8001, 8002, 8003, 8004]
        for port in ports:
            try:
                with socketserver.TCPServer(("", port), handler) as httpd:
                    print(f"Serveur demarre sur le port {port}")
                    httpd.serve_forever()
                break
            except OSError:
                if port == ports[-1]:  # Dernier port essayé
                    raise
                continue
    except Exception as e:
        print(f"Erreur lors du demarrage du serveur: {e}")
