# 📊 Belajar Analisis Data dengan Python

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12%2B-3776AB.svg)](https://seaborn.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Repository ini berisi kumpulan materi, eksperimen, latihan komprehensif, serta proyek akhir (*capstone project*) dari alur belajar **Analisis Data dengan Python** (Dicoding Academy). Seluruh kode telah direfaktor mengikuti **Best Practice PEP 8**, penanganan data modern menggunakan **Pandas 2+**, visualisasi bebas *deprecated warning* (**Seaborn & Matplotlib**), serta performa dashboard interaktif menggunakan **Streamlit**.

---

## 📌 Daftar Isi
- [Struktur Proyek](#-struktur-proyek)
- [Ikhtisar Modul](#-ikhtisar-modul)
  - [1. Statistik Dasar & EDA](#1-statistik-dasar--exploratory-data-analysis-eda)
  - [2. Data Cleaning & Wrangling](#2-data-cleaning--wrangling)
  - [3. Visualisasi Data](#3-visualisasi-data)
  - [4. Dasar Streamlit Widget & Layout](#4-dasar-streamlit-widget--layout)
  - [5. Proyek Akhir: E-Commerce Analytics Dashboard](#5-proyek-akhir-e-commerce-analytics-dashboard)
- [Peningkatan & Refactoring Best Practice](#-peningkatan--refactoring-best-practice)
- [Instalasi & Penggunaan](#-instalasi--penggunaan)
  - [Prasyarat](#prasyarat)
  - [Setup Environment](#setup-environment)
  - [Menjalankan Dashboard](#menjalankan-dashboard)
  - [Menjalankan Skrip Mandiri](#menjalankan-skrip-mandiri)
- [Temuan & Insight Bisnis Proyek Akhir](#-temuan--insight-bisnis-proyek-akhir)
- [Lisensi & Kredit](#-lisensi--kredit)

---

## 📂 Struktur Proyek

```plaintext
Belajar-Analisis-Data-dengan-Python/
│
├── Cleaning Data/                       # Teknik pembersihan dan preprocessing data
│   ├── Mission Value/                   # Penanganan missing values
│   │   ├── dropping_data.py             # Penghapusan baris/kolom kosong (dropna)
│   │   ├── imputation_data.py           # Imputasi nilai rata-rata/mean (fillna)
│   │   └── interpolation_data.py        # Interpolasi linear deret berkala
│   ├── Outlier/                         # Deteksi dan penanganan nilai ekstrem (outlier)
│   │   ├── drop_data.py                 # Filter pemotongan outlier via rentang IQR
│   │   └── imputation_data.py           # Winsorization / capping outlier via .clip()
│   └── drop_duplicate.py                # Pembersihan duplikasi baris
│
├── Data Visualization/                  # Eksplorasi grafik Matplotlib & Seaborn
│   ├── studi case/                      # Studi kasus visualisasi terapan
│   │   ├── BBCA_stock_price.py          # Line chart tren harga saham BBCA
│   │   └── penguin_spesies.py           # Scatter plot morfologi spesies pinguin
│   ├── bar_chart_matplotlib.py          # Bar chart horizontal Matplotlib
│   ├── bar_chart_seaborn.py             # Bar chart Seaborn
│   ├── box_plot_BBCA.py                 # Box plot sebaran harga saham
│   ├── clustered_bar_chart.py           # Clustered / grouped bar chart
│   ├── histogram_chart_matplotlib.py    # Histogram distribusi acak Matplotlib
│   ├── histogram_chart_seaborn.py       # Histogram distribusi Seaborn
│   ├── line_chart.py                    # Line chart dasar
│   ├── line_chart_BBCA.py               # Line chart harga penutupan BBCA
│   ├── scatter_plot_matplotlib.py       # Scatter plot dasar
│   ├── scatter_plot_penguin.py          # Scatter plot pinguin
│   ├── scatter_plot_seaborn.py          # Scatter plot dengan pengelompokan warna
│   ├── simple_bar_chart.py              # Bar chart sederhana
│   ├── simple_box_plot.py               # Box plot dasar
│   ├── simple_donut_chart.py            # Donut chart
│   └── simple_pie_chart.py              # Pie chart proporsi suara
│
├── latihan/
│   └── proyek_analisis_data/            # Proyek Akhir Analisis Data (Dicoding)
│       ├── all_data.csv                 # Dataset gabungan transaksi E-Commerce
│       ├── dashboard.py                 # Dashboard analitik interaktif Streamlit
│       └── notebook.ipynb               # Jupyter Notebook analisis data & EDA
│
├── streamlit/                           # Contoh modul & widget Streamlit
│   ├── button_widget.py                 # Widget button, checkbox, selectbox, slider
│   ├── column.py                        # Layout multikolom
│   ├── container.py                     # Container layout
│   ├── expander.py                      # Komponen expander lipat
│   ├── hello-world.py                   # Demo awal Streamlit
│   ├── input_widget.py                  # Text input, date picker, file uploader
│   ├── sidebar.py                       # Sidebar kontrol
│   ├── simple_chart_display.py          # Line chart bawaan Streamlit
│   ├── simple_data_display.py           # Dataframe, table, metric, json display
│   ├── simple_text.py                   # Typography & text styling
│   ├── tab.py                           # Navigasi tab
│   └── write.py                         # Eksekusi magic command st.write
│
├── correlation.py                       # Analisis korelasi antar fitur numerik
├── covariance.py                        # Analisis kovariansi antar fitur numerik
├── EDA_example.ipynb                    # Notebook contoh eksplorasi data
├── grafik_histogram.py                  # Histogram frekuensi kemunculan data
├── grouping_data.ipynb                  # Notebook agregasi & pengelompokan data
├── left_skewed.py                       # Perhitungan skewness distribusi data
├── nilai_iqr.py                         # Perhitungan Interquartile Range (IQR)
├── nilai_mean.py                        # Perhitungan nilai rata-rata (mean)
├── nilai_median.py                      # Perhitungan nilai tengah (median)
├── nilai_mode.py                        # Perhitungan modus (mode) yang sering muncul
├── nilai_range.py                       # Perhitungan jangkauan data (range)
├── nilai_stdev.py                       # Perhitungan standar deviasi sampel
├── nilai_variance.py                    # Perhitungan variansi data
├── requirements.txt                     # Daftar dependensi Python
└── README.md                            # Dokumentasi lengkap proyek
```

---

## 🧠 Ikhtisar Modul

### 1. Statistik Dasar & Exploratory Data Analysis (EDA)
Modul di root directory berfokus pada pemahaman parameter statistik deskriptif:
- **Ukuran Pemusatan Data (*Central Tendency*)**:
  - `nilai_mean.py`: Nilai rata-rata dari sebaran data.
  - `nilai_median.py`: Titik tengah dari data yang diurutkan (kebal terhadap outlier).
  - `nilai_mode.py`: Nilai yang paling sering muncul menggunakan `scipy.stats.mode`.
- **Ukuran Penyebaran Data (*Dispersion*)**:
  - `nilai_range.py`: Selisih nilai maksimum dan minimum.
  - `nilai_iqr.py`: Interquartile Range ($Q_3 - Q_1$), fondasi penentuan batas outlier.
  - `nilai_variance.py` & `nilai_stdev.py`: Derajat variabilitas dan simpangan baku data.
- **Bentuk Sebaran & Hubungan Antar Variabel**:
  - `left_skewed.py`: Derajat kemiringan distribusi (*skewness*).
  - `covariance.py`: Mengukur arah hubungan dua variabel (positif, negatif, atau netral).
  - `correlation.py`: Matriks korelasi Pearson standar antar variabel numerik.

### 2. Data Cleaning & Wrangling
Terletak di folder `Cleaning Data/`, mencakup implementasi standar industri untuk pembersihan data:
- **Missing Value Handling**:
  - **Dropping (`dropping_data.py`)**: Menghapus baris/kolom kosong menggunakan `dropna()`.
  - **Imputation (`imputation_data.py`)**: Mengisi nilai kosong dengan mean/median kolom tanpa mutasi inplace yang *deprecated*.
  - **Interpolation (`interpolation_data.py`)**: Mengisi titik data waktu/berkala menggunakan interpolasi linear teratur.
- **Outlier Handling**:
  - **Trimming (`drop_data.py`)**: Memotong data di luar batas $Q_1 - 1.5 \times \text{IQR}$ dan $Q_3 + 1.5 \times \text{IQR}$.
  - **Winsorization / Capping (`imputation_data.py`)**: Membatasi nilai ekstrem ke ambang batas wajar menggunakan fungsi vectorized `.clip(lower, upper)`.
- **Deduplikasi (`drop_duplicate.py`)**: Mendeteksi dan menghapus baris duplikat.

### 3. Visualisasi Data
Terletak di folder `Data Visualization/`, mendemonstrasikan perbandingan teknik visualisasi dengan **Matplotlib** dan **Seaborn**:
- **Distribusi**: Histogram (`histogram_chart_*.py`) dan Box Plot (`box_plot_BBCA.py`).
- **Komparasi**: Simple Bar Chart, Horizontal Bar Chart, dan Grouped/Clustered Bar Chart.
- **Proporsi**: Pie Chart (`simple_pie_chart.py`) dan Donut Chart (`simple_donut_chart.py`).
- **Hubungan & Tren**: Scatter Plot (`scatter_plot_*.py`) dan Line Chart deret waktu saham BBCA (`line_chart_BBCA.py`, `studi case/BBCA_stock_price.py`).

### 4. Dasar Streamlit Widget & Layout
Folder `streamlit/` menyajikan contoh penggunaan komponen antarmuka web interaktif:
- Input widgets: Text input, date picker, sliders, selectbox, radio button.
- Layouts: Columns, Containers, Tabs, Expanders, dan Sidebar.
- Visualisasi metrik bisnis: `st.metric()`, `st.dataframe()`, dan integrasi figure Matplotlib.

### 5. Proyek Akhir: E-Commerce Analytics Dashboard
Aplikasi analitik interaktif yang terletak di `latihan/proyek_analisis_data/dashboard.py`. Aplikasi ini mengolah dataset transaksi e-commerce publik (`all_data.csv`) untuk menjawab pertanyaan bisnis strategis:
1. **Daily Orders & Total Revenue**: Tren harian pesanan dan pertumbuhan pendapatan.
2. **Best & Worst Performing Products**: Produk terlaris vs produk dengan penjualan paling sedikit.
3. **Customer Demographics**: Profil pelanggan berdasarkan jenis kelamin (*gender*), kelompok usia (*Youth, Adults, Seniors*), serta distribusi geografis negara bagian (*states*).
4. **RFM Analysis (Recency, Frequency, Monetary)**:
   - **Recency**: Kapan terakhir kali pelanggan bertransaksi (hari).
   - **Frequency**: Seberapa sering pelanggan melakukan pesanan.
   - **Monetary**: Total uang yang dibelanjakan pelanggan.

---

## 🛠️ Peningkatan & Refactoring Best Practice

Kode dalam repository ini telah diperbarui dengan standar rekayasa perangkat lunak modern:

| Komponen | Kondisi Sebelumnya | Perbaikan & Best Practice |
|---|---|---|
| **`nilai_iqr.py`** | Mencetak objek fungsi built-in `range` (`<class 'range'>`). | Diperbaiki agar mencetak nilai variabel `iqr` hasil kalkulasi kuartil. |
| **`nilai_range.py`** | Nama variabel `range` menimpa (*shadowing*) fungsi built-in Python; komentar menyebut "Median". | Diubah menjadi `range_nilai` dan komentar diperbaiki menjadi "Range". |
| **`nilai_mode.py`** | Pengambilan indeks `[0]` rentan *IndexError* / *DeprecationWarning* pada SciPy terbaru. | Menggunakan normalisasi numpy array `mode_result.mode` yang kompatibel di semua versi SciPy. |
| **`Outlier/imputation_data.py`** | Terdapat `SyntaxError: positional argument follows keyword argument` pada pemanggilan `df.mask`. | Diganti dengan metode idiomatik Pandas: `.clip(lower=minimum, upper=maximum)`. |
| **`Outlier/drop_data.py`** | Memanggil `df.drop()` dua kali secara sekuensial. | Diganti dengan boolean filtering satu langkah: `df[(df >= min) & (df <= max)]`. |
| **Pandas Mutating Inplace** | Peringatan *FutureWarning: inplace=True on Series is deprecated*. | Diubah menjadi penugasan eksplisit: `df['col'] = df['col'].fillna(...)`. |
| **Yahoo Finance URLs** | Script saham BBCA mengalami crash langsung jika diblokir `HTTP 429 Too Many Requests`. | Ditambahkan blok `try-except` dengan generator data simulasi realistis sebagai fallback transparan. |
| **Dashboard Path Resolution** | `pd.read_csv("all_data.csv")` gagal (*FileNotFoundError*) jika dijalankan dari root directory. | Menggunakan path dinamis absolut: `Path(__file__).resolve().parent / "all_data.csv"`. |
| **Dashboard Caching** | File CSV dibaca ulang dan di-parsing tanggalnya pada setiap interaksi pengguna. | Dioptimalkan dengan decorator `@st.cache_data`. |
| **Streamlit Date Range** | *ValueError* saat pengguna baru memilih 1 tanggal pada pemilih rentang waktu. | Proteksi unpacking tuple yang aman dengan pengecekan panjang elemen `len(date_range) == 2`. |
| **Seaborn Barplot Palette** | *FutureWarning: Passing palette without assigning hue is deprecated*. | Ditambahkan parameter `hue` dan `legend=False` serta penyesuaian panjang palette warna. |
| **RFM Metric Bug** | Variabel `avg_frequency` digunakan ulang untuk metric Monetary pada dashboard. | Diperbaiki menjadi variabel `avg_monetary` yang semantik. |

---

## 🚀 Instalasi & Penggunaan

### Prasyarat
- Python versi 3.9 atau lebih baru.
- Pip (Python package manager).

### Setup Environment
1. **Clone repository ini:**
   ```bash
   git clone https://github.com/MHendriF/Belajar-Analisis-Data-dengan-Python.git
   cd Belajar-Analisis-Data-dengan-Python
   ```

2. **Buat dan aktifkan virtual environment:**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependensi yang diperlukan:**
   ```bash
   pip install -r requirements.txt
   ```

---

### Menjalankan Dashboard
Jalankan dashboard Streamlit melalui terminal dari root folder:

```bash
streamlit run latihan/proyek_analisis_data/dashboard.py
```

Dashboard akan otomatis terbuka di browser pada URL lokal: `http://localhost:8501`.

---

### Menjalankan Skrip Mandiri
Setiap skrip latihan dapat dijalankan secara mandiri, misalnya:

```bash
# Menghitung statistik dasar
python nilai_mean.py
python nilai_iqr.py
python correlation.py

# Menjalankan pembersihan data
python "Cleaning Data/drop_duplicate.py"
python "Cleaning Data/Outlier/imputation_data.py"

# Menjalankan visualisasi data
python "Data Visualization/studi case/penguin_spesies.py"
python "Data Visualization/studi case/BBCA_stock_price.py"
```

---

## 📈 Temuan & Insight Bisnis Proyek Akhir

Berdasarkan eksplorasi pada dataset transaksi e-commerce:

1. **Pola Transaksi & Musiman**:
   - Volume pesanan harian berfluktuasi dengan lonjakan yang sering terjadi pada periode promosi tertentu.
2. **Kinerja Produk**:
   - Kategori produk fashion (*denim*, *trousers*, dan *jacket*) menduduki peringkat teratas dalam kuantitas penjualan.
   - Perlu evaluasi strategi promosi atau stok untuk produk-produk di barisan bawah (*worst performing*) guna meminimalkan biaya penyimpanan (*holding cost*).
3. **Demografi Pelanggan**:
   - Mayoritas basis pelanggan adalah segmen usia dewasa (*Adults*), diikuti oleh segmen remaja (*Youth*).
   - Distribusi pelanggan tersebar luas dengan konsentrasi tinggi di beberapa negara bagian utama seperti South Australia, New South Wales, dan Queensland.
4. **Segmentasi RFM**:
   - Sebagian besar pelanggan memiliki recency transaksi yang sehat, namun frekuensi pesanan rata-rata masih didominasi pembelian tunggal.
   - Rekomendasi: Terapkan program loyalitas dan kampanye *retargeting* otomatis untuk meningkatkan frekuensi pembelian ulang (*repeat order rate*).

---

## 📜 Lisensi & Kredit

- **Sumber Materi**: [Dicoding Academy](https://www.dicoding.com/) — Kelas *Belajar Analisis Data dengan Python*.
- **Author / Maintainer**: M. Hendri Febriansyah
- **Lisensi**: Proyek ini dilisensikan di bawah lisensi MIT. Silakan gunakan untuk keperluan studi dan referensi.
