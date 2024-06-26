import streamlit as st
import pickle
import pandas as pd

st.title('Mendiagnosa Penyakit Hewan Ternak Sapi')

# Inisialisasi variabel hasil checkbox
hasil_checkbox = {
    "anorexia": 0,
    "bulu kusam": 0,
    "kekurusan": 0,
    "lemah": 0,
    "mencret": 0,
    "gatal": 0,
    "leleran nanah vulva": 0,
    "hidung beringus": 0,
    "demam": 0,
    "pincang": 0,
    "lumpuh": 0,
    "bulu rontok": 0,
    "radang mata": 0,
    "luka berdarah": 0,
    "mencret berdarah": 0,
    "ovarium kecil keras": 0,
    "berahi tenang": 0,
    "tidak ada ovulasi": 0,
    "ovarium kenyal dan licin": 0,
    "anestrus": 0,
    "corpus luteum tidak sempurna": 0,
    "daun telinga berkopeng": 0,
    "partus": 0,
    "fases kering keras": 0,
    "rahim bernanah": 0
}

# Membagi layout menjadi tiga kolom
col1, col2, col3 = st.columns(3)

# Menampilkan checkbox di kolom pertama
with col1:
    st.header("")
    check1 = st.checkbox('Anorexia')
    check2 = st.checkbox('Bulu Kusam')
    check3 = st.checkbox('Kekurusan')
    check4 = st.checkbox('Lemah')
    check5 = st.checkbox('Mencret')
    check6 = st.checkbox('Gatal')
    check7 = st.checkbox('Leleran Nanah')
    check8 = st.checkbox('Hidung Beringus')
    # Lanjutkan untuk checkbox lainnya di kolom pertama

# Menampilkan checkbox di kolom kedua
with col2:
    st.header("")
    check9 = st.checkbox('Demam')
    check10 = st.checkbox('Pincang')
    check11 = st.checkbox('lumpuh')
    check12 = st.checkbox('Bulu Rontok')
    check13 = st.checkbox('Radang Mata')
    check14 = st.checkbox('Luka Berdarah')
    check15 = st.checkbox('Mencret Berdarah')
    check16 = st.checkbox('Ovarium kecil dan keras')
    
    
    # Lanjutkan untuk checkbox lainnya di kolom kedua

# Menampilkan checkbox di kolom ketiga
with col3:
    st.header("")
    check17 = st.checkbox('Berahi Tenang')
    check18 = st.checkbox('Tidak ada ovolusi')
    check19 = st.checkbox('Ovarium kenyal dan licin')
    check20 = st.checkbox('Anesterus')
    check21 = st.checkbox('Corpus Lotum Tidak Sempurna')
    check22 = st.checkbox('Daun Telinga Berkopeng')
    check23 = st.checkbox('Partus')
    check24 = st.checkbox('Fases Kering')
    check25 = st.checkbox('Rahim  bernanah')
    # Lanjutkan untuk checkbox lainnya di kolom ketiga

# Logika untuk mengatur nilai checkbox menjadi 1 jika dicentang
if check1:
    hasil_checkbox["anorexia"] = 1
if check2:
    hasil_checkbox["bulu kusam"] = 1
if check3:
    hasil_checkbox["kekurusan"] = 1
if check4:
    hasil_checkbox["lemah"] = 1
if check5 :
    hasil_checkbox["mencret"] = 1
if check6 :
    hasil_checkbox["gatal"] = 1
if check7 :
    hasil_checkbox["leleran nanah vulva"] = 1
if check8 :
    hasil_checkbox["hidung beringus"] = 1
if check9 :
    hasil_checkbox["demam"] = 1
if check10 :
    hasil_checkbox["pincang"] = 1
if check11 :
    hasil_checkbox["lumpuh"] = 1
if check12 :
    hasil_checkbox["bulu rontok"] = 1
if check13 :
    hasil_checkbox["radang mata"] = 1
if check14 :
    hasil_checkbox["luka berdarah"] = 1
if check15 :
    hasil_checkbox["mencret berdarah"] = 1
if check16 :
    hasil_checkbox["ovarium kecil keras"] = 1
if check17 :
    hasil_checkbox["berahi tenang"] = 1
if check18 :
    hasil_checkbox["tidak ada ovulasi"] = 1
if check19 :
    hasil_checkbox["ovarium kenyal dan licin"] = 1
if check20 :
    hasil_checkbox["anestrus"] = 1
if check21 :
    hasil_checkbox["corpus luteum tidak sempurna"] = 1
if check22 :
    hasil_checkbox["daun telinga berkopeng"] = 1
if check23 :
    hasil_checkbox["partus"] = 1
if check24 :
    hasil_checkbox["fases kering keras"] = 1
if check25 :
    hasil_checkbox["rahim bernanah"] = 1
# Lanjutkan untuk checkbox lainnya

# Membaca model yang telah di-train
with open('RF-Baru.pkl', 'rb') as f:
    model = pickle.load(f)

# Membuat DataFrame dari input data
input_df = pd.DataFrame([hasil_checkbox])

# Menampilkan tombol "Predict"
if st.button('Predict'):
    prediction = model.predict(input_df)[0]

    # Menampilkan hasil diagnosa
    if prediction == 'avitaminosis':
        st.write('Hasil diagnosa adalah Avitaminosis')
    elif prediction == 'Bovine Ephemeral Fever':
        st.write('Hasil diagnosa adalah Bovine Ephemeral Fever')
    elif prediction == 'cacingan':
        st.write('Hasil diagnosa adalah cacingan')
    elif prediction == 'scabies':
        st.write('Hasil diagnosa adalah Scabies')
    elif prediction == 'coccidiosis':
        st.write('Hasil diagnosa adalah coccidiosis')
    elif prediction == 'Hipofungsi Ovari':
        st.write('Hasil diagnosa Hipofungsi Ovari')
    elif prediction == 'Corpus Luteum Persisten':
        st.write('Hasil diagnosa Corpus Luteum Persisten')
    elif prediction == 'Baliziekte':
        st.write('Hasil diagnosa adalah Baliziekte')
    elif prediction == 'Endometritis':
        st.write('Hasil diagnosa adalah Endometritis')
    elif prediction == 'Thelaziasis':
        st.write('Hasil diagnosa adalah Thelaziasis')
