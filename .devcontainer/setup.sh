#!/usr/bin/env bash
set -e

# Volume Permissions
sudo chown -R $(whoami) /home/vscode/.cache/uv
sudo chown -R $(whoami) /home/vscode/.config

echo "Installing packages"
uv sync

echo "Installing github stack"
gh extension install github/gh-stack

echo "Check GCP is logged in"
if ! gcloud auth print-access-token >/dev/null 2>&1; then
    echo "--------------------------------------------------------"
    echo "⚠️  gcloud is not authenticated."
    echo "Run 'gcloud auth application-default login' in your VS Code terminal."
    echo "--------------------------------------------------------"
fi

echo "Setup successful!"