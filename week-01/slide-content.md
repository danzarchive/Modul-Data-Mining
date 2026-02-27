# Week 1 — Introduction Data Mining

> **Sumber:** `week1.pdf` (11 slides)
> **Penyaji:** Danish Rafie Ekaputra (NIP), Yendra Wijayanto (5052231005)
> **Institusi:** Institut Teknologi Sepuluh Nopember

---

## Slide 1: Cover

**Praktikum Data Mining**
W1 - Introduction Data Mining

---

## Slide 2: Roadmap Berdasarkan RPS

| Week | Topik |
|:---:|---|
| W-1 | Introduction Data Mining |
| W-2 | Data Cleaning & Preprocessing |
| W-3 | Data Integration & Transformation |
| W-4 | Dimensionality Reduction |
| W-5 | Feature Extraction |
| W-6 | Mining Associations Rule |
| W-7 | Mining Associations Rule |
| W-9 | Unsupervised Learning |
| W-10 | Unsupervised Learning / Decision Tree Algorithm |

---

## Slide 3: What is Data Mining?

**Data Mining** adalah proses menemukan pola, model, atau pengetahuan yang menarik (*interest patterns*) dari set data yang sangat besar. Sering juga disebut sebagai **Knowledge Discovery from Data (KDD)**.

Tujuan utamanya adalah untuk menemukan **informasi tersembunyi** (*hidden patterns*) yang dapat digunakan untuk **pengambilan keputusan**.

---

## Slide 4: Machine Learning

**Machine learning** adalah cabang dari AI, yaitu sebuah kemampuan ketika komputer dapat belajar dari data tanpa perlu diprogram secara eksplisit.

### Diagram Perbandingan

**Traditional Programming:**
```
Data + Program → Computer → Output
```

**Machine Learning:**
```
Data + Output → Computer → Program
```

---

## Slide 5: Step-step on Data Mining

### 1. Data Preparation
- **Data Cleaning**: Membersihkan noise dan data yang tidak konsisten.
- **Data Integration**: Menggabungkan data dari berbagai sumber.
- **Data Transformation**: Mengubah data ke bentuk yang sesuai untuk proses mining.
- **Data Selection**: Mengambil data yang relevan dengan tugas analisis.

### 2. Data Mining
Langkah inti di mana metode cerdas diterapkan untuk mengekstrak pola.

### 3. Pattern/Model Evaluation
Mengidentifikasi pola yang benar-benar menarik.

### 4. Knowledge Presentation
Menggunakan teknik visualisasi untuk menyajikan pengetahuan kepada pengguna.

> *Sumber: Han, J., Kamber, M. and J. Pei, Data Mining: Concepts and Techniques. Morgan Kaufmann, 4th., 2023*

---

## Slide 6: Metode Dalam Data Mining

| Metode | Deskripsi |
|---|---|
| **Classification** | Membangun model untuk memprediksi label kelas kategorikal |
| **Regression** | Memprediksi nilai numerik kontinu, seperti prediksi harga rumah |
| **Clustering** | Mengelompokkan data tanpa label kelas berdasarkan prinsip kemiripan antar objek (maximising intraclass similarity) |
| **Association Rule Learning** | Menemukan item yang sering muncul bersamaan, contohnya analisis keranjang belanja (market basket analysis) |

---

## Slide 7: Data Mining Tools

Tools yang digunakan dalam Data Mining:
- Jupyter Notebook
- Anaconda
- RStudio
- Google Colab

---

## Slide 8: Data Mining Library

Library Python untuk Data Mining:
- **NumPy**
- **pandas**
- **matplotlib**
- **scikit-learn**
- **TensorFlow**
- **statsmodels**
- **Keras**
- **PyTorch**

---

## Slide 9: Virtual Environment

**Virtual environment** adalah lingkungan Python terisolasi yang digunakan untuk menjalankan suatu proyek dengan versi library dan dependensi yang spesifik, tanpa mempengaruhi Python atau proyek lain di sistem yang sama.

*Virtual environment memungkinkan setiap proyek memiliki paket dan versinya sendiri.*

### Mengapa perlu Virtual Environment?

- Ketika kesalahan terjadi di environment terpisah, maka dengan mudah kita dapat menghapus environment tersebut dan tidak akan ada yang tersisa
- Environment mudah dibagikan sehingga dapat membantu kerjasama untuk mengerjakan suatu proyek dalam sebuah tim

### Contoh Kebutuhan

| Proyek | Library yang Dibutuhkan |
|---|---|
| Proyek A | numpy 1.20 |
| Proyek B | numpy 1.26 |

---

## Slide 10: Move To Notebook >>

*(Transisi ke Jupyter Notebook untuk praktikum)*

---

## Slide 11: Terima Kasih

Praktikum Data Mining Week 1
