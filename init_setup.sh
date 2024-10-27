#!/bin/bash
echo $(DATE) "Environment Setup Started"
VERSION=3.10
echo "Creating a conda environment with python $VERSION" 
conda create -n python_project_test python=$VERSION -y
echo "Enviroment created successfully"
echo "Activating the environment"
#source C:/Users/smart/miniconda3/etc/profile.d/conda.sh
source activate python_project
echo "Installing the depencies"
pip install -r requirements.txt
echo "Requirements installed successfully"
echo $(DATE) "Environment Setup completed"