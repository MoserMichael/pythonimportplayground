#!/bin/bash

find . -name '*.pyc' | xargs rm -f
find . -name __pycache__ -type d | xargs rm -rf
