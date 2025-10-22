import os, time, shutil, http.server, socketserver

# Creation des varaibles contenant les contenus des fichiers su projet

contenu_html_index = " // Your HTML here" 

contenu_css = " // Your custom CSS here"

contenu_js = " // Your custom JavaScript here"

# Fonction pour obtenir le chemin du bureau sur tous les OS
def get_desktop_path(custom_path=None):
    if custom_path:
        return custom_path
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Creation des dossiers (structure d'un projet KEN-NET)

def create_project_main_folder(project_name, barre, custom_path=None):
    barre.set_description("Creating project ...")
    try:
        project_path = os.path.join(get_desktop_path(custom_path), project_name)
        os.makedirs(project_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating project: {e}")

def create_assets_folder(project_name, barre, custom_path=None):
    barre.set_description("Creating assets folder ...")
    try:
        assets_path = os.path.join(get_desktop_path(custom_path), project_name, "assets")
        os.makedirs(assets_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating assets folder: {e}")

def create_medias_folder(project_name, barre, custom_path=None):
    barre.set_description("Creating medias folder ...")
    try:
        medias_path = os.path.join(get_desktop_path(custom_path), project_name, "medias")
        os.makedirs(medias_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating medias folder: {e}")

def create_css_folder(project_name, barre, custom_path=None):
    barre.set_description("Creating css folder ...")
    try:
        css_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "css")
        os.makedirs(css_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating css folder: {e}")

def create_js_folder(project_name, barre, custom_path=None):
    barre.set_description("Creating js folder ...")
    try:
        js_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "js")
        os.makedirs(js_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating js folder: {e}")


# Creation des fichiers du projet

def create_index_html_file(project_name, barre, custom_path=None):
    barre.set_description("Creating index.html file ...")
    try:
        project_path = os.path.join(get_desktop_path(custom_path), project_name)
        shutil.copy("index.html", project_path)
    except Exception as e:
        print(f"Error creating index.html file: {e}")
    
def create_style_css_file(project_name, barre, custom_path=None):
    barre.set_description("Creating style.css file ...")
    try:
        css_file_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "css", "style.css")
        with open(css_file_path, 'w') as f:
            f.write(contenu_css)
    except Exception as e:
        print(f"Error creating style.css file: {e}")

def create_main_js_file(project_name, barre, custom_path=None):
    barre.set_description("Creating main.js file ...")
    try:
        js_file_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "js", "main.js")
        with open(js_file_path, 'w') as f:
            f.write(contenu_js)
    except Exception as e:
        print(f"Error creating main.js file: {e}")

def create_bootstrap_css_file(project_name, barre, custom_path=None):
    barre.set_description("Copying bootstrap css ...")
    try:
        css_dest_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "css")
        shutil.copy("assets/css/bootstrap.min.css", css_dest_path)
    except Exception as e:
        print(f"Error copying bootstrap css: {e}")

def create_bootstrap_js_file(project_name, barre, custom_path=None):
    barre.set_description("Copying bootstrap js ...")
    try:
        js_dest_path = os.path.join(get_desktop_path(custom_path), project_name, "assets", "js")
        shutil.copy("assets/js/bootstrap.min.js", js_dest_path)
    except Exception as e:
        print(f"Error copying bootstrap js: {e}")

def copy_media_images(project_name, barre, custom_path=None):
    barre.set_description("Copying media files ...")
    try:
        medias_dest_path = os.path.join(get_desktop_path(custom_path), project_name, "medias")
        shutil.copy("medias/ken-net.png", medias_dest_path)
    except Exception as e:
        print(f"Error copying media files: {e}")

def copy_readme_file(project_name, barre, custom_path=None):
    barre.set_description("Insertion du readme ...")
    try:
        project_path = os.path.join(get_desktop_path(custom_path), project_name)
        shutil.copy("README.md", project_path)
    except Exception as e:
        print(f"Error copying readme: {e}")

def git_init(project_name, custom_path=None):
    try:
        project_path = os.path.join(get_desktop_path(custom_path), project_name)
        os.chdir(project_path)
        os.system("git init")
    except Exception as e:
        print(f"Error initializing git: {e}")

def start_server(project_name, custom_path=None):
    try:
        project_path = os.path.join(get_desktop_path(custom_path), project_name)
        os.chdir(project_path)
        handler = http.server.SimpleHTTPRequestHandler
        
        # Essayer plusieurs ports si 8000 est occupé
        ports = [8000, 8001, 8002, 8003, 8004]
        for port in ports:
            try:
                with socketserver.TCPServer(("", port), handler) as httpd:
                    print(f"Server started on port {port}")
                    httpd.serve_forever()
                break
            except OSError:
                if port == ports[-1]:  # Dernier port essayé
                    raise
                continue
    except Exception as e:
        print(f"Error starting server: {e}")
