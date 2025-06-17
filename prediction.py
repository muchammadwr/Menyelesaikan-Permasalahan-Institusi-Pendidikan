# --------------------------------------------
# Proyek Penerapan Data Science:
# Prediksi DropOut (Pengunduran Diri Students)
# Studi Kasus: Permasalaham Institusi Pendidikan
# Disusun oleh: Muchammad Wildan Alkautsar
# --------------------------------------------

import pandas as pd
import pickle

# --------------------------------------------
# Load model yang sudah disimpan (Pipeline Logistic Regression)
# --------------------------------------------
MODEL_PATH = "model/student_model.pkl"

try:
    with open(MODEL_PATH, "rb") as file_model:
        model = pickle.load(file_model)
except FileNotFoundError:
    print(f"File model tidak ditemukan di: {MODEL_PATH}")
    exit(1)

# --------------------------------------------
# Data baru untuk diprediksi (satu orang student)
# --------------------------------------------
new_data = pd.DataFrame(
    [
        {
            "Daytime_evening_attendance": 1,
            "Previous_qualification_grade": 122,
            "Admission_grade": 100,
            "Displaced": 1,
            "Educational_special_needs": 1,
            "Debtor": 0,
            "Tuition_fees_up_to_date": 1,
            "Scholarship_holder": 0,
            "Unemployment_rate": 15,
            "Inflation_rate": 1,
            "GDP": 3,
        }
    ]
)


# --------------------------------------------
# Prediksi dan interpretasi hasil
# --------------------------------------------

# Prediksi ulang
prediksi = model.predict(new_data)[0]
probabilitas = model.predict_proba(new_data)[0]

status = "DROPOUT (KELUAR)" if prediksi == 1 else "NO DROPOUT (TIDAK KELUAR)"

print("===== HASIL PREDIKSI STUDENTS =====")
print(f"[LOADED MODEL] Prediksi: {probabilitas} → {status}")
print(f"[LOADED MODEL] Probabilitas [DROPOUT, NO DROPOUT]: {probabilitas}")
