import streamlit as st
import random
import datetime

st.set_page_config(page_title="Emergency Kit ⚠️", layout="centered")
st.title("🚨 EMERGENCY REMINDER KIT 🚨")

# Motivational quotes
quotes = [
    "Ingat kenapa kamu mulai. 💪",
    "Allah gak tidur, semua prosesmu dilihat. ✨",
    "Kamu pantas jadi versi terbaikmu. 💥",
    "Istiqomah itu capek, tapi hasilnya manis. 🍯",
    "Kalau kamu gak nyerah, kamu menang. 🚀",
    "Bangkit, bestie! Hidupmu mahal. 💎",
    "Relapse itu bukan takdir, itu keputusan. Kamu bisa nolak. 🛑"
]

# Reminder
st.subheader("📣 Kamu Lagi Kuat Banget Lho!")
st.write("Kalau kamu buka halaman ini, berarti kamu masih punya kontrol. Jangan nyerah, Bestie. 🥺✨")

# Tombol dapetin motivasi
if st.button("🎯 Kasih Aku Motivasi!"):
    st.success(random.choice(quotes))

# Kolom curhat
st.subheader("✏️ Curhat Dikit, Yuk")
user_input = st.text_area("Lagi ngerasa apa? Tulis aja di sini, ini buat kamu sendiri 💖")

if user_input:
    st.info("Kadang nulis aja bisa bikin lega. Kamu hebat udah nyoba. ✨")

# Checklist aksi pengalihan
st.subheader("🛡️ Pengalihan Darurat")
st.markdown("""
✅ Minum air putih  
✅ Ganti posisi (berdiri / jalan sebentar)  
✅ Cuci muka atau mandi  
✅ Lihat goal tracker kamu  
✅ Ingat alasan kamu mulai  
✅ Baca 1 paragraf Qur’an atau dzikir  
✅ Tulis rencana besok  
✅ Panggil teman atau distract dengan coding!
""")

# Catatan akhir
st.warning("💡 Jangan biarkan 10 menit impuls menghancurkan progres 10 hari. Stay strong, Besty! Kamu gak sendiri 💖")
