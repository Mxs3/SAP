#!/bin/bash

apt install python3
pip3 install pydub
pip3 install colorama

echo "Executing Simple Audio Player (SAP)..."
python3 ./sap.py