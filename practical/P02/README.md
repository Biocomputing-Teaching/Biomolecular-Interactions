# Protein-protein Docking with LightDock

## Introduction

This tutorial will perform an example docking calculation using the LightDock program (or webserver) for Docking analysis. The program and its dependencies will be installed during the practical session to control the installation process. However, if something fails during the installation, we can always use the LightDock server to complete this practical session.

## Requirements

* Setting up your computer with a Linux or macOS operating system (see course repository)

* Complete the "Learn the Basics" entries in the Python Tutorial

* Install Chimera for molecular visualization

* Install LightDock in a new Conda environment (see the "Installing LightDock" section)

* Install additional packages using Conda (see the "Installing Other needed packages" section)

* Clone this repository and open the P02 jupyter-notebook (see the "Downloading the repository and opening the P02 notebook" section)

### Installing LightDock

We start by creating a new Conda environment exclusive to run LightDock:

```
conda create --name lightdock python=3.7
```

Then we activate this new environment by running:

```
conda activate lightdock
```

You should see that your terminal prompt now starts with the word (lightdock) instead of the default (base); this indicates that the active Conda environment has changed to our new lightdock one.


After this, we proceed to install the LightDock program by running:

```
pip3 install lightdock
```

Then we are going to get the LightDock package for GitHub:

```
git clone https://github.com/lightdock/lightdock.git
```

We enter the "lightdock" folder and execute the setup.sh script:

```
cd lightdock
```

```
./setup.sh
```

After this is finished, we get the Path to this folder by executing:


```
pwd
```

We must copy the output from the previous command and replace the string "/path/to/lightdock" with it in the first of the following lines:

```
export LIGHTDOCK_HOME="/path/to/lightdock"
export PATH=$PATH:$LIGHTDOCK_HOME/bin
export PYTHONPATH=$PYTHONPATH:$LIGHTDOCK_HOME
```

After replacing it, we paste these lines at the end of the .bashrc file. To edit that file, we execute:

For Ubuntu:

```
gedit ~/.bashrc
```

For Mac:

```
open -t ~/.bashrc
```

We save the file and go back to the terminal to source the changes running:

```
source ~/.bashrc
```

We test now that our program is correctly installed by running:

```
lightdock3.py -h
```

If everything went right, we should see the following lines:

```
"usage: lightdock [-h] [-f configuration_file] [-s SCORING_FUNCTION]
                 [-sg GSO_SEED] [-t TRANSLATION_STEP] [-r ROTATION_STEP] [-V]
                 [-c CORES] [--profile] [-mpi] [-ns NMODES_STEP] [-min]
                 [--listscoring]
                 setup_file steps

                 .
                 .
                 .
```

### Installing Other needed packages


We will also need to install the following Conda packages (one by one):

```
conda install -c conda-forge jupyterlab
```

```
conda install -c conda-forge mdtraj
```

```
conda install pandas
```

```
conda install -c anaconda git
```

```
conda install -c conda-forge matplotlib
```

### Downloading the repository and opening the P02 notebook

After getting these packages, we can clone our repository in a new folder:

```
mkdir P02
```

```
cd P02
```

```
git clone https://github.com/Biocomputing-Teaching/Biomolecular-Interactions.git
```

We enter the practical session 2 folder:

```
cd Biomolecular-Interactions/practical/P02
```

And open the Jupyter Notebook:

```
jupyter notebook 02-AnalyseDockingSimulations.ipynb
```
