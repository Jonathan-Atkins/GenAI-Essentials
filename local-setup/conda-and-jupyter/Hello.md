## Hello Example

Here we are creating our hello env.
We install pandas in our hello env
We observe which packages are installed hello
We observe which packages are installed in base
We can use Python binary to execute the python in context of conda
Check what binary is being loaded
```sh
conda create -n hello python 3.10.0 -y
conda activate {conda file name}
conda install -c conda-forge pandas
pip list
conda deactivate
pip list
conda activate hello
python app.py
whereis python3
```
