#!/bin/bash

# Exit on error
set -e

echo "🍺 Installing Homebrew..."

# Check if Homebrew is already installed
if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH for the current session
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "✅ Homebrew is already installed"
fi

# Update Homebrew
echo "🔄 Updating Homebrew..."
brew update

# Install applications
echo "📥 Installing applications..."

# System tools
echo "🛠️ Installing system tools..."
brew install --cask iterm2
brew install --cask clipy
brew install --cask caffeine

echo "✅ All applications installed successfully!" 