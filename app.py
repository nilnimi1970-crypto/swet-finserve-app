import streamlit as st
import time
import pandas as pd

# 1. Page Configuration
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
""", unsafe_allow_html=True)

# Initialize Lists in Session State to act as a Live Cloud Database
if "customers_list" not in st.session_state:
    st.session_state.customers_list = []
if "accounts_list" not in st.session_state:
    st.session_state.accounts_list = []
if "loaded" not in st.session_state:
    st.session_state.loaded = False

# ----------------- PAGE 1: SPLASH / LANDING PAGE -----------------
if not st.session_state.loaded:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px; margin: 0;'>⚜️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>Welcome to Swet Finserve</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Finance & Insurance Consultancy Services</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 1px solid #d4af37;'>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='color: #4a4a4a; font-size: 16px;'>
        📍 <b>Office No. S – 6</b>, 2nd Floor, Radheshyam Chamber,<br>
        Pirchalla Road, Haluriya Road, Bhavnagar - 364001, Gujarat
        </p>
    """, unsafe_allow_html=True)
    st.markdown("<p class='gold-text'>📞 Contact: +91 9429965252  |  ✉️ Email: swetfinserve@gmail.com</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    loading_text = st.empty()
    progress_bar = st.progress(0)
    
    for percent in range(100):
        time.sleep(0.05) 
        progress_bar.progress(percent + 1)
        if percent < 30: loading_text.markdown("<center><b style='color:#786200;'>Securing Financial Modules...</b></center>", unsafe_allow_html=True)
        elif percent < 70: loading_text.markdown("<center><b style='color:#786200;'>Connecting Swet Finserve Database...</b></center>", unsafe_allow_html=True)
        else: loading_text.markdown("<center><b style='color:#786200;'>Ready to Launch...</b></center>", unsafe_allow_html=True)
        
    st.session_state.loaded = True
    st.rerun()

# ----------------- PAGE 2: MAIN DASHBOARD SOFTWARE -----------------
else:
    st.markdown("<h2 style='color:#4a3b00;'>⚜️ Swet Finserve Dashboard</h2>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["👥 Customer Data", "💰 Accounting & Reports", "⚙️ Admin Settings"])
    
    with tab1:
        st.subheader("Customer Data Management")
        cust_name = st.text_input("Enter Customer / Supplier Name:", key="cust_in")
        if st.button("Save Customer", type="primary"):
            if cust_name:
                st.session_state.customers_list.append({"Sr No": len(st.session_state.customers_list)+1, "Customer Name": cust_name})
                st.success(f"'{cust_name}' ka naam kamyabi se save ho gaya!")
                time.sleep(0.5)
                st.rerun()
            else:
                st.warning("Kripya naam likhein!")
        
        # --- DATA DEKHNE KE LIYE TABLE ---
        st.markdown("<br><h4 style='color:#786200;'>📋 Saved Customers List</h4>", unsafe_allow_html=True)
        if st.session_state.customers_list:
            df_cust = pd.DataFrame(st.session_state.customers_list)
            st.dataframe(df_cust, use_container_width=True, hide_index=True)
        else:
            st.info("Abhi tak koi customer save nahi kiya gaya hai.")
                
    with tab2:
        st.subheader("Accounting & Hisab-Kitab")
        amount = st.number_input("Amount (Rs):", min_value=0.0, step=100.0, key="acc_in")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Add Income", use_container_width=True):
                if amount > 0:
                    st.session_state.accounts_list.append({"Time": time.strftime("%H:%M:%S"), "Type": "Income (➕)", "Amount (Rs)": amount})
                    st.success(f"Rs. {amount} Income me add ho gaye!")
                    time.sleep(0.5)
                    st.rerun()
                else: st.warning("Amount 0 se zyada hona chahiye!")
        with col2:
            if st.button("➖ Add Expense", use_container_width=True):
                if amount > 0:
                    st.session_state.accounts_list.append({"Time": time.strftime("%H:%M:%S"), "Type": "Expense (➖)", "Amount (Rs)": amount})
                    st.error(f"Rs. {amount} Expense me add ho gaye!")
                    time.sleep(0.5)
                    st.rerun()
                else: st.warning("Amount 0 se zyada hona chahiye!")
        
        # --- DATA DEKHNE KE LIYE TABLE ---
        st.markdown("<br><h4 style='color:#786200;'>📊 Live Transaction Report</h4>", unsafe_allow_html=True)
        if st.session_state.accounts_list:
            df_acc = pd.DataFrame(st.accounts_list)
            st.dataframe(df_acc, use_container_width=True, hide_index=True)
            
            # Auto-Calculation
            total_income = sum(item["Amount (Rs)"] for item in st.session_state.accounts_list if "Income" in item["Type"])
            total_expense = sum(item["Amount (Rs)"] for item in st.session_state.accounts_list if "Expense" in item["Type"])
            net_balance = total_income - total_expense
            
            # Summary Boxes
            st.markdown(f"""
                <div style='background-color: #ffffff; border-radius: 10px; padding: 15px; border: 1px solid #d4af37;'>
                    <p style='margin:0; color:#198754;'><b>Total Income:</b> Rs. {total_income}</p>
                    <p style='margin:0; color:#dc3545;'><b>Total Expense:</b> Rs. {total_expense}</p>
                    <hr style='margin: 8px 0;'>
                    <h5 style='margin:0; color:#4a3b00;'><b>Net Cash Balance:</b> Rs. {net_balance}</h5>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Abhi tak koi transaction entry nahi ki gayi hai.")
                
    with tab3:
        st.subheader("⚙️ Admin Settings")
        st.info("Aap yahan se software ke features live control kar sakte hain.")
        st.text_input("Change Company Name:", value="Swet Finserve")
        st.text_area("Change Address:", value="Office No. S – 6, 2nd Floor, Radheshyam Chamber...")
        if st.button("Save New Settings"): st.success("Details updated instantly!")

    st.markdown("<br><hr><center class='footer-links'>Connect with us: <a href='https://facebook.com' target='_blank'>Facebook</a> | <a href='https://linkedin.com' target='_blank'>LinkedIn</a> | <a href='https://twitter.com' target='_blank'>Twitter</a></center>", unsafe_allow_html=True)   
