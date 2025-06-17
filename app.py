import streamlit as st
import pandas as pd
import pickle


# Load model yang sudah dilatih
@st.cache_data()
def load_model(model_path):
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model


# Fungsi untuk melakukan prediksi
def predict(model, input_data):
    X_new = pd.DataFrame(input_data, index=[0])
    y_pred = model.predict(X_new)
    return y_pred[0]


# "Daytime_evening_attendance": 1,
# "Previous_qualification_grade": 122,
# "Admission_grade": 100,
# "Displaced": 1,
# "Educational_special_needs": 1,
# "Debtor": 0,
# "Tuition_fees_up_to_date": 1,
# "Scholarship_holder": 0,
# "Unemployment_rate": 15,
# "Inflation_rate": 1,
# "GDP": 3,
def main():
    st.title("Prediksi DROPOUT Mahasiswa")

    st.header("Masukkan Data untuk prediksi")
    st.markdown(
        "Isi kolom-kolom berikut dengan data mahasiswa yang ingin Anda prediksi."
    )
    st.markdown("Pilih 1 jika YA, pilih 0 jika TIDAK")

    day_evening_attendance = st.selectbox(
        "Daytime Evening Attendance",
        [0, 1],
    )
    qualification_grad = st.number_input("Previous Qualification Grade", value=122.0)
    admission_grade = st.number_input("Admission Grade", value=100)
    displaced = st.selectbox("Displaced", [0, 1])
    education_spesial_need = st.selectbox("Educational Special Needs", [0, 1])
    debtor = st.selectbox("Debtor", [0, 1])
    tuition_fee_update = st.selectbox(
        "Tuition Fees Up to Date",
        [0, 1],
    )
    scholarship_holder = st.selectbox("Scholarship Holder", [1, 0])
    unemployment_rate = st.number_input("Unemployment Rate", value=15)
    inflation_rate = st.number_input("Inflation Rate", value=1)
    gdp = st.number_input("GDP", value=3)

    # Tombol untuk memulai prediksi
    if st.button("Prediksi"):
        # Load model
        model = load_model("model/student_model.pkl")

        # Masukkan data ke dalam dictionary
        input_data = {
            "Daytime_evening_attendance": [day_evening_attendance],
            "Previous_qualification_grade": [qualification_grad],
            "Admission_grade": [admission_grade],
            "Displaced": [displaced],
            "Educational_special_needs": [education_spesial_need],
            "Debtor": [debtor],
            "Tuition_fees_up_to_date": [tuition_fee_update],
            "Scholarship_holder": [scholarship_holder],
            "Unemployment_rate": [unemployment_rate],
            "Inflation_rate": [inflation_rate],
            "GDP": [gdp],
        }

        # Lakukan prediksi
        prediction = predict(model, input_data)

        # Tampilkan hasil prediksi
        if prediction == "1":
            st.success("Hasil Prediksi: Berpotensi Dropout")
        else:
            st.warning("Hasil Prediksi: Tidak Dropout")


if __name__ == "__main__":
    main()
