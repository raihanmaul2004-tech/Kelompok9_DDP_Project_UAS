import streamlit as st
from daftar_jurnaling import load_data
from keuangan import load_keuangan  

def home_page():
    st.title("🏠 Home")
    st.write("Beranda utama tempat semua rencana dan keuangan kamu bersatu. Santai dulu, tapi tetap produktif.")
    st.markdown("### Progres aktivitas 💪😘 ")

    # --- Ringkasan Aktivitas ---
    data = load_data()
    selesai = sum(1 for r in data if len(r) > 2 and r[2] == "Selesai")
    ongoing = sum(1 for r in data if len(r) > 2 and r[2] == "Ongoing")
    belum   = sum(
        1 for r in data
        if (len(r) == 2) or (len(r) > 2 and r[2] == "Belum Dimulai")
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("✅ Selesai", selesai)
    col2.metric("🔄 Ongoing", ongoing)
    col3.metric("⏳ Belum Dimulai", belum)

    total = selesai + ongoing + belum
    if total > 0:
        st.progress(selesai/total)

    # --- Ringkasan Keuangan ---
    keuangan = load_keuangan()
    if keuangan:
        pemasukan = sum(int(r[1]) for r in keuangan if r[1].isdigit())
        pengeluaran = sum(int(r[2]) for r in keuangan if r[2].isdigit())
        saldo = int(keuangan[-1][3])  # saldo terakhir

        st.markdown("### Ringkasan Keuangan 💰 ")
        col4, col5, col6 = st.columns(3)
        col4.metric("Pemasukan", f"Rp {pemasukan:,}")
        col5.metric("Pengeluaran", f"Rp {pengeluaran:,}")
        col6.metric("Saldo", f"Rp {saldo:,}")

    else:
        st.info("Belum ada catatan keuangan.")

    st.markdown(
        """
        <div style="background-color:#162d6a; padding:15px; border-radius:8px; text-align:center;">
            <h4 style="color:#f5f5f5; font-style:italic;text-shadow: 1px 1px 2px #000;">"Langkah kecil hari ini, hasil besar esok."</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
