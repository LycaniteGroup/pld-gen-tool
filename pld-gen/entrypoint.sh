#!/bin/sh

cd /var/md2html \
&& python3 mkbuild.py \
&& mkdocs build \
&& node build.js