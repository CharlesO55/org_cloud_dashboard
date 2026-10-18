#!/usr/bin/env bash
set -e

sudo chown -R $(whoami) /home/vscode/.cache/uv

uv sync

gh extension install github/gh-stack

echo "Setup successful!"
