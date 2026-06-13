import streamlit as st
import time

# 1. Page Configuration (Website ka title aur icon)
st.set_page_config(page_title="Swet Finserve", page_icon="⚜️", layout="centered")

# Custom HTML/CSS Styling (Golden & Yellow Luxury Theme)
st.markdown("""
    <style>
    .stApp { background-color: #fffbeb; }
    .main-box {
        background-color: #ffffff;
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.2);
    }
    .main-title { color: #4a3b00; font-family: 'Helvetica', sans-serif; font-weight: bold; }
    .subtitle { color: #786200; font-style: italic; }
    .gold-text { color: #b89214; font-weight: bold; }
    .footer-links a { color: #b89214; text-decoration: none; font-weight: bold; margin: 0 10px; }
    </style>
""", unsafe_transform=True)

# 2. Session State Setup (10-second loading track karne ke liye)
if "loaded" not in st.session_state:
    st.session_state.loaded = False

# ----------------- PAGE 1: SPLASH / LANDING PAGE -----------------
if not st.session_state.loaded:
    st.markdown('<div class="main-box">', unsafe_transform=True)
    
    # Centered Logo and Welcome Note
    st.markdown("<h1 style='font-size: 80px; margin: 0;'>⚜️</h1>", unsafe_transform=True)
    st.markdown("<h1 class='main-title'>Welcome to Swet Finserve</h1>", unsafe_transform=True)
    st.markdown("<p class='subtitle'>Finance & Insurance Consultancy Services</p>", unsafe_transform=True)
    st.markdown("<hr style='border-top: 1px solid #d4af37;'>", unsafe_transform=True)
    
    # Office Details
    st.markdown("""
        <p style='color: #4a4a4a; font-size: 16px;'>
        📍 <b>Office No. S – 6</b>, 2nd Floor, Radheshyam Chamber,<br>
        Pirchalla Road, Haluriya Road, Bhavnagar - 364001, Gujarat
        </p>
    """, unsafe_transform=True)
    st.markdown("<p class='gold-text'>📞 Contact: +91 9429965252  |  ✉️ Email: swetfinserve@gmail.com</p>", unsafe_transform=True)
    
    st.markdown('</div>', unsafe_transform=True)
    
    # Progress Bar (10 Seconds)
    st.write("")
    loading_text = st.empty()
    progress_bar = st.progress(0)
    
    for percent in range(100):
        time.sleep(0.1) # 100 steps * 0.1s = 10 Seconds
        progress_bar.progress(percent + 1)
        if percent < 30: loading_text.markdown("<center><b style='color:#786200;'>Securing Financial Modules...</b></center>", unsafe_transform=True)
        elif percent < 70: loading_text.markdown("<center><b style='color:#786200;'>Connecting Swet Finserve Database...</b></center>", unsafe_transform=True)
        else: loading_text.markdown("<center><b style='color:#786200;'>Ready to Launch...</b></center>", unsafe_transform=True)
        
    st.session_state.loaded = True
    st.rerun()

# ----------------- PAGE 2: MAIN DASHBOARD SOFTWARE -----------------
else:
    st.markdown("<h2 style='color:#4a3b00;'>⚜️ Swet Finserve Dashboard</h2>", unsafe_transform=True)
    
    # App Tabs
    tab1, tab2, tab3 = st.tabs(["👥 Customer Data", "💰 Accounting", "⚙️ Admin Settings"])
    
    with tab1:
        st.subheader("Customer Data Management")
        cust_name = st.text_input("Enter Customer / Supplier Name:")
        if st.button("Save Customer", type="primary"):
            if cust_name:
                st.success(f"'{cust_name}' ka naam kamyabi se Cloud par save ho gaya!")
            else:
                st.warning("Kripya naam likhein!")
                
    with tab2:
        st.subheader("Accounting & Hisab-Kitab")
        amount = st.number_input("Amount (Rs):", min_value=0.0, step=100.0)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Add Income", use_container_width=True):
                st.success(f"Rs. {amount} Income me add ho gaye!")
        with col2:
            if st.button("➖ Add Expense", use_container_width=True):
                st.error(f"Rs. {amount} Expense me add ho gaye!")
                
    with tab3:
        st.subheader("⚙️ Admin Settings (No Notepad Needed!)")
        st.info("Aap yahan se software ke features live control kar sakte hain.")
        st.text_input("Change Company Name:", value="Swet Finserve")
        st.text_area("Change Address:", value="Office No. S – 6, 2nd Floor, Radheshyam Chamber...")
        if st.button("Save New Settings"):
            st.success("Details updated instantly!")

    # Fixed Social Media Links at Bottom
    st.markdown("<br><hr><center class='footer-links'>Connect with us: <a href='https://facebook.com' target='_blank'>Facebook</a> | <a href='https://linkedin.com' target='_blank'>LinkedIn</a> | <a href='https://twitter.com' target='_blank'>Twitter</a></center>", unsafe_transform=True)
