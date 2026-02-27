# Week 01 — Virtual Environment

Pengenalan virtual environment di Python menggunakan **venv** dan **conda**.

## Materi

| File | Deskripsi |
|---|---|
| [`Virtual-Environment.md`](Virtual-Environment.md) | Materi lengkap: venv, conda, pip, perbandingan, contoh |
| [`Slide-Introduction-Data-Mining.pdf`](Slide-Introduction-Data-Mining.pdf) | Slide presentasi praktikum (referensi asdos sebelumnya) |
| [`slide-content.md`](slide-content.md) | Konten slide dalam format markdown |

## Demo

Linear Regression demo menggunakan NumPy, pandas, scikit-learn, dan matplotlib.

```bash
# Dengan venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r demo/requirements.txt
python demo/demo.py

# Dengan conda
conda env create -f demo/environment.yml
conda activate datmin
python demo/demo.py
```

## Topik yang Dibahas

1. **Mengapa perlu virtual environment?** — Dependency conflict, isolasi project
2. **venv** — Modul bawaan Python, ringan, pakai pip
3. **conda** — Package manager + environment manager, support non-Python
4. **Perbandingan venv vs conda** — Kapan pakai yang mana
5. **pip commands** — install, freeze, list, show, uninstall, cache purge
6. **conda commands** — create, activate, install, export, search, update, clean
7. **Sharing environment** — requirements.txt, environment.yml
