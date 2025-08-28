# Install Mini-Conda

https://www.anaconda.com/docs/getting-started/miniconda/main

```sh
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh
bash /tmp/miniconda.sh -b -u -p ~/miniconda3
```

## Setup Miniconda

```sh
source ~/miniconda3/bin/activate
conda init --all
```

## Create a new env 

```sh
conda create --name hello python=3.10.0 -y

## To accept the Terms of Service (ToS) for the default Anaconda channels

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

## Activate Env

```sh
conda activate hello
```

## See all existing conda envs

```sh
ls -la ~/miniconda3/envs
```

## Deactivate/Remove Envs

```sh
conda deactivate
conda remove -n envname --all -y
```