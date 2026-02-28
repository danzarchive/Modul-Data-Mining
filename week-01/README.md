# Week 01 — Virtual Environment & Introduction to Git

Pengenalan virtual environment di Python menggunakan **venv** dan **conda**, serta pengenalan **Git & GitHub** untuk version control.

## Materi

| File | Deskripsi |
|---|---|
| [`Virtual-Environment.md`](Virtual-Environment.md) | Materi lengkap: venv, conda, pip, perbandingan, contoh |
| [`Introduction-Git-GitHub.md`](Introduction-Git-GitHub.md) | Materi lengkap: Git setup, SSH, GitHub, branching, pull request |
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
8. **Apa itu Git & GitHub?** — Version control, konsep dasar, tiga area Git
9. **Setup Git & SSH** — Instalasi, konfigurasi, SSH key untuk GitHub
10. **Workflow Git** — init, add, commit, push, pull, clone
11. **Branching & Pull Request** — Branching, merge, kolaborasi via PR
12. **.gitignore** — File yang tidak perlu di-track, template Python/Data Science
