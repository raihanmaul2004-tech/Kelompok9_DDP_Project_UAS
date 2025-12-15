import streamlit as st
from keuangan import keuangan_page
from statistik_keuangan import finance_stats
from home import home_page
from jurnaling import tujuan_page
from daftar_jurnaling import rekap_page
from kontak import kontak_page

custom_css = """
<style>
<style>
/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #f5f5f5;
    border-right: 1px solid #dcdcdc;
}

/* Sidebar teks */
[data-testid="stSidebar"] .css-1d391kg {
    color: #333333;
    font-weight: 500;
}

/* Sidebar item aktif */
[data-testid="stSidebar"] .css-1d391kg:hover {
    background-color: #e0e0e0;
    color: #1e3a8a;
}

/* Tombol utama */
.stButton>button {
    background-color: #1e3a8a;
    color: #f5f5f5;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 16px;
    text-shadow: 1px 1px 2px #000;
}

/* Hover tombol */
.stButton>button:hover {
    background-color: #162d6a;
    color: #f5f5f5;
    text-shadow: 1px 1px 2px #000;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

menu=st.sidebar.radio("Menu",["🏠 Home","➕ Tambah Jurnaling","📝 Daftar Jurnaling","💰 Catatan Keuangan","📈 Statistik Keuangan","📞 Kontak Kami"])

if menu=="💰 Catatan Keuangan":
    keuangan_page()
elif menu=="📈 Statistik Keuangan":
    finance_stats()
elif menu=="🏠 Home":
    home_page()
elif menu=="➕ Tambah Jurnaling":
    tujuan_page()
elif menu=="📝 Daftar Jurnaling":
    rekap_page()
elif menu=="📞 Kontak Kami":
    kontak_page()