import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

st.set_page_config(layout='wide',
                    page_title='Bike Sharing Analysis Dashboard',
                    page_icon=':bike',
                    initial_sidebar_state='expanded')

# Header Section
st.subheader("""
        :bike: Analisis Pengguna Rental Sepeda dari Capital Bikeshare System Washington D.C, Amerika Serikat Tahun 2011-2012 :bike:
        """)

img=Image.open('images/bike.jpg')
st.image(img, width=600)

st.write("""
        Sistem rental sepeda adalah generasi baru dari persewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian kembali menjadi otomatis.
        
        Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi ke posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam masalah lalu lintas, lingkungan dan kesehatan.

        Terlepas dari penerapan sistem rental sepeda di dunia nyata yang menarik, karakteristik data yang dihasilkan oleh sistem ini menjadikannya menarik untuk penelitian. Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan, keberangkatan, dan posisi kedatangan dicatat secara eksplisit dalam sistem ini. Fitur ini mengubah sistem berbagi menjadi jaringan sensor virtual yang dapat digunakan untuk mendeteksi mobilitas dalam kota. 
        
        Oleh karena itu, peristiwa-peristiwa terpenting di kota tersebut diharapkan dapat dideteksi dengan memantau data ini.
        """)

st.write("""
        Untuk lebih memahami analisis rental sepeda, berikut akan di jabarkan penjelasan dataset berupa visualisasi dan insight.
        """)

# Side Section
with st.sidebar:
        st.header("""
                Bike Sharing Analysis Dashboard
                """)
        st.write("""
                The Dashboard was created for final project of Belajar Analisis Data dengan Python - IDcamp 2023 collaborated with Dicoding Indonesia
                """)
        st.write('Created by [Lingga Rizki Mandala](https://www.linkedin.com/in/linggarizkim/)')


# Load cleaned data
cleaned_df = pd.read_csv('data/cleaned_data.csv')

# Visualisasi 1
st.subheader('Jumlah Penyewa Rental Sepeda dalam Harian')
df_weekday = cleaned_df.groupby(['year', 'weekday'])['count'].sum().reset_index()
plt.figure(figsize=(20,10))
ax = sns.barplot(x='weekday', y='count', data=df_weekday, hue='year', errorbar=None)
ax.bar_label(ax.containers[0] , fontsize=12)
ax.bar_label(ax.containers[1], fontsize=12)
plt.tick_params(axis='both', which='major')
plt.xlabel('Day', fontsize=12)
plt.ylabel('Jumlah Pengguna', fontsize=12)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 1
st.write("""
        Terlihat bahwa jumlah penyewa Bike Sharing pada tahun 2011 rata-rata sebanyak 177.586 orang, dan mengalami kenaikan signifikan pada tahun 2012 rata-rata sebanyak 292.796 orang. Kenaikan pengguna Bike Sharing tersebut mencapai 64.8%. Pada tahun 2012 jumlah penyewa rental sepeda terbanyak pada hari rabu, kamis, jumat, dan sabtu di hari kerja. Hari minggu menempati posisi terendah karena memang hari libur, sehingga tidak banyak pengguna rental sepeda yang menggunakan jasa ini dibanding hari kerja.
        """)

# Visualisasi 2
st.subheader('Jumlah Pengguna Rental Sepeda dalam Bulanan')
df_month = cleaned_df.groupby(['year', 'month'])['count'].sum().reset_index()
plt.figure(figsize=(20,10))
ax = sns.barplot(x='month', y='count', data=df_month.sort_values('month'), hue='year', errorbar=None)
ax.bar_label(ax.containers[0], fontsize=12)
ax.bar_label(ax.containers[1], fontsize=12)
plt.tick_params(axis='both', which='major')
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Pengguna', fontsize=12)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 2
st.write("""
        Pada tahun 2011 di bulan Januari, jumlah pengguna rental sepeda mencapai titik terendah, namun mengalami kenaikan setiap bulan hingga bulan Juni dan Juli masing-masing pengguna berjumlah 140.000 orang. Pada Tahun 2012 mengalami lonjakan pengguna dibanding tahun sebelumnya. Peningkatan pengguna terus mengalami kenaikan setiap bulan hingga puncaknya pada September 2012 dengan total pengguna sebanyak 218.573 orang. Dan bulan Oktober hingga penghujung akhir 2022 mengalami penurunan. 
        """)


# Visualisasi 3
st.subheader('Jumlah Pengguna Rental Sepeda pada Hari Kerja')

# Pie Chart Tahun 2011
df_2011 = cleaned_df[cleaned_df['year'] == 2011]
plt.figure(figsize=(15,8))
plt.subplot(1, 2, 1)
df_2011 = df_2011.groupby('workingday')['count'].sum()
plt.pie(df_2011, labels=df_2011.index, autopct='%1.1f%%', startangle=0)
plt.title('Tahun 2011')

# Pie Chart Tahun 2012
df_2012 = cleaned_df[cleaned_df['year'] == 2012]
plt.subplot(1, 2, 2)
df_2012 = df_2012.groupby('workingday')['count'].sum()
plt.pie(df_2012, labels=df_2012.index, autopct='%1.1f%%', startangle=0)
plt.title('Tahun 2012')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 3
st.write("""
        Pada visualisasi kategori harian diatas, bisa terlihat bahwa pengguna rental sepeda didominasi pada saat hari kerja ketimbang hari libur. Dan terlihat dari 2 pie chart bahwa mayoritas pengguna sepeda yang menggunakan fasilitas tersebut di hari kerja sebanyak 68.9% tahun 2011, dan mengalami sedikit kenaikan pada tahun 2012 yaitu 70.1%. Untuk lebih memahami seberapa banyak pengguna rental sepeda bisa di lihat pada gambar di bawah ini.
        """)

# Visualisasi 4

# Plot Tahun 2011
df_2011 = cleaned_df[cleaned_df['year'] == 2011]
df_2011_grouped = df_2011.groupby('workingday')['count'].sum().reset_index()

plt.figure(figsize=(15,8))
plt.subplot(1, 2, 1)
ax = sns.barplot(x='workingday', y='count', data=df_2011_grouped,errorbar=None)
ax.bar_label(ax.containers[0], fmt='%.0f', fontsize=14)
plt.xlabel('Hari Kerja')
plt.ylabel('Jumlah Pengguna')
plt.title('Tahun 2011')

# Plot Tahun 2012
df_2012 = cleaned_df[cleaned_df['year'] == 2012]
df_2012_grouped = df_2012.groupby('workingday')['count'].sum().reset_index()

plt.subplot(1, 2, 2)
ax = sns.barplot(x='workingday', y='count', data=df_2012_grouped, errorbar=None)
ax.bar_label(ax.containers[0], fmt='%.0f', fontsize=14)
plt.xlabel('Hari Kerja')
plt.ylabel('Jumlah Pengguna')
plt.title('Tahun 2012')

plt.ticklabel_format(style='plain', axis='y')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 4
st.write("""
        Pada gambar ini ditampilkan total pengguna rental sepeda yang menggunakan pada hari kerja dari tahun 2011 dan 2012. Sebanyak 856.264 pengguna layanan ini pada tahun 2011, dan mengalami kenaikan 1.2% pada tahun 2012, yaitu sebanyak 1.436.146 pengguna.
        """)

# Visualisasi 5
st.subheader('Persentase Cuaca terhadap Pengguna Rental Sepeda')

# Plot tahun 2011
df_2011 = cleaned_df[cleaned_df['year'] == 2011]
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
df_2011 = df_2011.groupby('weather')['count'].sum()
ax = plt.pie(df_2011, labels=df_2011.index, autopct='%1.1f%%', startangle=90)
plt.title('Tahun 2011')

# Plot tahun 2012
df_2012 = cleaned_df[cleaned_df['year'] == 2012]
plt.subplot(1, 2, 2)
df_2012 = df_2012.groupby('weather')['count'].sum()
ax = plt.pie(df_2012, labels=df_2012.index, autopct='%1.1f%%', startangle=90)
plt.title('Tahun 2012')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 5
st.write("""
        Persentase cuaca cerah (clear) mencapai 67.2%, yang berarti aktivitas pengguna rental sepeda menggunakan fasilitas ini di kondisi cuaca cerah. Selanjutnya pada cuaca berawan (cloudy) mencapai 30.8%. Hanya 2% pengguna rental sepeda yang menggunakan fasilitas ini pada saat kondisi hujan. Namun pada tahun 2012, kenaikan pengguna mencapai 69.4% pada kondisi cerah, dan 30% pada kondisi berawan. Bagaimana dengan suhu rata-rata terhadap kondisi cuaca yang mempengaruhi pengguna rental sepeda? Simak pada gambar di bawah ini.
        """)

# Visualisasi 6
st.subheader('Pengaruh suhu rata-rata terhadap kondisi Cuaca')
plt.figure(figsize=(12, 5))
sns.lineplot(x='month', y='atemp', data=cleaned_df, hue='weather', marker='o')
plt.tick_params(axis='both', which='major')
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Suhu Rata-rata (dalam celsius)', fontsize=12)
plt.legend(title='Kondisi Cuaca')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 6
st.write("""
        Pengaruh suhu rata-rata terhadap kondisi cuaca pada bulan Januari ada di titik rendah. Dikarenakan bulan Januari merupakan puncaknya musim dingin, sehingga suhu rata-rata terendah dibandingkan bulan lainnya. Seiring berjalannya waktu, suhu rata-rata meningkat setiap bulannya. Hingga memasuki musim panas pada bulan Juni hingga September di atas 30∘C dan puncaknya pada bulan Juli dengan suhu rata-rata kisaran 35∘C. Memasuki musim gugur pada bulan September suhu rata-rata menurun sampai memasuki musim dingin pada bulan Desember.
        """)

# Kesimpulan
st.subheader("""Analisis Kesimpulan""")

st.write("""
        Berdasarkan hasil visualisasi data di atas, dapat disimpulkan sebagai berikut:
        1. Pengguna rental sepeda (Bike Sharing) di kota Washington D.C, Amerika Serikat didominasi oleh pengguna pada hari kerja, yaitu mulai senin hingga sabtu. Pada tahun 2011 pengguna layanan tersebut mencapai 68.9% dan meningkat 70.1% pada tahun 2012.
        2. Tahun 2011, jumlah pengguna rental sepeda harian ada rata-rata 177.586 orang, dan meningkat pada tahun 2012 dengan rata-rata pengguna 292.796 orang. Karena banyaknya pengguna di hari kerja, peningkatan pada tahun 2012 terjadi mulai hari selasa hingga puncaknya di hari jumat.
        3. Kondisi cuaca juga mempengaruhi pengguna rental sepeda karena banyaknya pengguna yang menggunakan layanan tersebut pada cuaca cerah, dan hanya 30% yang menggunakan saat kondisi berawan. Tren peningkatan pengguna bisa dilihat pada bulanannya dimana tahun 2012 peningkatan terlihat saat musim semi hingga puncaknya musim panas, yaitu pada bulan maret hingga september.
        """)