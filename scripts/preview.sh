#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --watch
