import streamlit as st
import datetime
import json
from pathlib import Path
import random

# CONFIG
DATA_FILE = Path("nofap_data.json")
DAYS_PER_CYCLE = 4

# ====== INIT FUNCTION ======
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "log": [],
            "cycles": [],
            "current_cycle": {
                "id": 1,
                "start_date": datetime.date.today().isoformat(),
                "days": []
            }
        }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ====== LOAD STATE & INIT SESSION ======
data = load_data()
today = datetime.date.today().isoformat()
today_date = datetime.date.today()
today_entry = next((entry for entry in data["log"] if entry["date"] == today), None)

if 'last_reward_day' not in st.session_state:
    st.session_state['last_reward_day'] = today_date

if 'used_rewards' not in st.session_state:
    st.session_state['used_rewards'] = []

# ====== UI CONFIG ======
st.set_page_config(page_title="Challenge 4Days Tracker", layout="centered")
st.title("🔥🔥 Future Fighter ❤️‍🔥❤️‍🔥")
st.markdown("Start from 4 Days, Realistic and Consistency")

# ====== DAILY TRACKER ======
if today_entry is None:
    status = st.radio("Today Status:", ["🟩 Clean", "🟥 Relapse"])
    note = st.text_input("Notes:")

    if status and st.button("Save Today Progress"):
        log_entry = {"date": today, "status": status, "note": note}
        data["log"].append(log_entry)
        data["current_cycle"]["days"].append(log_entry)

        if status == "🟥 Relapse":
            data["cycles"].append(data["current_cycle"])
            data["current_cycle"] = {
                "id": data["current_cycle"]["id"] + 1,
                "start_date": today,
                "days": []
            }

        elif status == "🟩 Clean":
            if len(data["current_cycle"]["days"]) == DAYS_PER_CYCLE:
                st.balloons()
                st.success(f"KAMU BERHASIL MENYELESAIKAN {DAYS_PER_CYCLE} Hari clean!")
                data["cycles"].append(data["current_cycle"])
                data["current_cycle"] = {
                    "id": data["current_cycle"]["id"] + 1,
                    "start_date": today,
                    "days": []
                }

        save_data(data)
        st.success("Today's Step is Done ✅")
        st.rerun()
else:
    st.success(f"Hari ini kamu sudah ngisi: {today_entry['status']}")
    if today_entry['note']:
        st.info(f"📝 Catatan: {today_entry['note']}")

# ====== DAILY LOG ======
st.subheader("🗓️ Daily Log")
for entry in reversed(data["log"][-10:]):
    st.write(f"{entry['date']} - {entry['status']} {'📝 ' + entry['note'] if entry['note'] else ''}")

# ====== STREAK ======
# ====== STREAK & STATS ======
st.subheader("📈 Progress")

# Hitung streak clean berturut-turut dari hari terakhir
clean_streak = 0
for entry in reversed(data["log"]):
    if entry['status'] == "🟩 Clean":
        clean_streak += 1
    else:
        break

# Total statistik
total_clean = sum(1 for entry in data["log"] if entry["status"] == "🟩 Clean")
total_relapse = sum(1 for entry in data["log"] if entry["status"] == "🟥 Relapse")

# Tampilkan metrik
#st.metric("Hari Clean Berturut-turut", clean_streak)
st.metric("Total Clean Days", total_clean)
st.metric("Jumlah Relapse", total_relapse)
#st.metric("Cycle yang telah diselesaikan", len(data["cycles"]))


# ====== DETAIL CYCLE ======
# ===== st.subheader("📅 Detail Cycle")
#for cycle in reversed(data["cycles"][-5:] + [data["current_cycle"]]): 
    #start = datetime.date.fromisoformat(cycle["start_date"])
    #age_days = (today_date - start).days
    #label = "🔥 Masih Aktif"

    #if len(cycle["days"]) == 0:
    #    continue
   # elif len(cycle["days"]) == DAYS_PER_CYCLE:
  #      label = "✅ Sukses"
 #   elif age_days > 30:
#        label = "🕒 Sudah Lewat 1 Bulan"

    #st.markdown(f"**Cycle #{cycle['id']}** - {len(cycle['days'])} hari - *{label}*")
    #for entry in cycle["days"]:
       # st.write(f"{entry['date']} - {entry['status']} {'📝 ' + entry['note'] if entry['note'] else ''}")

# ====== MOTIVASI ======
motivasi = [
    "Satu hari clean lebih kuat dari 1000 niat tanpa aksi.",
    "Kalau kamu bisa 1 hari, kamu bisa 4 hari.",
    "Relapse bukan gagal, cuma jalan muter.",
    "Jangan dengarkan bisikan 'sekali ini aja'. Itu jebakan.",
    "Tubuhmu butuh istirahat dari dopamin palsu."
]
st.info(f"💬 Motivasi hari ini: *{random.choice(motivasi)}*")

# ====== REWARD SYSTEM ======
st.subheader("🎁 REWARD UNLOCK 🎁")
reward_list = [
    "Mie Ayam 🍜",
    "Bakso Simpangan 🍲",
    "Nasi Padang 🍛",
    "Sate Padang 🍢",
    "Ayam Bakar 🍗",
    "Menu Special Warsun 🍽️",
    "Ketoprak 🥗",
    "Jajanan 2 item di Graha 🍡🍘",
    "Bakso Cuanki 🍥",
    "Pentol & Gorengan/Cimol 🧆🥟",
    "Seblak Pedas Nampol 🔥🍲"
]

days_since = (today_date - st.session_state['last_reward_day']).days

if days_since >= 4:
    available_rewards = [r for r in reward_list if r not in st.session_state['used_rewards']]
    if not available_rewards:
        st.session_state['used_rewards'] = []
        available_rewards = reward_list.copy()

    reward = random.choice(available_rewards)
    st.session_state['used_rewards'].append(reward)

    st.balloons()
    st.success(f"🎉 SELAMAT! Kamu unlock reward hari ini: **{reward}**")
    st.session_state['last_reward_day'] = today_date
else:
    st.info(f"Reward berikutnya bisa kamu buka dalam **{4 - days_since}** hari lagi ✨")
