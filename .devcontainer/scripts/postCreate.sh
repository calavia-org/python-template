#!/bin/sh

# Include commands that you would like to execute after the container is created
uname -a
pip install pre-commit
pre-commit install
