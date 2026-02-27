"""
Demo script — menggunakan numpy, pandas, scikit-learn, dan matplotlib.
Membuat dataset sederhana, train model, lalu plot hasilnya.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib

matplotlib.use("Agg")  # non-GUI backend supaya bisa jalan tanpa display
import matplotlib.pyplot as plt

# ============================================================
# 1. Buat dataset sederhana dengan NumPy
# ============================================================
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 data, fitur 1 kolom (0-10)
y = 2.5 * X.squeeze() + 7 + np.random.randn(100) * 2  # y = 2.5x + 7 + noise

print("=" * 50)
print("DEMO: NumPy, Pandas, Scikit-learn, Matplotlib")
print("=" * 50)

# ============================================================
# 2. Masukkan ke Pandas DataFrame
# ============================================================
df = pd.DataFrame({"X": X.squeeze(), "y": y})
print(f"\n[Pandas] DataFrame shape : {df.shape}")
print(f"[Pandas] Statistik deskriptif:")
print(df.describe().to_string())

# ============================================================
# 3. Train Linear Regression dengan Scikit-learn
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n[Scikit-learn] Linear Regression")
print(f"  Coefficient (slope) : {model.coef_[0]:.4f}")
print(f"  Intercept           : {model.intercept_:.4f}")
print(f"  MSE                 : {mse:.4f}")
print(f"  R² Score            : {r2:.4f}")

# ============================================================
# 4. Plot hasil dengan Matplotlib
# ============================================================
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color="steelblue", label="Data aktual", alpha=0.7)
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Prediksi model")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression — Demo Virtual Environment")
plt.legend()
plt.tight_layout()
plt.savefig("demo_plot.png", dpi=100)
print(f"\n[Matplotlib] Plot disimpan ke 'demo_plot.png'")

print("\n✅ Semua library bekerja dengan baik!")
