#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Data Science Development Tools Installation..."

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Make scripts executable
chmod +x "$SCRIPT_DIR"/*.sh

# Run individual installation scripts
echo "📦 Installing Homebrew and applications..."
"$SCRIPT_DIR/brew_install.sh"

echo "☕ Installing SDKMAN! and Java tools..."
"$SCRIPT_DIR/sdkman_install.sh"

echo "✨ Installation complete! Please restart your terminal to ensure all changes take effect." 