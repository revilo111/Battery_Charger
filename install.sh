#!/usr/bin/env bash
set -e

INSTALL_DIR="$HOME/.local/bin"

echo "Installing bchrg..."

mkdir -p "$INSTALL_DIR"

cp bchrg "$INSTALL_DIR/bchrg"
chmod +x "$INSTALL_DIR/bchrg"

echo "Installed to $INSTALL_DIR/bchrg"

if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo ""
    echo "WARNING: ~/.local/bin is not in your PATH."
    echo "Add this to your shell config:"
    echo 'export PATH="$HOME/.local/bin:$PATH"'
fi

INSTALL_DIR="$HOME/.local/share/applications"

echo "Installing bchrg.desktop..."

mkdir -p "$INSTALL_DIR"

cp bchrg.desktop "$INSTALL_DIR/bchrg.desktop"
chmod +x "$INSTALL_DIR/bchrg.desktop"

echo "Installed to $INSTALL_DIR/bchrg.desktop"

if [[ ":$PATH:" != *":$HOME/.local/share/applications:"* ]]; then
    echo ""
    echo "WARNING: ~/.local/share/applications is not in your PATH."
    echo "Add this to your shell config:"
    echo 'export PATH="$HOME/.local/share/applications:$PATH"'
fi

echo "Done."
