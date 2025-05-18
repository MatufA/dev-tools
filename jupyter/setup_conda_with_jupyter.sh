#!/bin/bash 
set -x 

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash

source ~/.bashrc
conda env list

conda install -c conda-forge jupyterlab -y
conda install ipykernel -y
conda install conda-forge::papermill -y

jupyter-lab --generate-config -y
sudo aws s3 cp s3://tremor-data-science/development/configurations/Dev-Env/jupyter_lab_config.py /home/ec2-user/.jupyter/jupyter_lab_config.py

conda install -c conda-forge nb_conda_kernels -y

sudo aws s3 cp s3://tremor-data-science/development/configurations/Dev-Env/lunch_jupyterlab.sh /etc/systemd/lunch_jupyterlab.sh
sudo chmod +x /etc/systemd/lunch_jupyterlab.sh

sudo aws s3 cp s3://tremor-data-science/development/configurations/Dev-Env/jupyter-lab-server.service /etc/systemd/system/jupyter-lab-server.service 
sudo systemctl daemon-reload
sudo systemctl start jupyter-lab-server
sudo systemctl enable jupyter-lab-server
