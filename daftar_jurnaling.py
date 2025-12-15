import streamlit as st
import csv
import os

FILE = "rencana.csv"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    return []

def save_data(data):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def rekap_page():
    st.title("📝 Daftar Jurnaling")
    st.write("Lihat semua rencana yang sudah kamu buat. Ada yang selesai, ada yang masih—wacana.")

    data = load_data()

    if data:
        selesai_count = 0
        ongoing_count = 0
        belum_count = 0

        for row in data:
            if row:
                if len(row) == 2:
                    status = "Belum Dimulai"
                else:
                    status = row[2]

                if status == "Selesai":
                    selesai_count += 1
                elif status == "Ongoing":
                    ongoing_count += 1
                else:
                    belum_count += 1

        st.markdown(
            f"""
            <div style="
                background-color:;
                padding:15px;
                margin-bottom:20px;
                border-radius:8px;
                border:1px solid #f5f5f5;">
                <h4 style="color:; margin:0; font-weight:bold;">Ringkasan Status</h4>
                <p style="color:rgb(46, 125, 50); font-weight:bold;">✅ Selesai: {selesai_count}</p>
                <p style="color:rgb(204, 153, 0); font-weight:bold;">🔄 Ongoing: {ongoing_count}</p>
                <p style="color:rgb(198, 40, 40); font-weight:bold;">⏳ Belum Dimulai: {belum_count}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Ayo wujudkan Rencana Anda 💪😘")
        updated = False
        for i, row in enumerate(data):
            if row:
                if len(row) == 2:
                    bulan, rencana = row
                    status = "Belum Dimulai"
                else:
                    bulan, rencana, status = row

                new_status = st.selectbox(
                    f"Status untuk '{rencana}'",
                    ["Belum Dimulai", "Ongoing", "Selesai"],
                    index=["Belum Dimulai", "Ongoing", "Selesai"].index(status),
                    key=f"status_{i}"
                )

                if new_status != status:
                    data[i] = [bulan, rencana, new_status]
                    updated = True

                if new_status == "Selesai":
                    bg_color = "rgb(46, 125, 50)"
                    text_color = "rgb(200, 255, 200)"
                    text_shadow = "1px 1px 2px #000"
                elif new_status == "Ongoing":
                    bg_color = "rgb(204, 153, 0)"
                    text_color = "rgb(255, 255, 200)"
                    text_shadow = "1px 1px 2px #000"
                else:
                    bg_color = " rgb(198, 40, 40)"   
                    text_color = "rgb(255, 200, 200)"
                    text_shadow = "1px 1px 2px #000"            


                st.markdown(
                    f"""
                    <div style="
                        background-color:{bg_color};
                        padding:15px;
                        margin-bottom:10px;
                        border-radius:8px;
                        border:1px solid #444;">
                        <h4 style="color:{text_color}; text-shadow:{text_shadow};margin:0; font-weight:bold;">{bulan}</h4>
                        <p style="color:{text_color}; text-shadow:{text_shadow}; font-weight:bold; font-size:18px; margin:0;">{rencana}</p>
                        <small style="color:{text_color}; text-shadow:{text_shadow};">Status: {new_status}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    if updated:
        save_data(data)
        st.success("Status berhasil diperbarui!")
    else:
        st.info("Belum ada tujuan yang tersimpan.")
