# Venv & Conda Environment

## **Mengapa Perlu Virtual Environment?**
Saat mengerjakan beberapa project Python, setiap project bisa membutuhkan versi library yang berbeda-beda. Tanpa virtual environment, semua project akan berbagi library yang sama — dan ini bisa menyebabkan **dependency conflict**.

Virtual environment mengisolasi setiap project agar punya library sendiri-sendiri, sehingga:
- Project A bisa pakai `pandas==1.5` dan Project B pakai `pandas==2.0` tanpa bentrok
- Environment bisa di-reproduce ulang dengan mudah (tinggal share `requirements.txt` atau `environment.yml`)
- Tidak mengotori instalasi Python global di sistem

## **Venv**
venv adalah modul bawaan Python yang digunakan untuk membuat virtual environment.

Fitur utama:
- ringan
- sederhana
- tidak perlu install tambahan

venv menggunakan pip untuk menginstall library dari `Python Package Index`. 

**Langkah-langkah untuk membuat `venv`**
1. Buat environment:
   - Windows: `python -m venv myenv`
   - Mac/Linux: `python3 -m venv myenv`
2. Aktivasi:
   - Windows (cmd): `myenv\Scripts\activate`
   - Windows (PowerShell): `myenv\Scripts\Activate.ps1`
   - Mac/Linux: `source myenv/bin/activate`
3. `pip install jupyter ipykernel` -> untuk menambahkan venv ke kernel vscode
4. `python -m ipykernel install --user --name=myenv`

> **Catatan**: `py` adalah Python Launcher khusus Windows. Di Mac/Linux gunakan `python3`.

**Opsi tambahan saat membuat venv**
- `python -m venv myenv --clear` -> Hapus isi env lama lalu buat ulang
- `python -m venv myenv --upgrade-deps` -> Buat env dan upgrade pip ke versi terbaru
- `python -m venv myenv --system-site-packages` -> Env bisa akses system packages
- `python -m venv myenv --prompt "nama"` -> Custom nama prompt di terminal

**Deaktivasi venv**  
`deactivate` -> Keluar dari virtual environment yang sedang aktif

**Menghapus `venv` yang telah dibuat**
1. `jupyter kernelspec list`
2. `jupyter kernelspec uninstall nama_kernel`
3. Hapus folder:
   - Windows: `rmdir /s myenv`
   - Mac/Linux: `rm -rf myenv`

**Batch Instalation**  
Kamu bisa melakukan instalasi packages satu per satu dengan `pip install <packages>`, atau jika ingin menginstall banyak package sekaligus, kamu dapat membuat sebuah file `requirements.txt` yang berisi package-package yang ingin di install lalu jalankan command
`pip install -r requirements.txt`

Contoh isi `requirements.txt`:
```
numpy==2.4.2
pandas==3.0.1
scikit-learn==1.8.0
matplotlib==3.10.8
```

**Membuat `requirements.txt` dari env yang sudah ada**  
`pip freeze > requirements.txt` -> Export daftar package beserta versinya ke file

**Command pip penting lainnya**
- `pip list` -> Lihat semua package yang terinstall
- `pip show <nama_package>` -> Lihat info detail suatu package (versi, lokasi, dependencies)
- `pip uninstall <nama_package>` -> Hapus package
- `pip install --upgrade <nama_package>` -> Update package ke versi terbaru
- `pip install --upgrade pip` -> Update pip itu sendiri
- `pip check` -> Cek apakah ada dependency yang conflict
- `pip cache purge` -> Bersihkan cache pip

## **Conda Environment**
- open-source package management system
- Instalasi menggunakan conda
    - untuk install >> `conda install <nama_package>`
    - untuk install versi tertentu >> `conda install <nama_package>==<versi>`

**Membuat `conda environment`**  
1. Download `Anaconda` melalui browser terlebih dahulu
2. Buka anaconda prompt
3. Jalankan command `conda create --name <nama_env> python=3.10` atau `conda create --name <nama_env>`

**Aktivasi & Deaktivasi**  
`conda activate <nama_env>` -> Masuk ke environment  
`conda deactivate` -> Keluar dari environment yang sedang aktif

**Informasi Environment**  
`conda list --name <nama_env>` -> Untuk melihat packages apa saja yang terinstall dalam environment yang telah dibuat  
`conda env list` -> Untuk melihat environment yang sudah ada  
`conda info` -> Informasi tentang instalasi conda  

**Mencari & Mengelola Package**  
- `conda search <keyword>` -> Cari package yang tersedia
- `conda update <nama_package>` -> Update package tertentu
- `conda update conda` -> Update conda itu sendiri
- `conda update python` -> Update Python ke versi terbaru dalam seri (3.x -> latest 3.x)
- `conda remove --name <nama_env> <nama_package>` -> Hapus satu package dari environment
- `conda install --channel conda-forge <nama_package>` -> Install dari channel tertentu

**Konfigurasi Channel**
- `conda config --add channels conda-forge` -> Tambah channel
- `conda config --show channels` -> Lihat daftar channel yang aktif

**Batch Instalation**
1. Buat sebuah file `environment.yml` yang berisi packages yang ingin diinstal
2. Jalankan command `conda env create -f environment.yml`

Contoh isi `environment.yml`:
```yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=2.4.2
  - pandas=3.0.1
  - scikit-learn=1.8.0
  - pip:
    - some-pip-package
```

**Menghapus Environment Conda**  
`conda env remove --name <nama_env>`

**Command Conda Tambahan**
- `conda init` -> Setup conda untuk shell (bash/zsh/powershell)
- `conda clean --all` -> Bersihkan cache dan package tidak terpakai
- `conda run --name <nama_env> python script.py` -> Jalankan command di env tanpa activate
- `conda rename --name <old_env> <new_env>` -> Rename environment
- `conda compare <env>.yml` -> Bandingkan environment dengan file yml
- `conda doctor` -> Diagnosa masalah di environment

## **Venv vs Conda — Kapan Pakai yang Mana?**

| | Venv + pip | Conda |
|---|---|---|
| **Cocok untuk** | Project Python murni | Data science, ML, package non-Python |
| **Install dari** | PyPI (pip) | Anaconda repo + conda-forge |
| **Non-Python deps** (C/CUDA/MKL) | Tidak bisa | Bisa |
| **Ukuran** | Ringan | Lebih berat |
| **Sudah ada di Python** | Ya (built-in) | Perlu install Anaconda/Miniconda |
| **Kecepatan install** | Cepat | Lebih lambat (solving environment) |

**Ringkasan**: Kalau project-mu hanya butuh library Python biasa, **venv + pip** sudah cukup. Kalau butuh package yang punya dependency non-Python (misalnya TensorFlow dengan CUDA, atau package scientific computing), **conda** lebih mudah.

> **Alternatif Modern**: [`uv`](https://github.com/astral-sh/uv) adalah package manager Python baru yang jauh lebih cepat dari pip (10-100x). Bisa menggantikan pip + venv sekaligus. Worth checking out, tapi belum se-mature pip.

## **Command Penting**
```
# === VENV / PIP ===
python -m venv myenv                # Buat env (Mac/Linux: python3)
myenv\Scripts\activate              # Aktivasi (Windows)
source myenv/bin/activate           # Aktivasi (Mac/Linux)
deactivate                          # Keluar dari env

pip install <nama_package>
pip install <nama_package>==<versi>
pip install --upgrade <nama_package>
pip install --upgrade pip
pip install -r requirements.txt
pip uninstall <nama_package>

pip list
pip show <nama_package>
pip freeze > requirements.txt
pip check
pip cache purge

# === CONDA ===
conda create --name <nama_env> python=3.10
conda activate <nama_env>
conda deactivate

conda install <nama_package>
conda install <nama_package>==<versi>
conda install --channel conda-forge <nama_package>
conda update <nama_package>
conda update conda
conda update python
conda remove --name <nama_env> <nama_package>
conda search <keyword>

conda list --name <nama_env>
conda env list
conda info

conda env create -f environment.yml
conda env export --name <nama_env> > <nama_env>.yaml
conda env remove --name <nama_env>

conda config --add channels conda-forge
conda config --show channels

conda init
conda clean --all
conda run --name <nama_env> python script.py
conda rename --name <old_env> <new_env>
conda doctor
```
