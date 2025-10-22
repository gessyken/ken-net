import sys, functions, colorama, os, time, tqdm
from functions import *
args = sys.argv

# Verfication de l'existance d'un nom de projet
if(len(args) > 1):
    project_name = args[1]
else:
    print(colorama.Fore.RED + " \n Veuillez entrer un nom de projet \n" + colorama.Style.RESET_ALL)
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
        print(colorama.Fore.RED + "\n Veuillez entrer des options valides \n" + colorama.Style.RESET_ALL)
        exit()


# Affichage du figlet stylise et petite pause
print(colorama.Fore.BLUE)
os.system("figlet KEN - NET")
time.sleep(2)
print(colorama.Style.RESET_ALL)

# Creation du projet avec affichage des messages
print(colorama.Fore.LIGHTGREEN_EX + " \n Creation de votre projet " + project_name + " ... \n" + colorama.Style.RESET_ALL)

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
        print(colorama.Fore.LIGHTGREEN_EX + " \n Le serveur de developpement est lance sur l'adresse (http://127.0.0.1:8000) \n" + colorama.Style.RESET_ALL)
        start_server(project_name, custom_path)
if(len(args) > 3):
        # Verification et initialisation du depot git
    if(args[3] == "--git"):
        git_init(project_name, custom_path)

    # Verification et demarrage du server
    if(args[3] == "--serve"):
        print(colorama.Fore.LIGHTGREEN_EX + "Le serveur de developpement est lance sur l'adresse http://127.0.0.1:8000 " + colorama.Style.RESET_ALL)
        start_server(project_name, custom_path)


exit()