# Data Science Development Tools for macOS

This repository contains installation scripts and documentation for setting up a data science development environment on macOS.

## Essential Tools

### System Tools
- [Homebrew](https://brew.sh/) - The missing package manager for macOS. Simplifies installation of command-line tools and applications.
- [iTerm2](https://iterm2.com/) - A powerful terminal replacement with features like split panes, search, autocomplete, and more.
- [Clipy](https://clipy-app.com/) - A clipboard extension app that keeps your clipboard history and allows you to manage multiple clips.
- [Caffeine](https://intelliscapesolutions.com/apps/caffeine) - A simple menu bar utility that prevents your Mac from going to sleep.

### Development Tools
- [SDKMAN!](https://sdkman.io/) - A tool for managing parallel versions of multiple Software Development Kits on Unix-like systems.
- [Scala](https://www.scala-lang.org/) - A modern multi-paradigm programming language designed to express common programming patterns in a concise, elegant, and type-safe way.
- [sbt](https://www.scala-sbt.org/) - The interactive build tool for Scala and Java projects.

### VSCode Plugins

#### 1. General Development
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - Enhanced Git integration and repository visualization
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - Code formatter supporting multiple languages
- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag) - Automatically rename paired HTML/XML tags

#### 2. Productivity
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) - Autocompletes filenames
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - Development container support
- [IntelliJ IDEA Keybindings](https://marketplace.visualstudio.com/items?itemName=k--kato.intellij-idea-keybindings) - IntelliJ IDEA keybindings for VS Code

#### 3. Theme and UI
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - Material Design Icons for VS Code

#### 4. Language Specific

##### General
- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) - Run code snippets or code files
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) - Docker extension for VS Code
- [Kubernetes](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) - Kubernetes support
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - YAML language support

##### Python
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python language support and debugging
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - Fast, feature-rich language support for Python
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) - Python Debugger extension
- [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.data-wrangler) - Data wrangling and visualization
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Jupyter notebook support
- [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers) - Jupyter notebook renderers

##### Scala
- [Scala (Metals)](https://marketplace.visualstudio.com/items?itemName=scalameta.metals) - Official Scala language server
- [Scala Syntax](https://marketplace.visualstudio.com/items?itemName=scala-lang.scala) - Scala syntax highlighting
- [Debugger for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug) - Java debugger
- [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) - Essential Java extensions
- [Language Support for Java](https://marketplace.visualstudio.com/items?itemName=redhat.java) - Java language support

#### 5. Remote Development
- [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) - Open folders on remote machines using SSH
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) - Real-time collaborative development

## Installation

### Automated Installation
Run the installation script to set up all tools:

```bash
./scripts/install.sh
```

### Manual Installation

#### Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### iTerm2
```bash
brew install --cask iterm2
```

#### Clipy
```bash
brew install --cask clipy
```

#### Caffeine
```bash
brew install --cask caffeine
```

#### SDKMAN!
```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

#### Java and Scala
```bash
sdk install java
sdk install scala
sdk install sbt
```

## Scripts

The `scripts` directory contains installation scripts for different components:

- `install.sh` - Main installation script
- `brew_install.sh` - Homebrew and cask applications
- `sdkman_install.sh` - SDKMAN! and related tools
