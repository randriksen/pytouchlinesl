#!/usr/bin/env bash
set -euo pipefail

export VERSION="${1:-}"

echo "$VERSION" | grep -qEo '[0-9]+\.[0-9]+\.[0-9]+'
if [ $? -ne 0 ]; then
    echo "Invalid version number. Please use the format '0.2.0'"
    exit 1
fi

# Bump version in pyproject.toml and sync the uv.lock file
sed -i 's/^\(version = \).*$/\1'\"$VERSION\"'/' pyproject.toml
uv sync

git add pyproject.toml uv.lock
git commit -m "chore: bump version to $VERSION"
git tag -a "$VERSION" -m "$VERSION"

git push origin main "$VERSION"
