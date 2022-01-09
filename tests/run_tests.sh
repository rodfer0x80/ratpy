#!/bin/bash

setup(){
    echo "Setting up virtual environment and dependencies..."
    if [ ! -d "venv/" ]; then
        python3 -m venv venv
    fi
}

setup &&\
    source venv/bin/activate &&\
    pip install -r requirements.txt > /dev/null &&\
    python3 __main__.py &&\


