#!/bin/bash

# Exit on error
set -e

echo "☕ Installing SDKMAN!..."

# Check if SDKMAN! is already installed
if [ ! -d "$HOME/.sdkman" ]; then
    curl -s "https://get.sdkman.io" | bash
    
    # Source SDKMAN! for the current session
    source "$HOME/.sdkman/bin/sdkman-init.sh"
else
    echo "✅ SDKMAN! is already installed"
    source "$HOME/.sdkman/bin/sdkman-init.sh"
fi

# Install Java
echo "📦 Installing Java..."
sdk install java

# Install Scala
echo "⚡ Installing Scala..."
sdk install scala

# Install sbt
echo "🔧 Installing sbt..."
sdk install sbt

echo "✅ All Java tools installed successfully!" 