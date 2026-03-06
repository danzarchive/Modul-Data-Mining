# Modul Data Mining

Materi praktikum mata kuliah **Data Mining** — Prodi Sains Data, Institut Teknologi Sepuluh Nopember (ITS).

Disusun oleh asisten dosen: **Danish Rafie Ekaputra** & **Yendra Wijayanto**

## Daftar Modul

### Modul 1: Data Preprocessing (Week 1-3)

Setup environment, data cleaning (noisy data, outlier), visualisasi multivariat (t-SNE), data integration, transformation, dan reduction.

| Week | Topik |
|:---:|---|
| 1 | [Virtual Environment (venv, conda, pip)](week-01/) |
| 2 | [Data Cleaning & Visualisasi Multivariat (t-SNE)](week-02/) |
| 3 | Data Integration, Transformation, Reduction |

### Modul 2: Dimensionality Reduction (Week 4-5)

Feature selection dan feature extraction untuk mengurangi dimensi data.

| Week | Topik |
|:---:|---|
| 4 | Feature Selection |
| 5 | Feature Extraction |

### Modul 3: Association Rules (Week 6-7)

Mining association rules menggunakan algoritma Apriori dan FP-Growth.

| Week | Topik |
|:---:|---|
| 6 | Apriori |
| 7 | FP-Growth |

### Week 8: ETS

### Modul 4: Unsupervised Learning (Week 9-10)

Clustering dan mixed data clustering untuk menemukan pola tersembunyi dalam data tanpa label.

| Week | Topik |
|:---:|---|
| 9 | Clustering |
| 10 | Mixed Data Clustering |

### Modul 5: Supervised Learning (Week 11-12)

Klasifikasi menggunakan Decision Tree dan Naive Bayes.

| Week | Topik |
|:---:|---|
| 11 | Decision Tree |
| 12 | Naive Bayes |

### Modul 6: Model Evaluation (Week 13-14)

Evaluasi model untuk klasifikasi dan regresi.

| Week | Topik |
|:---:|---|
| 13 | Klasifikasi |
| 14 | Regresi |

### Final Project & EAS (Week 15-16)

## Cara Menjalankan Environment & Run Notebook

### Prasyarat

Pastikan sudah terinstal:

- Python 3.11+ (via [Miniconda](https://docs.anaconda.com/miniconda/) atau [Homebrew](https://brew.sh/))
- Jupyter Notebook (atau ekstensi Jupyter di VS Code)

Panduan lengkap setup environment ada di [`week-01/`](week-01/).

### Menjalankan Notebook

1. Clone repo ini dan masuk ke folder week yang diinginkan
2. Buat conda environment dan install dependencies:
   ```bash
   conda create -n datmin python=3.12 -y
   conda activate datmin
   pip install numpy pandas scikit-learn matplotlib jupyter
   ```
3. Buka notebook (`.ipynb`) atau baca materi (`.md`) di folder week masing-masing

## Referensi Utama

- Han, J., Kamber, M. & Pei, J. *Data Mining: Concepts and Techniques*. 4th ed., 2023.
- Tan, P.-N., Steinbach, M. & Kumar, V. *Introduction to Data Mining*. Wiley, 2005.

## RPS

Rencana Pembelajaran Semester lengkap tersedia di [`rps/`](rps/).
