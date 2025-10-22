# About KEN-NET

ken-net is a small tool for web starter developers. It permit you to simply create the small structure of a web project.

# How to use

Just clone the project on your computer and in your CLI "python3 main.py <PROJECT_NAME>" and you would have your project name folder with an index.html, some assets (bootstrap, css and js files), some medias (images) inside.

## Tips

-> You can add "--git" to init git in your project
-> You can add "--serve" to start a development server (tries ports 8000-8004)
-> You can add "--path <FOLDER>" to choose custom destination folder

## Examples

python3 main.py mon-site
python3 main.py mon-site --git
python3 main.py mon-site --serve
python3 main.py mon-site --path /Users/username/Documents
python3 main.py mon-site --path /tmp --git --serve
