#!/usr/bin/env bash
set -e

BIN="$HOME/.local/bin"
DESKTOP="$HOME/.local/share/applications"

echo "Installing bchrg..."

# creating directories
mkdir -p "$BIN" "$DESKTOP"

# install executable
cp bchrg "$BIN/bchrg"
chmod +x "$BIN/bchrg"

echo "Installed to $BIN/bchrg"

echo "Installing bchrg.desktop..."

# install .desktop
sed "s|{EXEC_PATH}|$BIN/bchrg|g" bchrg.desktop.template > "$DESKTOP/bchrg.desktop"

echo "Installed to $DESKTOP/bchrg.desktop"
update-desktop-database "$DESKTOP" || true

echo "Done."
