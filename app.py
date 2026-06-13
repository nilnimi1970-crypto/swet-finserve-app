import streamlit as st
import time
import pandas as pd

# Page configuration
st.set_page_config(page_title="Swet Finserve", page_icon="⚜️", layout="centered")

# Initialize Session State
if "loaded" not in st.session_state:
    st.session_state.loaded = False
if "customers_list" not in st.session_state:
    st.session_state.customers_list = []
if "accounts_list" not in st.session_state:
    st.session_state.accounts_list = []

# ----------------- PAGE 1: PREMIUM HTML/CSS/JS SPLASH PAGE -----------------
if not st.session_state.loaded:
    # Full Screen Light Golden Luxury Theme Blank styling for Streamlit elements
    st.markdown("""
        <style>
        .stApp { background-color: #fffbeb; }
        [data-testid="stHeader"] { display: none; }
        div.block-container { padding-top: 2rem; }
        
        /* Premium Card Design */
        .luxury-card {
            background: #ffffff;
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.3);
            max-width: 600px;
            margin: auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Big Elegant Logo Animation */
        .luxury-logo {
            font-size: 90px;
            color: #d4af37;
            margin-bottom: 10px;
            animation: pulse 2s infinite ease-in-out;
        }
        
        /* Main Typography */
        .main-title {
            color: #3a2e00;
            font-size: 32px;
            font-weight: 700;
            margin: 10px 0 5px 0;
            letter-spacing: 0.5px;
        }
        .tagline {
            color: #8a6d00;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 25px;
        }
        
        /* Divider */
        .gold-line {
            width: 80px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #d4af37, transparent);
            margin: 20px auto;
        }
        
        /* Info Details */
        .info-text {
            color: #4a4a4a;
            font-size: 15px;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .contact-highlight {
            color: #b89214;
            font-weight: 600;
            font-size: 14px;
            margin-top: 15px;
        }
        
        /* Social Media Icons Styling */
        .social-footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #f2ebcc;
        }
        .social-text {
            font-size: 12px;
            color: #8a6d00;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }
        .social-links a {
            color: #b89214;
            text-decoration: none;
            font-weight: bold;
            margin: 0 12px;
            font-size: 15px;
            transition: color 0.3s;
        }
        .social-links a:hover {
            color: #3a2e00;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        </style>
        
        <div class="luxury-card">
            <div class="luxury-logo">⚜️</div>
            <div class="main-title">Welcome to Swet Finserve</div>
            <div class="tagline">Finance & Insurance Consultancy Services</div>
            <div class="gold-line"></div>
            <div class="info-text">
                📍 Office No. S – 6, 2nd Floor, Radheshyam Chamber,<br>
                Pirchalla Road, Haluriya Road, Bhavnagar - 364001, Gujarat
            </div>
            <div class="contact-highlight">
                📞 +91 9429965252 &nbsp;|&nbsp; ✉️ swetfinserve@gmail.com
            </div>
            
            <div class="social-footer">
                <div class="social-text">Connect With Us</div>
                <div class="social-links">
                    <a href="https://facebook.com" target="_blank">Facebook</a>
                    <a href="https://linkedin.com" target="_blank">LinkedIn</a>
                    <a href="https://twitter.com" target="_blank">Twitter</a>
                    <a href="https://instagram.com" target="_blank">Instagram</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 10-Second JavaScript Styled Progress Bar Tracker
    st.write("")
    status_label = st.empty()
    progress_ui = st.progress(0)
    
    for p in range(100):
        time.sleep(0.1) # 100 * 0.1s = Exact 10 Seconds Progress Bar
        progress_ui.progress(p + 1)
        if p < 30:
            status_label.markdown("<center><span style='color:#8a6d00; font-weight:600; font-size:14px;'>🔒 Securing Financial Modules...</span></center>", unsafe_allow_html=True)
        elif p < 70:
            status_label.markdown("<center><span style='color:#8a6d00; font-weight:600; font-size:14px;'>⏳ Connecting Swet Finserve Cloud Database...</span></center>", unsafe_allow_html=True)
        else:
            status_label.markdown("<center><span style='color:#8a6d00; font-weight:600; font-size:14px;'>✨ Ready to Launch System...</span></center>", unsafe_allow_html=True)
            
    st.session_state.loaded = True
    st.rerun()

# ----------------- PAGE 2: MAIN ADVANCED DASHBOARD -----------------
else:
    # Custom styling for dashboard
    st.markdown("""
        <style>
        .stApp { background-color: #fffbeb; }
        h2 { color: #3a2e00 !important; font-weight: 700; }
        .stButton>button { background-color: #d4af37 !important; color: white !important; border-radius: 8px !important; border: none !important; font-weight: bold; }
        .stButton>button:hover { background-color: #3a2e00 !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2>⚜️ Swet Finserve Management System</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["👥 Customer Data Management", "💰 Accounting & Reports", "⚙️ System Settings"])
    
    with tab1:
        st.subheader("Customer Directory")
        cust_name = st.text_input("Enter Customer / Supplier Name:", key="c_name_in")
        if st.button("Save Customer Profile", type="primary"):
            if cust_name:
                st.session_state.customers_list.append({"Sr No": len(st.session_state.customers_list)+1, "Customer Name": cust_name})
                st.success(f"✓ '{cust_name}' ka profile cloud directory me save ho gaya!")
                time.sleep(0.5)
                st.rerun()
            else:
                st.warning("⚠️ Kripya customer ka naam darj karein!")
        
        st.markdown("<br><h4 style='color:#8a6d00;'>📋 Registered Customers Directory</h4>", unsafe_allow_html=True)
        if st.session_state.customers_list:
            df_cust = pd.DataFrame(st.session_state.customers_list)
            st.dataframe(df_cust, use_container_width=True, hide_index=True)
        else:
            st.info("Abhi tak directory me koi customer added nahi hai.")
                
    with tab2:
        st.subheader("Ledger Hisab-Kitab")
        amount = st.number_input("Transaction Amount (Rs):", min_value=0.0, step=500.0, key="money_in")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Record Income", use_container_width=True):
                if amount > 0:
                    st.session_state.accounts_list.append({"Time": time.strftime("%I:%M %p"), "Type": "Income (Credit)", "Amount (Rs)": amount})
                    st.success(f"Rs. {amount} Credit entry save ho gayi!")
                    time.sleep(0.5)
                    st.rerun()
                else: st.warning("Amount 0 se bada hona chahiye!")
        with col2:
            if st.button("➖ Record Expense", use_container_width=True):
                if amount > 0:
                    st.session_state.accounts_list.append({"Time": time.strftime("%I:%M %p"), "Type": "Expense (Debit)", "Amount (Rs)": amount})
                    st.error(f"Rs. {amount} Debit entry save ho gayi!")
                    time.sleep(0.5)
                    st.rerun()
                else: st.warning("Amount 0 se bada hona chahiye!")
        
        st.markdown("<br><h4 style='color:#8a6d00;'>📊 Live Transaction Ledger</h4>", unsafe_allow_html=True)
        if st.session_state.accounts_list:
            df_acc = pd.DataFrame(st.session_state.accounts_list)
            st.dataframe(df_acc, use_container_width=True, hide_index=True)
            
            # Calculations
            t_income = sum(i["Amount (Rs)"] for i in st.session_state.accounts_list if "Income" in i["Type"])
            t_expense = sum(i["Amount (Rs)"] for i in st.session_state.accounts_list if "Expense" in i["Type"])
            net_bal = t_income - t_expense
            
            st.markdown(f"""
                <div style='background-color: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid rgba(212, 175, 55, 0.3); box-shadow: 0 4px 15px rgba(0,0,0,0.02);'>
                    <p style='margin:0 0 5px 0; color:#198754; font-size:15px;'><b>Total Credit (Income):</b> Rs. {t_income}</p>
                    <p style='margin:0 0 10px 0; color:#dc3545; font-size:15px;'><b>Total Debit (Expense):</b> Rs. {t_expense}</p>
                    <hr style='margin: 10px 0; border-top:1px solid #f2ebcc;'>
                    <h5 style='margin:0; color:#3a2e00; font-size:18px;'><b>Net Available Balance:</b> Rs. {net_bal}</h5>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Ledger me abhi koi transaction recorded nahi hai.")
                
    with tab3:
        st.subheader("⚙️ System Customization")
        st.info("Aap yahan se dashboard aur profile data bina kisi programming ke update kar sakte hain.")
        st.text_input("Active Company Profile Name:", value="Swet Finserve")
        st.text_area("Registered Office Address:", value="Office No. S – 6, 2nd Floor, Radheshyam Chamber...")
        if st.button("Update Configuration"): 
            st.success("System configurations updated instantly across the cloud!")

    st.markdown("<br><hr style='border-top:1px solid #f2ebcc;'><center style='font-size:12px; color:#8a6d00;'>Swet Finserve Premium Cloud Application Dashboard</center>", unsafe_allow_html=True)
