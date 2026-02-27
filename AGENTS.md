# Asisten Dosen Data Mining (asdos-datmin)

## Project Overview
Materi praktikum mata kuliah **Data Mining** yang disusun oleh asisten dosen: **Danish Rafie Ekaputra** & **Yendra Wijayanto**.
Konten ditulis dalam **Bahasa Indonesia**, format utama adalah Markdown (.md) dengan demo code Python.

## Struktur Project
```
asdos-datmin/
├── README.md                # Overview kurikulum & cara pakai
├── .gitignore
├── AGENTS.md                # Project context (file ini)
├── rps/
│   ├── 4_Data-Mining_27-Mei-2024.pdf   # RPS resmi
│   └── rps-content.md                  # RPS dalam markdown
│
├── week-01/
│   ├── README.md                              # Overview week 1
│   ├── Virtual-Environment.md                 # Materi utama
│   ├── Slide-Introduction-Data-Mining.pdf     # Slide presentasi (referensi)
│   ├── slide-content.md                       # Konten slide dalam markdown
│   └── demo/
│       ├── demo.py              # Linear Regression demo
│       ├── requirements.txt     # pip dependencies
│       ├── environment.yml      # conda env file
│       ├── notes.md             # Quick reference commands
│       └── demo_plot.png        # Generated plot
│
├── week-02/                 # (belum dibuat)
│   └── ...
└── ...
```

## Konvensi & Aturan
- **Bahasa**: Konten materi dalam Bahasa Indonesia, tapi istilah teknis data science boleh pakai English (e.g. "missing values", "feature selection", "clustering")
- **Format utama**: `.md` per topik + demo code `.py`
- **Organisasi**: Per-minggu → `week-01/`, `week-02/`, dst.
- **Naming**: Folder pakai `week-XX/`, file pakai nama topik (contoh: `Virtual-Environment.md`)
- **Library versions**: Selalu pakai latest stable, dicek via PyPI
- **Contoh code**: Harus practical dan tested (bukan pseudocode)
- **Setiap week punya**: `README.md` (overview) + materi + demo/
- **Emoji**: Jangan pakai emoji di file `.md`

## Kurikulum

| Week | Topik | Status |
|:---:|---|:---:|
| 1 | Virtual Environment (venv, conda, pip) | DONE |
| 2 | Data Cleaning: Missing Values & Noisy Data | - |
| 3 | Data Integration, Transformation, Reduction | - |
| 4 | Dimensionality Reduction: Feature Selection | - |
| 5 | Dimensionality Reduction: Feature Extraction | - |
| 6 | Mining Association Rules (Apriori) | - |
| 7 | Mining Association Rules (FP-Growth) | - |
| 8 | **ETS** | - |
| 9 | Unsupervised Learning: Clustering | - |
| 10 | Unsupervised Learning: Mixed Data Clustering | - |
| 11 | Supervised Learning: Decision Tree | - |
| 12 | Supervised Learning: Naive Bayes | - |
| 13-14 | Credibility: Model Evaluation (Klasifikasi & Regresi) | - |
| 15-16 | Final Project | - |
| 16 | **EAS** | - |

## Tech Stack
- Python 3.11 (Homebrew) / Python 3.12 (conda)
- Jupyter Notebook
- Ruff linter
- Libraries: numpy, pandas, scikit-learn, matplotlib

## Environment User (dans)
- **OS**: macOS ARM (Apple Silicon)
- **Python system**: 3.11 via Homebrew (`/opt/homebrew/bin/python3.11`)
- **Conda**: miniconda (`/opt/miniconda3/`)
- **Known issue**: Shell alias `python` → Homebrew Python, meng-override conda env. Fix: `unalias python && unalias python3`
- **Conda init**: Sudah di-setup via `conda init zsh`

## GitHub Repo
- **Repo name**: `Modul-Data-Mining` (di GitHub)
- **Local folder**: `asdos-datmin` (nama berbeda, tidak masalah)
- **AGENTS.md masuk repo**: Ya, di-commit sebagai project context

## Session History

### Session 2026-02-27 (sesi 1)
- Converted `Virtual Environtment.ipynb` → `.py` dan `.md`
- Identified notebook has 1 cell (markdown only), no code
- Added missing commands from official docs (venv & conda)
- Improved docs: added "Mengapa Perlu Virtual Environment?", comparison table, contoh requirements.txt & environment.yml, fixed typos
- Updated example library versions to latest stable (numpy 2.4.2, pandas 3.0.1, scikit-learn 1.8.0, matplotlib 3.10.8)
- Created and tested `demo/demo.py` — Linear Regression demo
- Tested both venv (pip) and conda workflows — both passed ✅
- Diagnosed conda PATH issue: Homebrew alias overrides conda Python → fix with `unalias`

### Session 2026-02-27 (sesi 2)
- Scanned RPS PDF (7 pages) → `rps/rps-content.md` — full curriculum Week 1–16
- Scanned week1.pdf (11 slides) → `week-01/slide-content.md` — asdos lama presentation
- Compared pdf-to-img + multimodal vs pdf-to-md: multimodal lebih bersih, pdf-to-md lebih reliable
- Planned 16-week curriculum based on RPS
- Created global skill `git-push-github` di `~/.config/opencode/skills/`
- Restructured repo: flat → `week-XX/` per-minggu structure
- Created `.gitignore`, root `README.md`, `week-01/README.md`
- Renamed: `Virtual Environtment.md` → `Virtual-Environment.md`, `week1.pdf` → `Slide-Introduction-Data-Mining.pdf`

## Tips & Gotchas
- `conda env export` default includes platform-specific builds. Use `--no-builds` for cross-OS sharing
- `conda env export --from-history` for minimal export (only explicitly installed packages)
- Nama folder lokal (`asdos-datmin`) tidak harus sama dengan nama repo GitHub (`Modul-Data-Mining`)
- `.gitignore` wajib masuk repo
