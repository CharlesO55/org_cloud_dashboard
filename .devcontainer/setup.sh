#!/usr/bin/env bash
set -e

sudo chown -R $(whoami) /home/vscode/.cache/uv

uv sync
echo "Setup successful!"
