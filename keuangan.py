import streamlit as st
import csv, os

filename = "keuangan.csv"

# Tambahkan fungsi ini
def load_keuangan():
    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            return reader[1:] if len(reader) > 1 else []  # skip header
    return []

def keuangan_page():
    st.title("💰 Catatan Keuangan Pribadi")
    st.write("Masukkan pemasukan dan pengeluaran. Jangan sampai saldo cuma tinggal harapan.")

    if os.path.exists(filename):
        with open(filename, "r", newline="") as f:
            reader = list(csv.reader(f))
        if len(reader) > 1:
            saldo_awal = int(reader[-1][3])
        else:
            saldo_awal = 0
    else:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Tanggal","pemasukan","pengeluaran","saldo"])
        saldo_awal = 0

    def saldobaru(saldo_awal, a, b):
        return saldo_awal + a - b

    Tanggal = st.date_input("Masukan Tanggal")
    pemasukan = st.number_input("Masukkan pemasukan (Rp)", min_value=0, step=10000)
    pengeluaran = st.number_input("Masukkan pengeluaran (Rp)", min_value=0, step=10000)

    if st.button("Simpan Catatan"):
        saldo_baru = saldobaru(saldo_awal, pemasukan, pengeluaran)
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([Tanggal, pemasukan, pengeluaran, saldo_baru])
        st.success(f"Catatan berhasil disimpan! Saldo sekarang: Rp {saldo_baru:,.0f}")

    if os.path.exists(filename):
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            st.write("### 📋 Hasil Keuangan")
            st.table(data)
