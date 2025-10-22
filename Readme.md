# About KEN-NET
ken-net is a small tool for web starter developers. It permit you to simply create the small structure of a web project.

## Installation
```bash
# Clone the project
git clone <repository-url>
cd ken-net

# Install dependencies
pip install -r requirements.txt
```

## How to use
Just run in your CLI: `python3 main.py <PROJECT_NAME>` and you would have your project name folder with an index.html, some assets (bootstrap, css and js files), some medias (images) inside.

### Basic usage
```bash
python3 main.py mon-projet
# Creates: ~/Desktop/mon-projet/
```

### Options available
- `--git` : Initialize git repository in your project
- `--serve` : Start a development server (tries ports 8000-8004)
- `--path <FOLDER>` : Choose custom destination folder

### Examples
```bash
# Basic project creation
python3 main.py mon-site

# With git initialization
python3 main.py mon-site --git

# With development server
python3 main.py mon-site --serve

# In custom folder
python3 main.py mon-site --path /Users/username/Documents
# Creates: /Users/username/Documents/mon-site/

# Combine options
python3 main.py mon-site --path /tmp --git --serve
```

## Features
- ✅ **Cross-platform**: Works on Windows, macOS, Linux
- ✅ **Error handling**: Graceful error messages, no crashes
- ✅ **Port management**: Automatically finds available port for server
- ✅ **Custom paths**: Create projects anywhere you want
- ✅ **Git integration**: Optional git repository initialization
- ✅ **Development server**: Built-in Python HTTP server

## Project structure created
```
mon-projet/
├── index.html          # Main HTML file with Bootstrap
├── assets/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   └── js/
│       ├── bootstrap.min.js
│       └── main.js
└── medias/
    └── ken-net.png
```

## Requirements
- Python 3.6+
- colorama
- tqdm
