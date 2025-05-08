import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

st.set_page_config(page_title="Takaran Pakan Ikan Nila")

@st.cache_data
def load_model():
    df = pd.read_excel("dataset_pakan_ikan_nila.xlsx")
    X = df[['Umur_Ikan (hari)', 'Berat_Ikan (gram)']]
    y = df['Takaran_Pakan (gram)']
    model = KNeighborsRegressor(n_neighbors=5)
    model.fit(X, y)
    return model

model = load_model()

# Cek dan buat session_state 'page'
if "page" not in st.session_state:
    st.session_state.page = "sampul"

# Fungsi-fungsi navigasi
def go_to_prediksi():
    st.session_state.page = "prediksi"

def back_to_sampul():
    st.session_state.page = "sampul"

# Halaman Sampul
def halaman_sampul():
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>APLIKASI PREDIKSI TAKARAN PAKAN IKAN</h1>
            <hr style='width: 50%; margin: auto;'>
            <p> TAKARAN PAKAN IKAN GURAME!</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("nilla.png", width=200)
        st.write("")  # buat jarak kosong
        st.button("Mulai Prediksi", on_click=go_to_prediksi)

# Halaman Prediksi
def halaman_prediksi():
    st.title("ISI SESUAI KRITERIA IKAN")

    umur = st.number_input("Umur Ikan (Hari)", min_value=1, max_value=365, value=30)
    berat = st.number_input("Berat Ikan (gram)", min_value=0.1, max_value=1000.0, value=50.0)
    jumlah_ikan = st.number_input("Jumlah Ikan", min_value=1, max_value=10000, value=10)
    panjang_kolam = st.number_input("Panjang Kolam (Meter)", min_value=1.0, max_value=100.0, value=5.0)

    if st.button("Prediksi Takaran Pakan"):
        pred = model.predict([[umur, berat]])
        total_pakan = pred[0] * jumlah_ikan

        if umur < 90:
            jenis_pakan = "PF (Pakan Fase Awal)"
        elif umur <= 180:
            jenis_pakan = "Pakan Kode -1"
        elif umur <= 240:
            jenis_pakan = "Pakan Kode -2"
        else:
            jenis_pakan = "Pakan Kode -3"

        st.success(f"Takaran Pakan per Ikan: {pred[0]:.2f} Ons")
        st.success(f"Total Takaran untuk {jumlah_ikan} Ikan: {total_pakan:.2f} Ons")
        st.info(f"Jenis Pakan yang Disarankan: **{jenis_pakan}**")

    st.button("⬅ Kembali ke Halaman Utama", on_click=back_to_sampul)

# Menentukan halaman
if st.session_state.page == "sampul":
    halaman_sampul()
elif st.session_state.page == "prediksi":
    halaman_prediksi()
