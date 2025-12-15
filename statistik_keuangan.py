import streamlit as st
import csv
import os

def finance_stats():
    st.title("📈 Statistik Keuangan")

    filename = "keuangan.csv"

    if not os.path.exists(filename):
        st.warning("Belum ada data keuangan.")
        return

    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    title = data[0]
    rows = data[1:]

    if not rows:
        st.warning("Data masih kosong.")
        return

    Tanggal = [(row[0],) for row in rows]
    pemasukan = [int(row[1]) for row in rows]
    pengeluaran = [int(row[2]) for row in rows]
    saldo = [int(row[3]) for row in rows]

    total_pemasukan = sum(pemasukan)
    total_pengeluaran = sum(pengeluaran)
    saldo_rata = sum(saldo) / len(saldo)
    saldo_akhir = saldo[-1]

    
    st.write(f"**Total Pemasukan:** Rp {total_pemasukan:,.0f}")
    st.write(f"**Total Pengeluaran:** Rp {total_pengeluaran:,.0f}")
    st.write(f"**Saldo Rata-rata:** Rp {saldo_rata:,.0f}")
    st.write(f"**Saldo Akhir:** Rp {saldo_akhir:,.0f}")

    Data_Chart = {
        "Tanggal": Tanggal,
        "Pemasukan": pemasukan,
        "Pengeluaran": pengeluaran,
        "Saldo": saldo
    }
    st.subheader("Grafik Keuangan")
    st.line_chart(Data_Chart, x="Tanggal", y="Saldo")