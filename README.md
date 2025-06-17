# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang telah berdiri sejak tahun 2000 dan dikenal melahirkan lulusan berkualitas. Namun, tingginya angka siswa yang mengalami dropout menjadi tantangan serius bagi institusi ini. Untuk mengatasi masalah tersebut, diperlukan upaya deteksi dini terhadap siswa yang berisiko tidak menyelesaikan pendidikan. Dalam hal ini, diperlukan analisis data performa siswa dan membangun dashboard yang dapat membantu pemantauan serta pengambilan keputusan yang lebih tepat sasaran.

### Permasalahan Bisnis

Permasalahan bisnis utama yang dihadapi Jaya Jaya Institut adalah tingginya angka siswa yang mengalami dropout, yang tidak hanya berdampak pada reputasi institusi tetapi juga pada efisiensi dan efektivitas proses pembelajaran. Ketidakmampuan dalam mengidentifikasi siswa yang berisiko dropout secara dini membuat intervensi menjadi terlambat atau tidak tepat sasaran. Oleh karena itu, diperlukan sistem yang mampu menganalisis data performa siswa untuk memprediksi potensi dropout dan menyediakan informasi yang mudah dipahami melalui dashboard, guna mendukung pengambilan keputusan yang lebih cepat dan akurat oleh pihak institusi.

### Cakupan Proyek

1. Eksplorasi dan Pemahaman Data: Analisis dataset Students' Performance untuk memahami karakteristik siswa dan distribusi status dropout.
2. Data Preparation: Membersihkan dan memproses data agar siap digunakan untuk analisis lebih lanjut.
3. Analisis Faktor Penyebab Attrition: Analisis antara variabel seperti pendapatan, lembur, tingkat kepuasan, dan jarak rumah. Visualisasi tren dan pola attrition di berbagai departemen, level pekerjaan, dan usia karyawan.
   Pembuatan Business Dashboard: Visualisasi data dalam bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab attrition.
4. Kesimpulan dan Rekomendasi: Menarik kesimpulan dari hasil analisis dan memberikan rekomendasi praktis untuk mengurangi attrition.

### Persiapan

Sumber Data: [Student's performa](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut untuk setup environment:.

```
conda create --name student_performa python=3.12.9
```

3. Aktifkan virtual environment dengan menjalankan perintah berikut

```
conda activate student_performa
```

4. Instal semua library yang dibutuhkan menggunakan perintah berikut.

```
pip install -r requirements.txt
```

5. Buka jupyter-notebook dengan menjalankan perintah berikut.

```
jupyter-notebook
```

6. Memprediksi di file python

- Buka file python prediction.py
- Masukkan data yang ingin diprediksi pada variabel data_baru
- Tekan tombol run code
- Hasil prediksi akan keluar beserta deskripsinya

7. Menjalankan streamlit di local untuk prediksi student

```
streamlit run app.py
```

## Business Dashboard

Berdasarkan dashboard yang telah dibuat, terlihat bahwa sebagian besar siswa berhasil lulus (49,9%), namun angka dropout masih cukup signifikan (32,1%). Siswa dropout cenderung memiliki nilai masuk (admission grade) dan nilai kualifikasi yang lebih rendah dibanding yang lulus. Selain itu, dropout lebih sering terjadi pada siswa yang tidak menerima beasiswa, tidak mengikuti pendidikan khusus, memiliki status sebagai debitur, serta berasal dari lingkungan dengan tingkat pengangguran dan inflasi yang lebih tinggi. Faktor-faktor sosiodemografis seperti jenis kelamin, kehadiran, dan status perpindahan juga menunjukkan hubungan dengan status kelulusan, yang mengindikasikan adanya kebutuhan intervensi terarah pada kelompok-kelompok tertentu.

Link dashboard: https://lookerstudio.google.com/s/igFW6X79gas

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

1. Memprediksi di file python

- Buka file python prediction.py
- Masukkan data yang ingin diprediksi pada variabel new_data
- Tekan tombol run code
- Hasil prediksi akan keluar beserta deskripsinya

2. Memprediksi dengan Menjalankan streamlit di local untuk prediksi student

```
streamlit run app.py
```

3. Menjalankan streamlit di web app
   link streamlit: https://studentperformawildan.streamlit.app/

## Conclusion

Proyek ini berhasil mengidentifikasi faktor-faktor utama yang memengaruhi risiko dropout siswa di Jaya Jaya Institut melalui analisis data dan visualisasi interaktif. Hasil analisis menunjukkan bahwa siswa yang memiliki nilai masuk rendah, tidak menerima beasiswa, berstatus debitur, serta berasal dari wilayah dengan kondisi ekonomi yang kurang stabil lebih berisiko mengalami dropout. Dashboard yang dibangun mempermudah institusi dalam memantau performa siswa dan mengambil tindakan preventif terhadap kelompok berisiko.

Dari sisi pemodelan, algoritma yang digunakan menghasilkan akurasi sebesar 0.748, yang menunjukkan performa prediksi yang cukup baik. Model memiliki precision 0.90 pada kelas dropout (label 1), namun dengan recall 0.33, mengindikasikan bahwa masih ada banyak siswa dropout yang tidak terdeteksi oleh model. Hal ini terlihat pula dari nilai f1-score sebesar 0.48 pada kelas tersebut. Meskipun demikian, model cukup andal dalam mengklasifikasikan siswa yang tidak dropout, dengan recall 0.98 dan f1-score 0.83 pada kelas tersebut. Secara keseluruhan, model ini dapat digunakan sebagai alat bantu awal dalam mendeteksi risiko dropout, meskipun perlu dilakukan pengembangan lebih lanjut untuk meningkatkan sensitivitas terhadap siswa yang benar-benar berisiko.

### Rekomendasi Action Items

Berikut beberapa rekomendasi action items yang dapat dilakukan Jaya Jaya Institut untuk menyelesaikan permasalahan dropout dan mencapai target peningkatan retensi siswa:

- Action Item 1:
  Implementasi Sistem Peringatan Dini Berbasis Data
  Gunakan model prediksi yang telah dikembangkan untuk membangun sistem peringatan dini (early warning system) yang secara rutin mengidentifikasi siswa dengan risiko dropout tinggi. Data hasil analisis dapat digunakan oleh tim akademik dan konselor untuk melakukan pendekatan proaktif dan personalisasi intervensi terhadap siswa-siswa tersebut.

- Action Item 2:
  Pemberian Dukungan Finansial dan Akademik yang Tepat Sasaran
  Berdasarkan temuan bahwa siswa tanpa beasiswa dan yang memiliki tanggungan finansial lebih rentan terhadap dropout, institusi disarankan untuk memperluas akses beasiswa atau bantuan keuangan berbasis kebutuhan. Selain itu, program bimbingan belajar atau mentoring akademik juga dapat difokuskan pada kelompok siswa dengan nilai masuk rendah untuk meningkatkan peluang kelulusan mereka.
