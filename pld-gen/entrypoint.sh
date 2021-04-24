#!/bin/sh

cd md2html \
&& python3 mkbuild.py \
&& mkdocs build \
&& node build.js