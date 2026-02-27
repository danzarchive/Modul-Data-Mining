# venv
python3 -m venv week1
source week1/bin/activate
python --version
pip --version
pip install --upgrade pip
pip install -r requirements.txt
python demo.py
pip freeze > requirements.txt

# conda
conda activate week1
python --version
python3 --version
which python
which python3
unalias python
unalias python3
conda install numpy
conda install numpy pandas scikit-learn matplotlib
python demo.py
conda env export --name week1 > environment.yml
conda env create -f environment.yml
conda activate week1
