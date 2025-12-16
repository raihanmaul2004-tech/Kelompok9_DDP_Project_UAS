import streamlit as st

def kontak_page():
    st.title("📞 Kontak Kelompok")

    # Data anggota kelompok
    anggota = [
        {
            "nama": "Muhammad Raihan Maulana",
            "nim" : "0110125052",
            "ig": "https://www.instagram.com/mraihnm/",
            "wa": "https://wa.me/6285882077754"
        },
        {
            "nama": "Muhammad Zidni Fadhilah",
            "nim" : "0110125007",
            "ig": "https://www.instagram.com/zidni_fadh?igsh=MWNlazczZWVxZHMxaQ==",
            "wa": "https://wa.me/6281808296075"
        },
        {
            "nama": "Putri Ramadhani Silitonga",
            "nim" : "0110125007",
            "ig": "https://www.instagram.com/_putrisltg?igsh=bWFtZ2szeHduNjc3",
            "wa": "https://wa.me/6285261497438"
        },
        {
            "nama": "Ayu Dia Isnani Arun Nisa",
            "nim" : "0110125007",
            "ig": "https://instagram.com/username4",
            "wa": "https://wa.me/6285714715122"
        },
    ]

    col = st.columns(1)[0]
    a = anggota[0]
    with col:
        st.markdown(
            f"""
            <div style="
                border:2px solid #f5f5f5;
                border-radius:10px;
                padding:15px;
                margin-bottom:15px;
                text-align:center;
                background-color:;
                word-wrap:break-word;">
                <h4 style="color:; margin:5px 0;text-shadow: 1px 1px 2px #000;">{a['nama']}</h4>
                <p>
                    <a href="{a['ig']}" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" style="margin:0 10px;">
                    </a>
                    <a href="{a['wa']}" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30" style="margin:0 10px;">
                    </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- Barisan kedua: 3 card ---
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for idx, a in enumerate(anggota[1:]):  # ambil anggota ke-2 sampai ke-4
        with cols[idx]:
            st.markdown(
                f"""
                <div style="
                    border:2px solid #f5f5f5;
                    border-radius:10px;
                    padding:15px;
                    margin-bottom:15px;
                    text-align:center;
                    background-color:;
                    display:inline-block;
                    word-wrap:break-word;">
                    <h4 style="color:; margin:5px 0;text-shadow: 1px 1px 2px #000;">{a['nama']}</h4>
                    <p>
                        <a href="{a['ig']}" target="_blank">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" style="margin:0 10px;">
                        </a>
                        <a href="{a['wa']}" target="_blank">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30" style="margin:0 10px;">
                        </a>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div style="background-color:#162d6a; padding:15px; border-radius:8px; text-align:center;">
            <h4 style="color:#f5f5f5; font-style:italic;text-shadow: 1px 1px 2px #000;">"Follow dan chat aja, nggak usah malu nggak gigit kok 💪😘"</h4>
        </div>
        """,
        unsafe_allow_html=True
    )