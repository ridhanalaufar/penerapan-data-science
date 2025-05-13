import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model/model_students-performance-15features.joblib")

# Title
st.title("Prediksi Status Mahasiswa")
st.markdown(
    "Aplikasi ini memprediksi apakah seorang mahasiswa akan **Dropout** atau **Lulus** berdasarkan data akademik dan personal."
)

# --- Input Data ---

# 1. Curricular_units_2nd_sem_approved:
curricular_units_2nd_sem_approved = st.slider(
    "Jumlah mata kuliah semester 2 yang disetujui", 0, 20, 0, step=1
)

# 2. Curricular_units_1st_sem_approved:
curricular_units_1st_sem_approved = st.slider(
    "Jumlah mata kuliah semester 1 yang disetujui", 0, 20, 0, step=1
)

# 3. Curricular_units_2nd_sem_grade:
curricular_units_2nd_sem_grade = st.slider(
    "Rata-rata nilai semester 2", 0.0, 100.0, 0.0, step=0.1
)

# 4. Curricular_units_1st_sem_grade:
curricular_units_1st_sem_grade = st.slider(
    "Rata-rata nilai semester 1", 0.0, 100.0, 0.0, step=0.1
)

# 5. Tuition fees up to date:
# Sesuai deskripsi: 1 – yes, 0 – no
tuition_options = ["1 - Yes", "0 - No"]
tuition_fees_up_to_date = st.selectbox("Pembayaran kuliah up-to-date?", tuition_options)

# 6. Curricular_units_2nd_sem_evaluations:
curricular_units_2nd_sem_evaluations = st.slider(
    "Jumlah evaluasi mata kuliah semester 2 (1)", 0, 10, 0, step=1
)

# 7. Age at enrollment:
age_at_enrollment = st.slider("Usia saat pendaftaran", 15, 60, 15, step=1)

# 8. Course:
# Sesuai deskripsi:
course_options = [
    "33 - Biofuel Production Technologies",
    "171 - Animation and Multimedia Design",
    "8014 - Social Service (evening attendance)",
    "9003 - Agronomy",
    "9070 - Communication Design",
    "9085 - Veterinary Nursing",
    "9119 - Informatics Engineering",
    "9130 - Equinculture",
    "9147 - Management",
    "9238 - Social Service",
    "9254 - Tourism",
    "9500 - Nursing",
    "9556 - Oral Hygiene",
    "9670 - Advertising and Marketing Management",
    "9773 - Journalism and Communication",
    "9853 - Basic Education",
    "9991 - Management (evening attendance)"
]
course = st.selectbox("Program Studi (Course)", course_options)

# 9. Curricular_units_2nd_sem_evaluations_2:
# (Jika diperlukan sebagai evaluasi kedua dari semester 2)
curricular_units_2nd_sem_evaluations_2 = st.slider(
    "Jumlah evaluasi mata kuliah semester 2 (2)", 0, 10, 0, step=1
)

# 10. Admission grade:
admission_grade = st.slider(
    "Nilai rata-rata masuk (Admission Grade)", 0.0, 200.0, 0.0, step=0.1
)

# 11. Scholarship holder:
# Sesuai deskripsi: 1 – yes, 0 – no
scholarship_options = ["1 - Yes", "0 - No"]
scholarship_holder = st.selectbox("Penerima beasiswa?", scholarship_options)

# 12. Previous qualification grade:
previous_qualification_grade = st.slider(
    "Nilai kualifikasi sebelumnya", 0.0, 200.0, 0.0, step=0.1
)

# 13. Application mode:
# Sesuai deskripsi berikut:
application_mode_options = [
    "1 - 1st phase - general contingent",
    "2 - Ordinance No. 612/93",
    "5 - 1st phase - special contingent (Azores Island)",
    "7 - Holders of other higher courses",
    "10 - Ordinance No. 854-B/99",
    "15 - International student (bachelor)",
    "16 - 1st phase - special contingent (Madeira Island)",
    "17 - 2nd phase - general contingent",
    "18 - 3rd phase - general contingent",
    "26 - Ordinance No. 533-A/99, item b2) (Different Plan)",
    "27 - Ordinance No. 533-A/99, item b3 (Other Institution)",
    "39 - Over 23 years old",
    "42 - Transfer",
    "43 - Change of course",
    "44 - Technological specialization diploma holders",
    "51 - Change of institution/course",
    "53 - Short cycle diploma holders",
    "57 - Change of institution/course (International)"
]
application_mode = st.selectbox("Mode pendaftaran (Application Mode)", application_mode_options)

# 14. Curricular_units_2nd_sem_enrolled:
curricular_units_2nd_sem_enrolled = st.slider(
    "Jumlah mata kuliah semester 2 yang diambil", 0, 20, 0, step=1
)

# 15. Father's Occupation:
# Sesuai deskripsi berikut:
fathers_occupation_options = [
    "0 - Student",
    "1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    "2 - Specialists in Intellectual and Scientific Activities",
    "3 - Intermediate Level Technicians and Professions",
    "4 - Administrative staff",
    "5 - Personal Services, Security and Safety Workers and Sellers",
    "6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    "7 - Skilled Workers in Industry, Construction and Craftsmen",
    "8 - Installation and Machine Operators and Assembly Workers",
    "9 - Unskilled Workers",
    "10 - Armed Forces Professions",
    "90 - Other Situation",
    "99 - (blank)",
    "101 - Armed Forces Officers",
    "102 - Armed Forces Sergeants",
    "103 - Other Armed Forces personnel",
    "112 - Directors of administrative and commercial services",
    "114 - Hotel, catering, trade and other services directors",
    "121 - Specialists in the physical sciences, mathematics, engineering and related techniques",
    "122 - Health professionals",
    "123 - teachers",
    "124 - Specialists in finance, accounting, administrative organization, public and commercial relations",
    "131 - Intermediate level science and engineering technicians and professions",
    "132 - Technicians and professionals, of intermediate level of health",
    "134 - Intermediate level technicians from legal, social, sports, cultural and similar services",
    "135 - Information and communication technology technicians",
    "141 - Office workers, secretaries in general and data processing operators",
    "143 - Data, accounting, statistical, financial services and registry-related operators",
    "144 - Other administrative support staff",
    "151 - personal service workers",
    "152 - sellers",
    "153 - Personal care workers and the like",
    "154 - Protection and security services personnel",
    "161 - Market-oriented farmers and skilled agricultural and animal production workers",
    "163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    "171 - Skilled construction workers and the like, except electricians",
    "172 - Skilled workers in metallurgy, metalworking and similar",
    "174 - Skilled workers in electricity and electronics",
    "175 - Workers in food processing, woodworking, clothing and other industries and crafts",
    "181 - Fixed plant and machine operators",
    "182 - assembly workers",
    "183 - Vehicle drivers and mobile equipment operators",
    "192 - Unskilled workers in agriculture, animal production, fisheries and forestry",
    "193 - Unskilled workers in extractive industry, construction, manufacturing and transport",
    "194 - Meal preparation assistants",
    "195 - Street vendors (except food) and street service providers"
]
fathers_occupation = st.selectbox("Pekerjaan ayah", fathers_occupation_options)

# --- Membuat DataFrame ---
input_dict = {
    "Curricular_units_2nd_sem_approved": [curricular_units_2nd_sem_approved],
    "Curricular_units_1st_sem_approved": [curricular_units_1st_sem_approved],
    "Curricular_units_2nd_sem_grade": [curricular_units_2nd_sem_grade],
    "Curricular_units_1st_sem_grade": [curricular_units_1st_sem_grade],
    "Tuition_fees_up_to_date": [tuition_fees_up_to_date],
    "Curricular_units_2nd_sem_evaluations": [curricular_units_2nd_sem_evaluations],
    "Age_at_enrollment": [age_at_enrollment],
    "Course": [course],
    "Curricular_units_2nd_sem_evaluations_2": [curricular_units_2nd_sem_evaluations_2],
    "Admission_grade": [admission_grade],
    "Scholarship_holder": [scholarship_holder],
    "Previous_qualification_grade": [previous_qualification_grade],
    "Application_mode": [application_mode],
    "Curricular_units_2nd_sem_enrolled": [curricular_units_2nd_sem_enrolled],
    "Fathers_occupation": [fathers_occupation]
}

input_df = pd.DataFrame(input_dict)

# --- One-Hot Encoding ---
input_df_encoded = pd.get_dummies(input_df)

# Pastikan kolom yang diharapkan oleh model ada (jika model memiliki atribut feature_names_in_)
model_features = (
    model.feature_names_in_
    if hasattr(model, "feature_names_in_")
    else input_df_encoded.columns
)
for col in model_features:
    if col not in input_df_encoded.columns:
        input_df_encoded[col] = 0
input_df_encoded = input_df_encoded[model_features]

# --- Prediksi ---
if st.button("Prediksi Status Mahasiswa"):
    pred = model.predict(input_df_encoded)[0]
    
    # Mapping hasil prediksi:
    if pred == 1:
        result = "Graduated"
    elif pred == 0:
        result = "Dropout"
    else:
        result = str(pred)
        
    st.success(f"Hasil Prediksi: Mahasiswa diprediksi akan **{result}**.")
