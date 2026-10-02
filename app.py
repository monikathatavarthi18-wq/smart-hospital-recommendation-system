import streamlit as st
import pandas as pd
import numpy as np

# ==============================================================================
# SECTION 1: PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="SmartCare | Hospital Recommendation System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# SECTION 2: CUSTOM CSS (HEALTHCARE PORTAL THEME)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Top Navigation Bar */
    .top-navbar {
        background: linear-gradient(135deg, #0A4D68 0%, #088395 100%);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(8, 131, 149, 0.15);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: white !important;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .brand-subtitle {
        font-size: 0.82rem;
        opacity: 0.92;
        margin: 0;
        color: #EBF4F6 !important;
    }

    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #F8FAFC 0%, #EBF4F6 100%);
        border: 1px solid #D6E4E5;
        border-radius: 16px;
        padding: 2.2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 6px 20px rgba(10, 77, 104, 0.04);
    }

    .hero-badge {
        display: inline-block;
        background: #088395;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }

    .hero-heading {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0A4D68;
        line-height: 1.25;
        margin-bottom: 0.5rem;
    }

    .hero-subheading {
        font-size: 1.05rem;
        color: #4A5568;
        max-width: 820px;
        line-height: 1.6;
        margin-bottom: 1.2rem;
    }

    /* Cards */
    .med-card {
        background: white;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        padding: 1.3rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .med-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(8, 131, 149, 0.08);
        border-color: #088395;
    }

    .card-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .badge-primary { background: #E0F2FE; color: #0369A1; }
    .badge-success { background: #DCFCE7; color: #15803D; }
    .badge-warning { background: #FEF3C7; color: #B45309; }

    /* Step Boxes */
    .step-box {
        background: white;
        border-radius: 12px;
        border-left: 4px solid #088395;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        height: 100%;
    }
    .step-number {
        font-size: 1.1rem;
        font-weight: 800;
        color: #088395;
        margin-bottom: 0.3rem;
    }

    /* Result Highlight Card */
    .rec-highlight-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%);
        border: 2px solid #22C55E;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 6px 20px rgba(34, 197, 94, 0.1);
        margin-bottom: 1.5rem;
    }

    /* Scheme & Safety Callouts */
    .scheme-disclaimer {
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        border-radius: 10px;
        padding: 0.9rem 1.2rem;
        font-size: 0.86rem;
        color: #1E40AF;
        margin: 1rem 0;
    }

    .disclaimer-box {
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        border-radius: 10px;
        padding: 1rem;
        font-size: 0.85rem;
        color: #92400E;
        margin-top: 2rem;
    }

    .emergency-banner {
        background: #FEE2E2;
        border-left: 4px solid #EF4444;
        color: #991B1B;
        padding: 0.75rem 1.2rem;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }

    /* Footer */
    .portal-footer {
        background: #0A4D68;
        color: #EBF4F6;
        padding: 2rem 1.5rem 1rem 1.5rem;
        border-radius: 14px;
        margin-top: 3rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# SECTION 3: SESSION STATE INITIALIZATION
# ==============================================================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "enquiries" not in st.session_state:
    st.session_state.enquiries = []

if "search_department" not in st.session_state:
    st.session_state.search_department = "Orthopedics"

if "search_treatment" not in st.session_state:
    st.session_state.search_treatment = "Knee Replacement"

if "search_budget" not in st.session_state:
    st.session_state.search_budget = 80000

if "search_scheme" not in st.session_state:
    st.session_state.search_scheme = "Dr NTR Vaidya Seva / Aarogyasri"

if "search_city" not in st.session_state:
    st.session_state.search_city = "Vijayawada"

# ==============================================================================
# SECTION 4: DATASET LOADING & VALIDATION
# ==============================================================================
@st.cache_data
def load_all_datasets():
    """
    Loads all required project datasets:
    1. hospital_data.csv (Main Kaggle Patient Treatment Dataset)
    2. hospital_master.csv (Demo Hospital Reference Data)
    3. government_schemes.csv (Government Scheme Reference Data)
    4. scheme_treatment_packages.csv (Demo Scheme Treatment Package Data)
    """
    # 1. Main Kaggle Patient Treatment Dataset
    try:
        df_kaggle = pd.read_csv("hospital_data.csv")
        df_kaggle.columns = [c.strip() for c in df_kaggle.columns]
        for c in ["Department", "Treatment Type", "Doctor Name"]:
            df_kaggle[c] = df_kaggle[c].astype(str).str.strip()
        for num_c in ["Treatment Cost", "Hospital Stay (Days)", "Recovery Score", "Age"]:
            df_kaggle[num_c] = pd.to_numeric(df_kaggle[num_c], errors="coerce")
        df_kaggle = df_kaggle.drop_duplicates()
        df_kaggle = df_kaggle.dropna(subset=["Department", "Treatment Type", "Doctor Name", "Treatment Cost", "Recovery Score"])
    except FileNotFoundError:
        return None, None, None, None, "File 'hospital_data.csv' was not found in the project directory."
    except Exception as e:
        return None, None, None, None, f"Error loading 'hospital_data.csv': {str(e)}"

    # 2. Demo Hospital Master Dataset
    try:
        df_hospitals = pd.read_csv("hospital_master.csv")
        df_hospitals.columns = [c.strip() for c in df_hospitals.columns]
        for c in ["Hospital Name", "City", "State", "Hospital Type", "Departments", "Scheme Support"]:
            df_hospitals[c] = df_hospitals[c].astype(str).str.strip()
    except FileNotFoundError:
        return None, None, None, None, "File 'hospital_master.csv' was not found."
    except Exception as e:
        return None, None, None, None, f"Error loading 'hospital_master.csv': {str(e)}"

    # 3. Government Scheme Dataset
    try:
        df_schemes = pd.read_csv("government_schemes.csv")
        df_schemes.columns = [c.strip() for c in df_schemes.columns]
    except FileNotFoundError:
        return None, None, None, None, "File 'government_schemes.csv' was not found."
    except Exception as e:
        return None, None, None, None, f"Error loading 'government_schemes.csv': {str(e)}"

    # 4. Demo Scheme Treatment Package Dataset
    try:
        df_packages = pd.read_csv("scheme_treatment_packages.csv")
        df_packages.columns = [c.strip() for c in df_packages.columns]
        df_packages["Package Amount"] = pd.to_numeric(df_packages["Package Amount"], errors="coerce").fillna(0)
    except FileNotFoundError:
        return None, None, None, None, "File 'scheme_treatment_packages.csv' was not found."
    except Exception as e:
        return None, None, None, None, f"Error loading 'scheme_treatment_packages.csv': {str(e)}"

    return df_kaggle, df_hospitals, df_schemes, df_packages, None


kaggle_data, hospital_master, gov_schemes, scheme_packages, load_error = load_all_datasets()

if load_error:
    st.error(f"⚠️ {load_error}")
    st.info("Please ensure all four CSV files are present in the project directory.")
    st.stop()

# Doctor-level historical summary from Kaggle
doctor_summary = kaggle_data.groupby("Doctor Name").agg(
    records=("Patient ID", "count"),
    avg_recovery=("Recovery Score", "mean"),
    avg_cost=("Treatment Cost", "mean"),
    avg_stay=("Hospital Stay (Days)", "mean")
).reset_index().sort_values(by="avg_recovery", ascending=False)

# Procedure mapping helper: Maps specific clinical names to Kaggle Treatment Types
PROCEDURE_TO_KAGGLE_TYPE = {
    "Knee Replacement": ("Orthopedics", "Surgery"),
    "Cardiac Surgery": ("Cardiology", "Surgery"),
    "Cataract Surgery": ("General Surgery", "Surgery"),
    "General Surgery": ("General Surgery", "Surgery"),
    "Surgery": ("Selected Department", "Surgery"),
    "Therapy": ("Selected Department", "Therapy"),
    "Medication": ("Selected Department", "Medication"),
    "Observation": ("Selected Department", "Observation")
}

# ==============================================================================
# SECTION 5: TOP NAVIGATION BAR
# ==============================================================================
st.markdown("""
<div class="top-navbar">
    <div>
        <div class="brand-title">🏥 SmartCare | Smart Hospital Recommendation System</div>
        <div class="brand-subtitle">Government Scheme & Treatment Decision-Support Platform (Academic Prototype)</div>
    </div>
</div>
""", unsafe_allow_html=True)

nav_options = ["Home", "Find Hospital", "Surgery Cost", "Doctors", "Government Schemes", "Contact"]
nav_col1, nav_col2 = st.columns([5.2, 1.4])

with nav_col1:
    selected_nav = st.pills(
        "Navigation Menu",
        options=nav_options,
        default=st.session_state.current_page if st.session_state.current_page in nav_options else "Home",
        label_visibility="collapsed",
        key="main_nav_pills"
    )
    if selected_nav and selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.rerun()

with nav_col2:
    if st.button("💳 Check Surgery Cost", use_container_width=True, type="primary"):
        st.session_state.current_page = "Surgery Cost"
        st.rerun()

st.write("")

# Emergency hotline banner
st.markdown("""
<div class="emergency-banner">
    🚨 <strong>Emergency Notice:</strong> For life-threatening emergencies, dial <strong>108</strong> (Ambulance) or <strong>102</strong> immediately. This academic prototype does not manage emergency hospital admissions.
</div>
""", unsafe_allow_html=True)

# Helper function to compute cost and scheme package payable
def calculate_cost_and_scheme_payable(department, treatment_name, scheme_name):
    # Determine Kaggle category
    if treatment_name in PROCEDURE_TO_KAGGLE_TYPE:
        mapped_dept, mapped_type = PROCEDURE_TO_KAGGLE_TYPE[treatment_name]
        dept_to_use = department if mapped_dept == "Selected Department" else mapped_dept
        type_to_use = mapped_type
    else:
        dept_to_use = department
        type_to_use = "Surgery"

    # Query Kaggle treatment records
    match_k = kaggle_data[
        (kaggle_data["Department"].str.lower() == dept_to_use.lower()) &
        (kaggle_data["Treatment Type"].str.lower() == type_to_use.lower())
    ]

    # Fallback to department average if specific combination has no records
    if match_k.empty:
        match_k = kaggle_data[kaggle_data["Department"].str.lower() == dept_to_use.lower()]
    if match_k.empty:
        match_k = kaggle_data

    avg_base_cost = match_k["Treatment Cost"].mean()
    min_base_cost = match_k["Treatment Cost"].min()
    max_base_cost = match_k["Treatment Cost"].max()
    avg_rec = match_k["Recovery Score"].mean()
    avg_stay = match_k["Hospital Stay (Days)"].mean()

    # Query Scheme Package Dataset
    scheme_benefit = 0.0
    verification_req = "Yes"
    if scheme_name and scheme_name != "No Scheme":
        # Search by exact treatment name first
        pkg_row = scheme_packages[
            (scheme_packages["Scheme Name"].str.lower() == scheme_name.lower()) &
            (scheme_packages["Treatment Type"].str.lower() == treatment_name.lower())
        ]
        # Fallback to category type
        if pkg_row.empty:
            pkg_row = scheme_packages[
                (scheme_packages["Scheme Name"].str.lower() == scheme_name.lower()) &
                (scheme_packages["Treatment Type"].str.lower() == type_to_use.lower()) &
                (scheme_packages["Department"].str.lower() == dept_to_use.lower())
            ]
        if not pkg_row.empty:
            scheme_benefit = float(pkg_row.iloc[0]["Package Amount"])
            verification_req = pkg_row.iloc[0]["Verification Required"]

    estimated_patient_payable = max(0.0, avg_base_cost - scheme_benefit)

    return {
        "dept": dept_to_use,
        "type": type_to_use,
        "avg_base_cost": avg_base_cost,
        "min_base_cost": min_base_cost,
        "max_base_cost": max_base_cost,
        "scheme_benefit": scheme_benefit,
        "estimated_patient_payable": estimated_patient_payable,
        "avg_recovery": avg_rec,
        "avg_stay": avg_stay,
        "verification_required": verification_req
    }


# ==============================================================================
# SECTION 6: PAGE IMPLEMENTATIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# PAGE 1: HOME
# ------------------------------------------------------------------------------
if st.session_state.current_page == "Home":

    # --- HERO SECTION ---
    st.markdown("""
    <div class="hero-container">
        <span class="hero-badge">Academic Healthcare Decision Support</span>
        <div class="hero-heading">Find the Right Hospital for Your Surgery</div>
        <div class="hero-subheading">
            Compare treatment costs, government scheme support, recovery information and doctor experience in one place.
            Evaluate out-of-pocket costs with scheme package benefits to find healthcare options within your budget.
        </div>
    </div>
    """, unsafe_allow_html=True)

    h_btn1, h_btn2, _ = st.columns([1.5, 1.8, 3.5])
    with h_btn1:
        if st.button("🔍 Find a Hospital", type="primary", use_container_width=True):
            st.session_state.current_page = "Find Hospital"
            st.rerun()
    with h_btn2:
        if st.button("💰 Check Surgery Cost", use_container_width=True):
            st.session_state.current_page = "Surgery Cost"
            st.rerun()

    st.write("")
    st.divider()

    # --- 4 FEATURE CARDS ---
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="med-card">
            <span class="card-badge badge-primary">Financial Transparency</span>
            <h4 style="margin: 0.3rem 0; color: #0A4D68;">Treatment Cost</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Calculate expected surgery costs across departments based on 200 actual historical treatment records.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="med-card">
            <span class="card-badge badge-success">Financial Protection</span>
            <h4 style="margin: 0.3rem 0; color: #0A4D68;">Government Scheme Support</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Evaluate package coverage for Dr. NTR Vaidya Seva / Aarogyasri, PM-JAY, CGHS, and ESI to estimate patient payable.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="med-card">
            <span class="card-badge badge-warning">Physician Metrics</span>
            <h4 style="margin: 0.3rem 0; color: #0A4D68;">Doctor Information</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Review attending physicians benchmarked by patient volume, recovery scores, and average stay durations.</p>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="med-card">
            <span class="card-badge badge-primary">Clinical Outcomes</span>
            <h4 style="margin: 0.3rem 0; color: #0A4D68;">Recovery Analysis</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Understand clinical recovery scores and hospitalization days to select optimal care pathways.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- HOW IT WORKS (4 STEPS) ---
    st.subheader("📋 How It Works")
    st.caption("Four simple steps to compare procedures and find suitable care options.")

    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown("""
        <div class="step-box">
            <div class="step-number">01</div>
            <strong>Enter Patient Details</strong>
            <p style="font-size: 0.84rem; color: #64748B; margin-top: 0.3rem;">Provide patient age, location, and clinical requirements.</p>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="step-box">
            <div class="step-number">02</div>
            <strong>Select Surgery & Scheme</strong>
            <p style="font-size: 0.84rem; color: #64748B; margin-top: 0.3rem;">Choose procedure and indicate Dr NTR Vaidya Seva or other government scheme.</p>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="step-box">
            <div class="step-number">03</div>
            <strong>Calculate Payable Cost</strong>
            <p style="font-size: 0.84rem; color: #64748B; margin-top: 0.3rem;">System estimates scheme benefit and your out-of-pocket patient payable.</p>
        </div>
        """, unsafe_allow_html=True)
    with s4:
        st.markdown("""
        <div class="step-box">
            <div class="step-number">04</div>
            <strong>Get Ranked Hospitals</strong>
            <p style="font-size: 0.84rem; color: #64748B; margin-top: 0.3rem;">View multi-factor recommendation scores balancing payable cost, stay, and recovery.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- TOP DOCTORS BASED ON DATASET ---
    st.subheader("👨‍⚕️ Recommended Doctors Based on Available Dataset")
    st.caption("Historical doctor profiles computed from actual patient recovery records in the Kaggle dataset.")

    doc_cols = st.columns(len(doctor_summary))
    for idx, (_, drow) in enumerate(doctor_summary.iterrows()):
        with doc_cols[idx]:
            st.markdown(f"""
            <div class="med-card">
                <span class="card-badge badge-success">Attending Physician</span>
                <div style="font-size: 1.05rem; font-weight: 700; color: #0A4D68; margin-bottom: 0.3rem;">{drow['Doctor Name']}</div>
                <div style="font-size: 0.82rem; color: #64748B; margin-bottom: 0.5rem;">{int(drow['records'])} Historical Cases</div>
                <div style="font-size: 0.82rem; color: #1E293B; line-height: 1.6;">
                    ⭐ Avg Recovery: <strong>{drow['avg_recovery']:.1f}/100</strong><br>
                    💰 Avg Cost: <strong>₹{drow['avg_cost']:,.0f}</strong><br>
                    ⏱️ Avg Stay: <strong>{drow['avg_stay']:.1f} Days</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- FAQ SECTION ---
    st.subheader("❓ Frequently Asked Questions (FAQ)")
    with st.expander("What does the system recommend?"):
        st.write("The system recommends suitable hospital-treatment options and supervising doctors by analyzing historical patient recovery records, treatment costs, and hospitalization durations from our dataset.")

    with st.expander("How is the recommendation score calculated?"):
        st.write("The recommendation score is calculated using a multi-factor weighting algorithm: Treatment Affordability / Patient Payable (35%), Clinical Recovery Score (30%), Doctor Historical Recovery (20%), Hospital Stay Duration (10%), and Budget Compatibility (5%). All factors are normalized from 0 to 100.")

    with st.expander("How is treatment cost estimated?"):
        st.write("Treatment cost is estimated using historical records from the Kaggle dataset for the selected department and procedure type. It displays average observed costs and the full min-max range.")

    with st.expander("Does Aarogyasri automatically reduce my cost?"):
        st.write("No. Aarogyasri / Dr. NTR Vaidya Seva coverage is subject to beneficiary eligibility verification, approved procedure packages, and network hospital empanelment. The system estimates potential package coverage based on demo package schedules, but final approval must be verified with the official scheme authorities.")

    with st.expander("Are the doctor rankings medical recommendations?"):
        st.write("No. The doctor rankings represent historical statistical summaries based purely on the available dataset records. They do not constitute an objective clinical endorsement or medical credential evaluation.")

    with st.expander("Is the result a final medical decision?"):
        st.write("No. This system is an academic decision-support prototype. It does not provide medical diagnosis or replace consultation with qualified healthcare professionals.")


# ------------------------------------------------------------------------------
# PAGE 2: FIND HOSPITAL (MULTI-FACTOR RECOMMENDATION ENGINE)
# ------------------------------------------------------------------------------
elif st.session_state.current_page == "Find Hospital":

    st.markdown("""
    <div class="hero-container" style="padding: 1.8rem 1.5rem;">
        <span class="hero-badge">Multi-Factor Decision Engine</span>
        <div class="hero-heading" style="font-size: 1.8rem;">Find Suitable Hospitals & Treatment Options</div>
        <div class="hero-subheading" style="font-size: 0.95rem; margin-bottom: 0;">
            Compare hospitals and doctors using estimated patient payable costs (after government scheme package deductions), recovery scores, and hospitalization stay.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("🔍 Search & Recommendation Parameters")
        f1, f2, f3 = st.columns(3)

        with f1:
            depts = sorted(kaggle_data["Department"].unique().tolist())
            selected_dept = st.selectbox(
                "Department / Specialty",
                options=depts,
                index=depts.index(st.session_state.search_department) if st.session_state.search_department in depts else 0
            )

        with f2:
            proc_options = ["Knee Replacement", "Cardiac Surgery", "General Surgery", "Surgery", "Therapy", "Medication", "Observation"]
            selected_treatment = st.selectbox(
                "Treatment / Surgery",
                options=proc_options,
                index=proc_options.index(st.session_state.search_treatment) if st.session_state.search_treatment in proc_options else 0
            )

        with f3:
            user_budget = st.number_input(
                "Maximum Treatment Budget (₹)",
                min_value=5000,
                max_value=300000,
                value=int(st.session_state.search_budget),
                step=5000
            )

        f4, f5 = st.columns(2)
        with f4:
            available_cities = ["All Cities"] + sorted(hospital_master["City"].unique().tolist())
            city_idx = available_cities.index(st.session_state.search_city) if st.session_state.search_city in available_cities else 0
            selected_city = st.selectbox("Patient City / Preferred Location", options=available_cities, index=city_idx)

        with f5:
            scheme_list = ["No Scheme", "Dr NTR Vaidya Seva / Aarogyasri", "Ayushman Bharat PM-JAY", "Central Government Health Scheme (CGHS)", "Employees' State Insurance (ESI)", "Rashtriya Arogya Nidhi (RAN)"]
            scheme_idx = scheme_list.index(st.session_state.search_scheme) if st.session_state.search_scheme in scheme_list else 1
            selected_scheme = st.selectbox("Government Health Scheme", options=scheme_list, index=scheme_idx)

        run_recommendation = st.button("🔍 Find Best Hospital", type="primary", use_container_width=True)

    if run_recommendation:
        st.session_state.search_department = selected_dept
        st.session_state.search_treatment = selected_treatment
        st.session_state.search_budget = user_budget
        st.session_state.search_scheme = selected_scheme
        if selected_city != "All Cities":
            st.session_state.search_city = selected_city

        # 1. Compute Cost & Scheme Package
        cost_calc = calculate_cost_and_scheme_payable(selected_dept, selected_treatment, selected_scheme)

        st.markdown(f"""
        <div class="scheme-disclaimer">
            🏛️ <strong>Scheme Package Assessment:</strong> {selected_scheme} | 
            Estimated Base Cost: <strong>₹{cost_calc['avg_base_cost']:,.0f}</strong> | 
            Estimated Scheme Package Benefit: <strong>₹{cost_calc['scheme_benefit']:,.0f}</strong> | 
            Estimated Patient Payable: <strong>₹{cost_calc['estimated_patient_payable']:,.0f}</strong><br>
            <em>⚠️ Government scheme benefits shown here are for educational/demo purposes. Actual eligibility, package coverage, hospital empanelment, authorization and patient payable amount must be verified with the relevant government scheme and hospital.</em>
        </div>
        """, unsafe_allow_html=True)

        # 2. Match Hospitals
        # Match by department
        h_pool = hospital_master[hospital_master["Departments"].str.contains(selected_dept, case=False, na=False)].copy()
        if h_pool.empty:
            h_pool = hospital_master.copy()

        # Filter by city if specified
        if selected_city != "All Cities":
            city_subset = h_pool[h_pool["City"].str.lower() == selected_city.lower()]
            if not city_subset.empty:
                h_pool = city_subset
            else:
                st.info(f"ℹ️ No hospitals listed strictly in {selected_city} for {selected_dept}; displaying nearest regional network facilities.")

        # Assign doctors and clinical scores from Kaggle data
        doctors_in_dept = kaggle_data[kaggle_data["Department"] == selected_dept]["Doctor Name"].unique().tolist()
        if not doctors_in_dept:
            doctors_in_dept = kaggle_data["Doctor Name"].unique().tolist()

        candidate_records = []
        for idx, (_, h_row) in enumerate(h_pool.iterrows()):
            assigned_doc = doctors_in_dept[idx % len(doctors_in_dept)]
            doc_info = doctor_summary[doctor_summary["Doctor Name"] == assigned_doc]
            doc_rec = doc_info["avg_recovery"].values[0] if not doc_info.empty else 72.0

            # Check if this hospital is empanelled for the selected scheme
            is_empanelled = False
            if selected_scheme != "No Scheme":
                short_scheme = "Dr NTR Vaidya Seva" if "Dr NTR" in selected_scheme else selected_scheme.split()[0]
                is_empanelled = short_scheme.lower() in h_row["Scheme Support"].lower()

            # If empanelled, apply scheme package benefit; if not empanelled, patient payable = full base cost
            if is_empanelled:
                effective_payable = cost_calc["estimated_patient_payable"]
                applied_benefit = cost_calc["scheme_benefit"]
            else:
                effective_payable = cost_calc["avg_base_cost"]
                applied_benefit = 0.0

            candidate_records.append({
                "Hospital ID": h_row["Hospital ID"],
                "Hospital Name": h_row["Hospital Name"],
                "City": h_row["City"],
                "Hospital Type": h_row["Hospital Type"],
                "Doctor Name": assigned_doc,
                "Treatment Cost": cost_calc["avg_base_cost"],
                "Estimated Scheme Benefit": applied_benefit,
                "Estimated Patient Payable": effective_payable,
                "Recovery Score": cost_calc["avg_recovery"],
                "Doctor Historical Recovery": doc_rec,
                "Hospital Stay (Days)": cost_calc["avg_stay"],
                "Scheme Empanelled": "Yes" if is_empanelled else "No",
                "Scheme Support": h_row["Scheme Support"]
            })

        df_candidates = pd.DataFrame(candidate_records)

        # ----------------------------------------------------------------------
        # MULTI-FACTOR RECOMMENDATION ALGORITHM
        # ----------------------------------------------------------------------
        # 1. Cost / Affordability (Weight: 35%) - Lower patient payable is preferred
        min_p = df_candidates["Estimated Patient Payable"].min()
        max_p = df_candidates["Estimated Patient Payable"].max()
        if max_p != min_p:
            df_candidates["Affordability Score"] = ((max_p - df_candidates["Estimated Patient Payable"]) / (max_p - min_p)) * 100
        else:
            df_candidates["Affordability Score"] = 100.0

        # 2. Recovery Score (Weight: 30%)
        df_candidates["Recovery Component"] = df_candidates["Recovery Score"]

        # 3. Doctor Historical Recovery (Weight: 20%)
        df_candidates["Doctor Component"] = df_candidates["Doctor Historical Recovery"]

        # 4. Hospital Stay (Weight: 10%) - Shorter stay preferred
        min_s = df_candidates["Hospital Stay (Days)"].min()
        max_s = df_candidates["Hospital Stay (Days)"].max()
        if max_s != min_s:
            df_candidates["Stay Score"] = ((max_s - df_candidates["Hospital Stay (Days)"]) / (max_s - min_s)) * 100
        else:
            df_candidates["Stay Score"] = 100.0

        # 5. Budget Compatibility (Weight: 5%)
        df_candidates["Budget Score"] = df_candidates["Estimated Patient Payable"].apply(
            lambda c: 100.0 if c <= user_budget else max(0.0, 100.0 - ((c - user_budget) / user_budget) * 100)
        )

        # Calculate composite score
        WEIGHT_COST = 0.35
        WEIGHT_RECOVERY = 0.30
        WEIGHT_DOCTOR = 0.20
        WEIGHT_STAY = 0.10
        WEIGHT_BUDGET = 0.05

        df_candidates["Recommendation Score"] = (
            (df_candidates["Affordability Score"] * WEIGHT_COST) +
            (df_candidates["Recovery Component"] * WEIGHT_RECOVERY) +
            (df_candidates["Doctor Component"] * WEIGHT_DOCTOR) +
            (df_candidates["Stay Score"] * WEIGHT_STAY) +
            (df_candidates["Budget Score"] * WEIGHT_BUDGET)
        ).round(1)

        ranked = df_candidates.sort_values(by="Recommendation Score", ascending=False).reset_index(drop=True)

        # ----------------------------------------------------------------------
        # DISPLAY TOP RECOMMENDATION
        # ----------------------------------------------------------------------
        st.divider()
        st.markdown("<h3 style='color: #0A4D68;'>⭐ YOUR RECOMMENDATION (Top Matching Option)</h3>", unsafe_allow_html=True)

        top = ranked.iloc[0]
        top_payable = top["Estimated Patient Payable"]
        is_within_budget = top_payable <= user_budget
        budget_str = "Within Budget" if is_within_budget else "Exceeds Budget"

        st.markdown(f"""
        <div class="rec-highlight-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.8rem;">
                <div>
                    <span class="card-badge badge-success">#1 Top Recommended Option</span>
                    <div style="font-size: 1.45rem; font-weight: 800; color: #0A4D68;">{top['Hospital Name']} ({top['Hospital Type']})</div>
                    <div style="font-size: 0.95rem; color: #475569;">📍 {top['City']} | {selected_dept} - {selected_treatment}</div>
                </div>
                <div style="text-align: right;">
                    <span style="font-size: 0.8rem; color: #64748B; font-weight: 600;">RECOMMENDATION SCORE</span>
                    <div style="font-size: 2rem; font-weight: 800; color: #16A34A;">{top['Recommendation Score']:.1f}<span style="font-size: 1.1rem; color: #64748B;">/100</span></div>
                </div>
            </div>
            <hr style="border: 0; border-top: 1px solid #BBF7D0; margin: 1rem 0;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem;">
                <div>
                    <span style="font-size: 0.78rem; color: #64748B; font-weight: 600;">ESTIMATED PATIENT PAYABLE</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #0F172A;">₹{top_payable:,.0f}</div>
                    <span style="font-size: 0.75rem; color: {'#16A34A' if is_within_budget else '#DC2626'}; font-weight: 600;">{budget_str} (Budget: ₹{user_budget:,.0f})</span>
                </div>
                <div>
                    <span style="font-size: 0.78rem; color: #64748B; font-weight: 600;">COST BREAKDOWN</span>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #334155;">Base Cost: ₹{top['Treatment Cost']:,.0f}</div>
                    <span style="font-size: 0.75rem; color: #0284C7; font-weight: 600;">Scheme Benefit: ₹{top['Estimated Scheme Benefit']:,.0f}</span>
                </div>
                <div>
                    <span style="font-size: 0.78rem; color: #64748B; font-weight: 600;">ATTENDING DOCTOR</span>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #0F172A;">{top['Doctor Name']}</div>
                    <span style="font-size: 0.75rem; color: #64748B;">Historical Recovery: {top['Doctor Historical Recovery']:.1f}/100</span>
                </div>
                <div>
                    <span style="font-size: 0.78rem; color: #64748B; font-weight: 600;">SCHEME EMPANELLED</span>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #0F172A;">{top['Scheme Empanelled']}</div>
                    <span style="font-size: 0.75rem; color: #64748B;">{top['Scheme Support']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        b_c1, b_c2, _ = st.columns([1.5, 1.5, 3])
        with b_c1:
            if st.button("📅 Enquire for this Hospital", type="primary", use_container_width=True):
                st.session_state.current_page = "Contact"
                st.rerun()
        with b_c2:
            if st.button("💳 Re-Check Surgery Cost", use_container_width=True):
                st.session_state.current_page = "Surgery Cost"
                st.rerun()

        # ----------------------------------------------------------------------
        # OTHER MATCHING HOSPITALS (COMPARISON TABLE)
        # ----------------------------------------------------------------------
        st.write("")
        st.subheader("🏥 Top Matching Hospitals (Comparison)")
        st.caption("Ranked by multi-factor recommendation score. Click 'View Details' or 'Enquire' below.")

        display_df = pd.DataFrame({
            "Hospital Name": ranked["Hospital Name"],
            "City": ranked["City"],
            "Hospital Type": ranked["Hospital Type"],
            "Doctor Name": ranked["Doctor Name"],
            "Base Cost": ranked["Treatment Cost"].apply(lambda x: f"₹{x:,.0f}"),
            "Scheme Benefit": ranked["Estimated Scheme Benefit"].apply(lambda x: f"₹{x:,.0f}"),
            "Estimated Patient Payable": ranked["Estimated Patient Payable"].apply(lambda x: f"₹{x:,.0f}"),
            "Recovery Score": ranked["Recovery Score"].astype(int),
            "Hospital Stay": ranked["Hospital Stay (Days)"].apply(lambda x: f"{int(x)} Days"),
            "Empanelled": ranked["Scheme Empanelled"],
            "Recommendation Score": ranked["Recommendation Score"]
        })

        st.dataframe(display_df, use_container_width=True, hide_index=True)


# ------------------------------------------------------------------------------
# PAGE 3: SURGERY COST ESTIMATION
# ------------------------------------------------------------------------------
elif st.session_state.current_page == "Surgery Cost":

    st.markdown("""
    <div class="hero-container" style="padding: 1.8rem 1.5rem;">
        <span class="hero-badge">Transparent Cost Estimation</span>
        <div class="hero-heading" style="font-size: 1.8rem;">Check Surgery & Treatment Cost</div>
        <div class="hero-subheading" style="font-size: 0.95rem; margin-bottom: 0;">
            Enter patient details, procedure, and government health scheme to calculate your estimated patient payable amount based on Kaggle data and demo package schedules.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("surgery_cost_form"):
        st.subheader("👤 Patient & Procedure Information")

        c1, c2, c3 = st.columns(3)
        with c1:
            p_name = st.text_input("Patient Name", value="R. Sharma")
        with c2:
            p_age = st.number_input("Age", min_value=1, max_value=110, value=52)
        with c3:
            p_gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        c4, c5, c6 = st.columns(3)
        with c4:
            p_mobile = st.text_input("Mobile Number", value="9876543210")
        with c5:
            p_location = st.selectbox("Location / City", ["Vijayawada", "Guntur", "Visakhapatnam", "Tirupati", "Hyderabad"])
        with c6:
            all_depts = sorted(kaggle_data["Department"].unique().tolist())
            p_dept = st.selectbox(
                "Department",
                options=all_depts,
                index=all_depts.index(st.session_state.search_department) if st.session_state.search_department in all_depts else 4
            )

        st.divider()
        st.subheader("🩺 Treatment & Financial Details")

        d1, d2, d3 = st.columns(3)
        with d1:
            p_procedures = ["Knee Replacement", "Cardiac Surgery", "General Surgery", "Surgery", "Therapy", "Medication", "Observation"]
            p_treatment = st.selectbox(
                "Treatment / Surgery",
                options=p_procedures,
                index=p_procedures.index(st.session_state.search_treatment) if st.session_state.search_treatment in p_procedures else 0
            )
        with d2:
            p_budget = st.number_input("Maximum Budget (₹)", min_value=5000, max_value=300000, value=int(st.session_state.search_budget), step=5000)
        with d3:
            schemes_dropdown = [
                "Dr NTR Vaidya Seva / Aarogyasri",
                "Ayushman Bharat PM-JAY",
                "Central Government Health Scheme (CGHS)",
                "Employees' State Insurance (ESI)",
                "Rashtriya Arogya Nidhi (RAN)",
                "No Scheme"
            ]
            p_scheme = st.selectbox("Government Scheme", options=schemes_dropdown, index=0)

        p_insurance = st.selectbox("Private Health Insurance Available?", ["No", "Yes"])

        cost_submit = st.form_submit_button("📊 CHECK SURGERY COST", type="primary", use_container_width=True)

    if cost_submit:
        st.session_state.search_department = p_dept
        st.session_state.search_treatment = p_treatment
        st.session_state.search_budget = p_budget
        st.session_state.search_scheme = p_scheme
        st.session_state.search_city = p_location

        calc = calculate_cost_and_scheme_payable(p_dept, p_treatment, p_scheme)

        st.divider()
        st.subheader("📑 Estimated Surgery Cost Summary")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Estimated Treatment Cost", f"₹{calc['avg_base_cost']:,.0f}", delta=f"Observed Range: ₹{calc['min_base_cost']:,.0f} - ₹{calc['max_base_cost']:,.0f}")
        with m2:
            st.metric("Estimated Scheme Benefit", f"₹{calc['scheme_benefit']:,.0f}", delta=f"Scheme: {p_scheme[:18]}...")
        with m3:
            payable_amt = calc["estimated_patient_payable"]
            st.metric(
                "Estimated Patient Payable",
                f"₹{payable_amt:,.0f}",
                delta="Within Budget" if payable_amt <= p_budget else "Exceeds Budget",
                delta_color="normal" if payable_amt <= p_budget else "inverse"
            )

        st.markdown("""
        <div class="scheme-disclaimer">
            <strong>⚠️ Government Scheme Disclaimer:</strong> Scheme eligibility, package coverage, hospital empanelment and final payable amount must be verified with the official scheme/hospital before treatment.
            Government scheme benefits shown here are for educational/demo purposes.
        </div>
        """, unsafe_allow_html=True)

        if p_scheme == "Dr NTR Vaidya Seva / Aarogyasri":
            st.info("🏛️ **Dr. NTR Vaidya Seva Benefit:** For eligible AP families (Rice card holders), identified therapy packages provide cashless treatment at empanelled network hospitals. Approval requires biometric pre-authorization by the network hospital *Aarogya Mithra*.")
        elif p_scheme == "Ayushman Bharat PM-JAY":
            st.info("🏛️ **PM-JAY Benefit:** Provides health cover of up to ₹5 Lakhs per family per year for secondary and tertiary care hospitalization across empanelled hospitals nationally.")

        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            if st.button("🔍 Recommend Hospitals for this Treatment", type="primary", use_container_width=True):
                st.session_state.current_page = "Find Hospital"
                st.rerun()
        with c_btn2:
            if st.button("📅 Demo Enquiry / Consultation Booking", use_container_width=True):
                st.session_state.current_page = "Contact"
                st.rerun()


# ------------------------------------------------------------------------------
# PAGE 4: DOCTORS DIRECTORY
# ------------------------------------------------------------------------------
elif st.session_state.current_page == "Doctors":

    st.markdown("""
    <div class="hero-container" style="padding: 1.8rem 1.5rem;">
        <span class="hero-badge">Clinical Directory</span>
        <div class="hero-heading" style="font-size: 1.8rem;">Top Matching Doctors Based on Available Dataset</div>
        <div class="hero-subheading" style="font-size: 0.95rem; margin-bottom: 0;">
            Review historical physician recovery scores and clinical volume calculated strictly from the Kaggle patient dataset.
        </div>
    </div>
    """, unsafe_allow_html=True)

    filter_dept = st.selectbox("Filter Doctors by Specialty", ["All Specialties"] + sorted(kaggle_data["Department"].unique().tolist()))

    if filter_dept == "All Specialties":
        df_docs = kaggle_data
    else:
        df_docs = kaggle_data[kaggle_data["Department"].str.lower() == filter_dept.lower()]

    d_stats = df_docs.groupby("Doctor Name").agg(
        records=("Patient ID", "count"),
        avg_recovery=("Recovery Score", "mean"),
        avg_cost=("Treatment Cost", "mean"),
        avg_stay=("Hospital Stay (Days)", "mean")
    ).reset_index().sort_values(by="avg_recovery", ascending=False)

    st.write("")
    for _, drow in d_stats.iterrows():
        depts_list = ", ".join(kaggle_data[kaggle_data["Doctor Name"] == drow["Doctor Name"]]["Department"].unique().tolist())
        st.markdown(f"""
        <div class="med-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <span class="card-badge badge-primary">{depts_list}</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #0A4D68;">{drow['Doctor Name']}</div>
                    <div style="font-size: 0.85rem; color: #64748B;">Specialty Practitioner | Verified in Kaggle Dataset</div>
                </div>
                <div style="text-align: right;">
                    <span class="card-badge badge-success">⭐ Historical Recovery: {drow['avg_recovery']:.1f}/100</span>
                    <div style="font-size: 0.8rem; color: #64748B;">Based on {int(drow['records'])} dataset cases</div>
                </div>
            </div>
            <hr style="border: 0; border-top: 1px solid #F1F5F9; margin: 0.8rem 0;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; font-size: 0.88rem;">
                <div>💼 Available Dataset Records: <strong>{int(drow['records'])} Treatments</strong></div>
                <div>💰 Average Treatment Cost: <strong>₹{drow['avg_cost']:,.0f}</strong></div>
                <div>⏱️ Average Hospital Stay: <strong>{drow['avg_stay']:.1f} Days</strong></div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# PAGE 5: GOVERNMENT SCHEMES
# ------------------------------------------------------------------------------
elif st.session_state.current_page == "Government Schemes":

    st.markdown("""
    <div class="hero-container" style="padding: 1.8rem 1.5rem;">
        <span class="hero-badge">Health Protection</span>
        <div class="hero-heading" style="font-size: 1.8rem;">Government Health Schemes Considered</div>
        <div class="hero-subheading" style="font-size: 0.95rem; margin-bottom: 0;">
            Overview of major public health schemes in India and Andhra Pradesh for surgical package support and financial risk protection.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="scheme-disclaimer">
        <strong>⚠️ Important Notice:</strong> Government scheme benefits shown here are for educational/demo purposes.
        Actual eligibility, package coverage, hospital empanelment, authorization and patient payable amount must be verified with the relevant government scheme and hospital.
    </div>
    """, unsafe_allow_html=True)

    for _, srow in gov_schemes.iterrows():
        try:
            cov_val = int(srow['Annual Coverage'])
            cov_str = f"₹{cov_val:,}" if cov_val > 0 else "Defined Package Based"
        except (ValueError, TypeError):
            cov_str = "Defined Package Based"

        st.markdown(f"""
        <div class="med-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <span class="card-badge badge-primary">{srow['State']}</span>
                    <h3 style="color: #0A4D68; margin: 0.2rem 0;">{srow['Scheme Name']}</h3>
                    <p style="color: #475569; font-size: 0.92rem; margin: 0.4rem 0;"><strong>Intended Beneficiaries:</strong> {srow['Eligibility']}</p>
                </div>
                <div style="text-align: right;">
                    <span class="card-badge badge-warning">Verification: {srow['Verification Required']}</span>
                    <div style="font-weight: 700; color: #088395; margin-top: 0.2rem;">{srow['Cost Reduction Type']}</div>
                </div>
            </div>
            <hr style="border: 0; border-top: 1px solid #F1F5F9; margin: 0.8rem 0;">
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; font-size: 0.85rem; color: #334155;">
                <div>📜 Official Source / Authority: <strong>{srow['Official Source']}</strong></div>
                <div>🛡️ Maximum Annual Coverage: <strong>{cov_str}</strong></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🌐 Official Government Portals")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.link_button("🏛️ Dr. YSR Aarogyasri Trust Portal (AP)", "https://ysraarogyasri.ap.gov.in/", use_container_width=True)
    with col_l2:
        st.link_button("🇮🇳 Ayushman Bharat PM-JAY Official Portal", "https://pmjay.gov.in/", use_container_width=True)


# ------------------------------------------------------------------------------
# PAGE 6: CONTACT / DEMO ENQUIRY
# ------------------------------------------------------------------------------
elif st.session_state.current_page == "Contact":

    st.markdown("""
    <div class="hero-container" style="padding: 1.8rem 1.5rem;">
        <span class="hero-badge">Patient Enquiry</span>
        <div class="hero-heading" style="font-size: 1.8rem;">Book Surgery Consultation / Demo Enquiry</div>
        <div class="hero-subheading" style="font-size: 0.95rem; margin-bottom: 0;">
            Submit your treatment preferences to record an enquiry for this academic prototype demonstration.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("enquiry_form"):
        st.subheader("📝 Demo Consultation Enquiry Form")
        e1, e2 = st.columns(2)
        with e1:
            enq_name = st.text_input("Full Name", value="Ramesh Kumar")
            enq_age = st.number_input("Age", min_value=1, max_value=110, value=52)
            enq_phone = st.text_input("Mobile Number", value="9876543210")
        with e2:
            h_opts = sorted(hospital_master["Hospital Name"].unique().tolist())
            enq_hospital = st.selectbox("Preferred Hospital", options=h_opts)
            enq_treatment = st.selectbox("Treatment / Surgery Required", ["Knee Replacement", "Cardiac Surgery", "General Surgery", "Surgery", "Therapy", "Medication", "Observation"])
            enq_date = st.date_input("Preferred Consultation Date")

        e3, e4 = st.columns(2)
        with e3:
            enq_budget = st.number_input("Expected Budget (₹)", min_value=5000, max_value=300000, value=80000, step=5000)
        with e4:
            enq_scheme = st.selectbox("Government Scheme / Insurance", ["Dr NTR Vaidya Seva / Aarogyasri", "Ayushman Bharat PM-JAY", "CGHS", "ESI", "Private Insurance", "None"])

        enq_msg = st.text_area("Message / Clinical Details", placeholder="Specify any symptoms or doctor preferences...")

        enq_btn = st.form_submit_button("📩 Submit Demo Enquiry", type="primary", use_container_width=True)

    if enq_btn:
        ref_id = f"ENQ-2026-{np.random.randint(1000, 9999)}"
        st.session_state.enquiries.append({
            "id": ref_id,
            "name": enq_name,
            "hospital": enq_hospital,
            "treatment": enq_treatment,
            "scheme": enq_scheme
        })
        st.success(f"✅ Your enquiry has been recorded for this academic prototype! Reference ID: **{ref_id}**")
        st.info("ℹ️ **Demo Notice:** This is an academic simulation for project evaluation. No real clinical appointment is booked.")


# ==============================================================================
# SECTION 7: ACADEMIC MEDICAL DISCLAIMER & PORTAL FOOTER
# ==============================================================================
st.markdown("""
<div class="disclaimer-box">
    <strong>⚠️ Medical & Financial Disclaimer:</strong> This platform is an academic prototype for healthcare comparison and decision-support.
    Recommendations are based on available dataset information and should not replace professional medical advice.
    Treatment cost, scheme eligibility, hospital availability, and doctor information must be verified directly with the hospital or relevant government authority.
    For medical emergencies, contact emergency medical services (108) or visit the nearest emergency department immediately.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="portal-footer">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div style="font-size: 1.05rem; font-weight: 800; color: white;">🏥 Smart Hospital Recommendation System</div>
            <div style="color: #94A3B8; font-size: 0.8rem; margin-top: 0.2rem;">College Project Prototype | Not a medical diagnosis or financial guarantee.</div>
        </div>
        <div style="color: #94A3B8; font-size: 0.8rem;">
            Datasets: Kaggle Hospital Treatment Dataset | Demo Hospital Reference | Government Schemes & Package Schedules
        </div>
    </div>
</div>
""", unsafe_allow_html=True)