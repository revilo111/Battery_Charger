#!/usr/bin/env bash
set -e

# set variable to dir addr
BIN="$HOME/.local/bin"
DESKTOP="$HOME/.local/share/applications"

echo "Installing bchrg..."

# creating directories
mkdir -p "$BIN" "$DESKTOP"

# install executable
cp bchrg "$BIN/bchrg"
chmod +x "$BIN/bchrg"

echo "Installed bchrg to $BIN/bchrg"

# install .desktop
sed "s|{EXEC_PATH}|$BIN/bchrg|g" bchrg.desktop > "$DESKTOP/bchrg.desktop"

echo "Installed bchrg.desktop to $DESKTOP/bchrg.desktop"

# updating desktop
update-desktop-database "$DESKTOP" || true
xdg-desktop-menu forceupdate || true

echo "Done."
