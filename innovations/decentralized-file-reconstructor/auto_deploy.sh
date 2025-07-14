#!/bin/bash
# auto_deploy.sh — One-click deploy script for AI File Reconstructor
# Compatible with Linux, macOS, WSL, Git Bash, and most CI agents

set -e

### CONFIG ###
REPO_NAME="ai-file-reconstructor"
DEFAULT_BRANCH="main"
USER_NAME="symbiote001"
USER_EMAIL="rickyfoster@protonmail.com"
REMOTE_URL="git@github.com:TheRickyFoster/ai-file-reconstructor.git"
################

echo "[🧠] Starting auto deployment..."

# Normalize line endings
git config --global core.autocrlf input

# Git setup
git config --global user.name "$USER_NAME"
git config --global user.email "$USER_EMAIL"

# Create repo if not already initialized
if [ ! -d ".git" ]; then
    echo "[🌱] Initializing Git repository..."
    git init
    git remote add origin "$REMOTE_URL"
    git branch -M $DEFAULT_BRANCH
fi

# Add everything
echo "[📦] Staging changes..."
git add .

# Commit
echo "[✅] Committing..."
git commit -m "Deploy: Full project sync at $(date '+%Y-%m-%d %H:%M:%S')"

# Fetch and rebase
echo "[🔄] Syncing with remote..."
git fetch origin $DEFAULT_BRANCH || echo "[⚠️] Remote branch not found — creating new one."
git rebase origin/$DEFAULT_BRANCH || echo "[ℹ️] Rebase skipped or failed — continuing..."

# Push
echo "[🚀] Pushing to $REMOTE_URL..."
git push origin $DEFAULT_BRANCH --force-with-lease

echo "[🎉] Deployment complete."
