import sys, functions, colorama, os, time, tqdm
from functions import *
args = sys.argv

# Verfication de l'existance d'un nom de projet
if(len(args) > 1):
    project_name = args[1]
    # Check for --help option
    if project_name == "--help":
        print(colorama.Fore.LIGHTBLUE_EX + "\n KEN-NET - Web Project Generator" + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTGREEN_EX + "\n Usage: python3 main.py <PROJECT_NAME> [options]" + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTYELLOW_EX + "\n Available options:" + colorama.Style.RESET_ALL)
        print("  --git     : Initialize git repository")
        print("  --serve   : Start development server")
        print("  --path    : Choose destination folder")
        print(colorama.Fore.LIGHTYELLOW_EX + "\n Examples:" + colorama.Style.RESET_ALL)
        print("  python3 main.py my-site")
        print("  python3 main.py my-site --git")
        print("  python3 main.py my-site --serve")
        print("  python3 main.py my-site --path /tmp")
        exit()
else:
    print(colorama.Fore.RED + " \n Please enter a project name \n" + colorama.Style.RESET_ALL)
    exit()

#Creation de la liste des options diponibles et verification des args passes

options = ["--git", "--serve", "--path"]

# Variable pour le chemin personnalisé
custom_path = None

# Detection de l'option --path
for i in range(len(args)):
    if args[i] == "--path" and i + 1 < len(args):
        custom_path = args[i + 1]
        break

# Validation simple des options
valid_options = ["--git", "--serve", "--path"]
for i in range(2, len(args)):
    if args[i] not in valid_options and not (i > 0 and args[i-1] == "--path"):
        print(colorama.Fore.RED + "\n Please enter valid options \n" + colorama.Style.RESET_ALL)
        exit()


# Affichage du figlet stylise et petite pause
print(colorama.Fore.BLUE)
os.system("figlet KEN - NET")
time.sleep(2)
print(colorama.Style.RESET_ALL)

# Creation of project with message display
print(colorama.Fore.LIGHTGREEN_EX + " \n Creating your project " + project_name + " ... \n" + colorama.Style.RESET_ALL)

# Creation du tableau de fonctions pour la barre de progression
traitements = [
    create_project_main_folder,
    create_assets_folder,
    create_css_folder,
    create_js_folder,
    create_medias_folder,
    create_index_html_file,
    create_style_css_file,
    create_main_js_file,
    create_bootstrap_css_file,
    create_bootstrap_js_file,
    copy_media_images,
     ]

# Creation de la barre de progression
barre = tqdm.tqdm(traitements)

# Traiments des differentes operations
for trait in traitements:
    time.sleep(0.5)
    trait(project_name, barre, custom_path)
    barre.update()

if(len(args) > 2):
    # Verification et initialisation du depot git
    if(args[2] == "--git"):
        git_init(project_name, custom_path)

    # Verification et demarrage du server
    if(args[2] == "--serve"):
        print(colorama.Fore.LIGHTGREEN_EX + " \n Development server started at (http://127.0.0.1:8000) \n" + colorama.Style.RESET_ALL)
        start_server(project_name, custom_path)
if(len(args) > 3):
        # Verification et initialisation du depot git
    if(args[3] == "--git"):
        git_init(project_name, custom_path)

    # Verification et demarrage du server
    if(args[3] == "--serve"):
        print(colorama.Fore.LIGHTGREEN_EX + "Development server started at http://127.0.0.1:8000 " + colorama.Style.RESET_ALL)
        start_server(project_name, custom_path)

# Useful end message
project_path = os.path.join(get_desktop_path(custom_path), project_name)
print(colorama.Fore.LIGHTGREEN_EX + f"\n Project created successfully in {project_path}" + colorama.Style.RESET_ALL)
print(colorama.Fore.LIGHTBLUE_EX + f" To view it: cd {project_path} && python3 -m http.server 8000" + colorama.Style.RESET_ALL)

exit()