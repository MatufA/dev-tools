#!/bin/bash

if [ -f "/home/ec2-user/miniconda3/etc/profile.d/conda.sh" ]; then
    . "/home/ec2-user/miniconda3/etc/profile.d/conda.sh"
    CONDA_CHANGEPS1=false /home/ec2-user/miniconda3/bin/jupyter-lab --config /home/ec2-user/.jupyter/jupyter_lab_config.py --allow-root
fi
