# 🏥 Smart Hospital Recommendation System
## Healthcare Decision-Support & Government Scheme Package Analysis Platform

An academic healthcare decision-support and hospital recommendation platform developed in **Python**, **Streamlit**, and **Pandas**. The system integrates four decoupled datasets to evaluate historical clinical outcomes, base procedure costs, government health scheme package benefits (**Dr. NTR Vaidya Seva / Aarogyasri**, **PM-JAY**, **CGHS**, **ESI**, **RAN**), and doctor performance to calculate **Estimated Patient Payable Costs** and recommend suitable hospitals within a patient's budget.

---

## 📌 Architecture & Datasets Breakdown

The application strictly separates real clinical records from reference master and scheme data:

```text
hospital recommendation system/
│
├── app.py                           # Streamlit Web Application & Recommendation Engine
├── hospital_data.csv                # Dataset 1: Actual Kaggle Patient Treatment Dataset (Main)
├── hospital_master.csv              # Dataset 2: Demo Hospital Reference Data
├── government_schemes.csv           # Dataset 3: Government Scheme Master Dataset
├── scheme_treatment_packages.csv    # Dataset 4: Demo Scheme Treatment Package Schedule
└── README.md                        # Complete Academic Documentation & Review Guide
```

### 1. Dataset 1: Kaggle Patient Treatment Dataset (`hospital_data.csv`)
- **Size:** 200 patient treatment records.
- **Actual Fields:** `Patient ID`, `Department`, `Treatment Type`, `Doctor Name`, `Gender`, `Age`, `Treatment Cost`, `Hospital Stay (Days)`, `Recovery Score`.
- **Purpose:** Used strictly for base cost calculation, length-of-stay analysis, clinical recovery outcome scoring, and doctor performance profiling. Does **not** contain hospital names or scheme coverage.

### 2. Dataset 2: Demo Hospital Reference Data (`hospital_master.csv`)
- **Fields:** `Hospital ID`, `Hospital Name`, `City`, `State`, `Hospital Type`, `Departments`, `Scheme Support`.
- **Purpose:** Prototype reference facilities across Andhra Pradesh (*Vijayawada, Guntur, Visakhapatnam, Tirupati*) and *Hyderabad* linking specialties and government scheme empanelment.
- **Academic Label:** Clearly documented as Demo/Sample Reference Data.

### 3. Dataset 3: Government Schemes Master (`government_schemes.csv`)
- **Fields:** `Scheme ID`, `Scheme Name`, `State`, `Eligibility`, `Annual Coverage`, `Cost Reduction Type`, `Reduction Value`, `Verification Required`, `Official Source`.
- **Schemes Included:**
  1. *Dr NTR Vaidya Seva / Aarogyasri* (Andhra Pradesh - BPL Rice Card holders, annual income < ₹5 Lakhs)
  2. *Ayushman Bharat PM-JAY* (All India - SECC 2011 eligible families)
  3. *Central Government Health Scheme (CGHS)* (Central Govt employees & pensioners)
  4. *Employees' State Insurance (ESI)* (Insured workers earning up to ₹21,000/month)
  5. *Rashtriya Arogya Nidhi (RAN)* (BPL patients suffering from life-threatening conditions)

### 4. Dataset 4: Demo Scheme Treatment Packages (`scheme_treatment_packages.csv`)
- **Fields:** `Scheme Name`, `Treatment Type`, `Department`, `Package Amount`, `Patient Contribution`, `Verification Required`.
- **Purpose:** Defined procedure package amounts (e.g. *Knee Replacement: ₹90,000*, *Cardiac Surgery: ₹1,20,000*, etc.) used to determine realistic out-of-pocket costs instead of arbitrary percentage discounts.

---

## 💡 Scheme Payable Calculation Logic

Real-world government schemes operate through **defined procedure packages** and **cashless network hospital empanelment**, not arbitrary percentage discounts:

$$\text{Estimated Patient Payable} = \max(0, \text{Base Treatment Cost} - \text{Applicable Scheme Package Benefit})$$

### Example Walkthrough:
- **Treatment:** Knee Replacement (Orthopedics)
- **Base Treatment Cost:** ₹1,19,437 (Average in Kaggle dataset)
- **Selected Scheme:** Dr. NTR Vaidya Seva / Aarogyasri
- **Scheme Package Benefit:** ₹90,000 (Package Schedule)
- **Estimated Patient Payable:** **₹29,437** *(Within patient's ₹80,000 budget!)*
- If treated at an empanelled Government hospital (*e.g. GGH Vijayawada*), treatment is cashless subject to *Aarogya Mithra* pre-authorization.

---

## 🧮 Multi-Factor Recommendation Algorithm

The system ranks matching options using a normalized weighted model (Score out of 100):

$$\text{Recommendation Score} = (0.35 \times S_{\text{affordability}}) + (0.30 \times S_{\text{recovery}}) + (0.20 \times S_{\text{doctor}}) + (0.10 \times S_{\text{stay}}) + (0.05 \times S_{\text{budget}})$$

- **Affordability / Payable Cost ($35\%$):** Evaluates estimated patient out-of-pocket payable after scheme deductions.
- **Clinical Recovery Score ($30\%$):** Historical recovery ratings ($40 - 100$) from dataset records.
- **Doctor Historical Recovery ($20\%$):** Mean recovery track record of attending physician across all their cases in the dataset.
- **Hospital Stay Duration ($10\%$):** Inverted hospitalization days (shorter stay = faster recovery and lower room expenses).
- **Budget Compatibility ($5\%$):** Full adherence bonus if patient payable falls within the maximum budget.

---

## 🚀 How to Run the Project

1. Ensure Python 3.10+ or 3.11+ is installed.
2. Run from your project directory:
   ```bash
   streamlit run app.py
   ```
3. Open in your browser:
   - **Local URL:** `http://localhost:8501`

---

## 🎓 College Review / Viva Talking Points

1. **Why decouple the datasets?**
   > *"The Kaggle dataset provides patient treatment outcomes and doctor records. It does not track physical hospitals or public health schemes. Decoupling hospital master and government scheme packages ensures clean database normalization, maintains academic integrity, and reflects real-world health information systems."*

2. **Why use Package-Based Reduction rather than fixed percentage discounts?**
   > *"Government schemes such as Dr. NTR Vaidya Seva and PM-JAY operate on approved procedure package schedules, cashless pre-authorization, and empanelled hospital networks. Using package schedules reflects actual public healthcare administration in Andhra Pradesh."*

3. **How does the system ensure safety?**
   > *"The platform emphasizes that all costs are estimates, highlights official scheme portals, warns that actual coverage requires Aarogya Mithra hospital desk pre-authorization, and includes prominent emergency callouts (108/102)."*
