import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

with st.sidebar:
    choose = option_menu("App Menu",["About","Data","Visualization","Conclusion","Contact Me"],
    icons=['house','server','palette-fill','journal-check','person lines fill'],
    menu_icon="app-indicator", default_index=0,
    styles={
        "container": {"padding": "5!important", "Background-color": "#fafafa"},
        "icon": {"color": "magenta", "font-size": "25px"},
        "nav-link-selected" : {"background-color": "#ff007f"}      
    }
    )
if choose == "About":
    st.title('Introduction')
    st.markdown('Hi, selamat datang di aplikasi portofolio saya tentang data analisis sebelum itu perkenalkan nama saya Vakris Candra Sasmita adalah lulusan S1 Matematika yang tertarik dan memiliki minat besar dalam ilmu data di sini saya akan menampilkan karya dari hasil analisis data yang telah saya pelajari, saya menggunakan bahasa pemrograman Python dan dengan bantuan sebuah library bernama streamlit untuk membuat aplikasi web sederhana untuk menampilkan hasil analisa. Sebelum itu mari simak pembahasan mengenai analisis data, tahap analisis data. Dari aplikasi web ini terdapat menu sidebar yang dapat menampilkan pilihan bahasan dan dengan satu kali klik akan menampilkan isi dari menu tersebut. Langsung saja mari kita mulai.')
    st.markdown('##### Apa itu analisis data?')
    st.markdown('Pengertian Teknik Analisis Data. Teknik analisis data merupakan suatu proses mengolah data menjadi informasi baru. Proses ini dilakukan bertujuan agar karakteristik data menjadi lebih mudah dimengerti dan berguna sebagai solusi bagi suatu permasalahan, khususnya yang berkaitan dengan penelitian. Tetapi analisis data dan data analis merupakan hal yang berbeda data analis adalah seorang yang bekerja untuk melakukan analisis data untuk digunakan dalam keperluan bisnis, pemerintah, kesehatan, lembaga non profit dan masih banyak lagi.')
    st.markdown('##### Proses Analisis')
    st.markdown('1. Bertanya: Mengajukan pertanyaan yang efektif, Mendefinisikan masalah, Menggunakan pemikiran terstruktur, Berkomunikasi dengan orang lain ')
    st.markdown('2. Mempersiapkan: Memahami bagaimana data dihasilkan dan dikumpulkan, Mengidentifikasi dan menggunakan format, jenis, dan struktur data yang berbeda, Memastikan data kredibel dan tidak bias, Menyusun dan melindungi data')
    st.markdown('3. Memproses: Membuat dan mengubah data, Mempertahankan integritas data, Menguji data, Membersihkan data, Memverifikasi dan melaporkan hasil pembersihan')
    st.markdown('4. Menganalisis: Menggunakan alat-alat untuk memformat dan mengubah data, Mengurutkan dan menyaring data, Mengidentifikasi pola dan menarik kesimpulan, Membuat prediksi dan rekomendasi, Mengambil keputusan berdasarkan data')
    st.markdown('5. Membagikan: Memahami visualisasi, Membuat visual yang efektif, Menghidupkan data, Menggunakan penceritaan data, Berkomunikasi untuk membantu orang lain memahami hasil analisa')
    st.markdown('6. Bertindak: Menerapkan wawasan Anda, Menyelesaikan masalah, Mengambil keputusan, Membuat hal baru.')
    
elif choose == "Data":
    st.title('Data')
    st.markdown('Data yang digunakan adalah data sebuah perusahaan bergerak pada penjualan retail yang disimpan dalam database yang terdiri dari tabel penjualan dan tabel produk.')
    st.markdown('##### Tabel Order')
    order = pd.read_csv('data/superstore_order.csv')
    order
    st.markdown('Berikut ini penjelasan tentang atribut dari tabel penjualan.')
    st.markdown('1. Order ID : merupakan sebuah kode unik untuk sebuah transaksi pemesanan')
    st.markdown('2. Order Date : tanggal pemesanan atau pembelian')
    st.markdown('3. Ship Date : tanggal dimana barang dikemas dan dikirim ke pembeli')
    st.markdown('4. Ship Mode : jenis pengiriman terdiri dari 3 kategori First Class, Second Class, Standard Class')
    st.markdown('5. Customer ID : kode unik untuk seorang pelanggan')
    st.markdown('6. Product ID : kode unik dari setiap barang')
    st.markdown('7. Sales : nominal dari sebuah transaksi')
    st.markdown('8. Quantity : banyak barang yang dipesan')
    st.markdown('9. Discount : potong harga dari suatu barang')
    st.markdown('10. Profit : laba yang diperoleh dari suatu barang')
    st.markdown('##### Tabel Product')
    product = pd.read_csv('data/superstore_product.csv')
    product
    st.markdown('Dan untuk atribut dari tabel produk adalah sebagai berikut ini:')
    st.markdown('1. Product ID : kode unik dari setiap barang')
    st.markdown('2. Product name : nama dari suatu barang atau produk')
    st.markdown('3. Category : Kategori barang meliputi furniture, office supplies, technology')
    st.markdown('4. Sub-category : sub-kategori dari setiap kategori barang.')    

elif choose == "Visualization":
    st.title('Data Visualization')
    df0 = pd.read_csv('data/superstore_order.csv')
    a1, a2, a3 = st.columns(3)
    a1.metric("Sales",'$2.3M')
    a2.metric("Profit",'$286,397.02')
    a3.metric("AVG Discount",'15.6%')
    b1, b2 = st.columns(2)
    b1.metric("Best Seller", 'Logitech P710e Mobile Speakerphone')
    
    st.markdown('Peratama kita akan selidiki laba dan jumlah penjualan barang pada tahun 2014-2017 melalui gambar diagram garis dibawah ini.')
    plt.rcParams["font.family"] = "Sans serif"
    df1 = pd.read_csv('data/sales2014.csv')
    df2 = pd.read_csv('data/sales2015.csv')
    df3 = pd.read_csv('data/sales2016.csv')
    df4 = pd.read_csv('data/sales2017.csv')
    fig = plt.figure(figsize=(10,5))
    plt.plot(df1['txtbulan'],df1['sales'], label='2014')
    plt.plot(df2['txtbulan'],df2['sales'], label='2015')
    plt.plot(df3['txtbulan'],df3['sales'], label='2016')
    plt.plot(df4['txtbulan'],df4['sales'], label='2017')
    plt.legend()
    plt.title('Sales 2014 - 2017')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.annotate('Max (USD 118,447.82)', xy=(10, 118447.82), xytext=(7, 110000),
    arrowprops=dict(arrowstyle="->", color='k',
                    connectionstyle="angle3,angleA=-90,angleB=0"))
    plt.annotate('Min (USD 4,519.89)', xy=(1, 4519.89), xytext=(2.5, 10000),
    arrowprops=dict(arrowstyle="->", color='k',
                    connectionstyle="angle3,angleA=90,angleB=180"))
    st.pyplot(fig)
    fig = plt.figure(figsize=(10,5))
    dtf1 = pd.read_csv('data/profit2014.csv')
    dtf2 = pd.read_csv('data/profit2015.csv')
    dtf3 = pd.read_csv('data/profit2016.csv')
    dtf4 = pd.read_csv('data/profit2017.csv')
    plt.plot(dtf1['txtbulan'],dtf1['profit'], label='2014')
    plt.plot(dtf2['txtbulan'],dtf2['profit'], label='2015')
    plt.plot(dtf3['txtbulan'],dtf3['profit'], label='2016')
    plt.plot(dtf4['txtbulan'],dtf4['profit'], label='2017')
    plt.legend()
    plt.title('Profit 2014 - 2017')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    plt.annotate('Max ($17,885.3)', xy=(11, 17885.3093), xytext=(9.05, 15900),
    arrowprops=dict(arrowstyle="->", color='k',
                    connectionstyle="angle3,angleA=-90,angleB=0"))
    plt.annotate('Min ($-3,281)', xy=(0, -3281.0070), xytext=(2, -1000),
    arrowprops=dict(arrowstyle="->", color='k',
                    connectionstyle="angle3,angleA=90,angleB=180"))
    st.pyplot(fig)
    st.markdown('Pada diagram garis diatas terlihat laba pada bulan Januari 2015 mengalami kerugian tetapi penjualan terlihat lebih besar daripada bulan yang sama pada tahun sebelumnya. akan diselidiki data keuntungan berdasarkan kategori barang yang terjual')    
    dpp = pd.read_csv('data/profitcategory.csv')
    fig = plt.figure(figsize=(10,5))
    category = dpp['category']
    labels = ["6,4% Furniture",
            "42,8% Office Supplies",
            "50,8% Technology"]
    profit, texts = plt.pie(dpp['total_profit'], wedgeprops=dict(width=0.5), startangle=-40)
    bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
                    bbox=bbox_props, zorder=0, va="center")
    for i, p in enumerate(profit):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle, angleA=0, angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(labels[i], xy=(x,y), xytext=(1.35*np.sign(x),1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
        plt.title("Total Profit by Category")
    st.pyplot(fig)
    st.markdown('Kategori barang yang menyumbang keuntungan terbesar adalah dari kategori Technology dan kategori Office Supplies.')

    fig = plt.figure(figsize=(10,5))
    jd = pd.read_csv('data/Jan2015.csv')
    category = jd['category']
    labels = ["88 Unit Furniture",
            "110 Unit Office Supplies",
            "38 Unit Technology"]
    profit, texts = plt.pie(jd['total_sales'], wedgeprops=dict(width=0.5), startangle=-40)
    bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
                    bbox=bbox_props, zorder=0, va="center")
    for i, p in enumerate(profit):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle, angleA=0, angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(labels[i], xy=(x,y), xytext=(1.35*np.sign(x),1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
        plt.title("Total Sales January 2015 by Category")
    st.pyplot(fig)

    fig = plt.figure(figsize=(10,5))
    dsc = pd.read_csv('data/rata_discountctgr.csv')
    bar = plt.bar(dsc['category'],dsc['rata_discount'], color="orange")
    plt.title('Rata-rata Discount Kategori Barang Januari 2015')
    plt.annotate('35%', fontsize=16, xy=(0, 0.25), xytext=(0, 0.25))
    plt.annotate('23%', fontsize=16, xy=(0.90, 0.15), xytext=(0.9, 0.15))
    plt.annotate('9%', fontsize=16, xy=(1.95, 0.045), xytext=(1.95, 0.045))
    st.pyplot(fig)
    st.markdown('Pada bulan Januari 2015 penjuan tertinggi pada kategori barang Office Supplies atau peralatan kantor dengan rataan diskon 9% per barang, tetapi rataan diskon terbesar pada kategori teknologi dengan rataan diskon mencapai 35%')
    st.markdown('###### Analisis Korelasi')
    st.markdown('Pada analisis sebelumnya adanya fakta bahwa keuntungan pada bulan Januari 2015 mengalami kerugian dengan diikuti bahwa penjualan tertinggi pada kategori peralatan kantor dan penjualan terendah pada teknologi sebaliknya rataan diskon tertinggi pada kategori teknologi akan diselidiki apakah faktor diskon mempengaruhi hasil laba yang didapat dengan analisis korelasi. analisis korelasi merupakan metode statistik untuk mengetahui adanya hubungan dari dua variabel dengan rentang nilai korelasi antara (-1,1) dimana nilai mendekati 0 artinya korelasi lemah atau tidak ada hubungan dan mendekati -1 dan 1 korelasi kuat.')
    fig = plt.figure(figsize=(10,5))
    dp = pd.read_csv('data/discpro.csv')
    corr = plt.scatter(dp['profit'],dp['discount'], color='c')
    plt.plot(np.linspace(-4000, 4000),
    np.linspace(0.8, 0), ':r')
    plt.title('Keuntungan Vs Discount')
    st.pyplot(fig)
    st.markdown('Dari grafik scatter plot terbentuk suatu pola dengan kemiringan negatif yang artinya adanya korelasi negatif dari variabel diskon dan laba, untuk lebih tepatnya akan kita hitung berapa nilai korelasi dibawah ini.')
    r = np.corrcoef(dp['profit'],dp['discount'])
    r
    st.markdown('Didapatkan nilai korelasi antara variabel laba dan diskon yaitu -0,2195 artinya meski nilai termasuk dalam korelasi lemah tetapi mengidikasi bahwa adanya hubungan negatif dari kedua variabel laba dan diskon.')

        
elif choose == "Conclusion":
    st.title('Simpulan')
    st.markdown('1. Hasil laporan penjualan perusahaan ritel superstore didapat nilai penjualan atau transaksi mencapai 2.3 juta USD, dengan total laba mencapai 286,397 USD dengan rataan diskon 15.6%, dengan produk terlaris adalah Logitech P710e Mobile Speakerphone.')
    st.markdown('2. Hasil transaksi penjualan tertinggi pada bulan November 2017 mencapai 118,448 USD dan penjualan terendah Februari 2014 dengan nilai transaksi 4,519 USD.')
    st.markdown('3. Hasil laba dari penjualan tertinggi pada bulan Desember 2016 mencapai 17,885 USD dan laba dari penjualan terendah Januari 2015 dengan nilai laba penjualan -3,281 USD (rugi).')
    st.markdown('4. Kategori barang yang menyumbang keuntungan terbesar adalah dari kategori Technology dan kategori Office Supplies.')
    st.markdown('5. Pada bulan Januari 2015 penjuan tertinggi pada kategori barang Office Supplies atau peralatan kantor dengan rataan diskon 9% per barang dan penjualan sebanyak 110 unit, tetapi rataan diskon terbesar pada kategori teknologi dengan rataan diskon mencapai 35%, dengan penjualan sebanyak 38 unit.')
    st.markdown('6. Dari analisis korelasi antara laba dan diskon didapakan nilai korelasi sebesar -0.2195 yang artinya adanya korelasi negatif dari variabel diskon dan laba sebagai salah satu penyebab kerugian pada bulan Januari 2015.')

elif choose == "Contact Me":
    st.markdown('##### Email')
    st.markdown('candravakris@gmail.com')
    st.markdown('##### Instagram')
    st.markdown('@vakris.candra')
    st.markdown('##### Linkedin')
    st.markdown('https://www.linkedin.com/in/vakris-candra-sasmita-590596136')
