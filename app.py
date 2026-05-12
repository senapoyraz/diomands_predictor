import streamlit as st
import numpy as np
import pickle

# Modeli yükle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Encoding sıralamaları
cut_order     = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_order   = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

st.title("💎 Elmas Fiyat Tahmini")
st.write("Elmasın özelliklerini gir, tahmini fiyatı öğren.")

st.divider()

# Kullanıcı girişleri
col1, col2 = st.columns(2)

with col1:
    carat   = st.number_input("Karat (ağırlık)", min_value=0.2, max_value=5.0, value=1.0, step=0.01)
    cut     = st.selectbox("Kesim Kalitesi", cut_order)
    color   = st.selectbox("Renk (D en iyi)", color_order[::-1])

with col2:
    clarity = st.selectbox("Berraklık (IF en iyi)", clarity_order[::-1])
    depth   = st.number_input("Derinlik (%)", min_value=43.0, max_value=79.0, value=61.7, step=0.1)
    table   = st.number_input("Table (%)", min_value=43.0, max_value=95.0, value=57.0, step=0.1)

st.divider()

# Tahmin butonu
if st.button("💰 Fiyatı Tahmin Et", use_container_width=True):
    cut_enc     = cut_order.index(cut)
    color_enc   = color_order.index(color)
    clarity_enc = clarity_order.index(clarity)

    features = np.array([[carat, cut_enc, color_enc, clarity_enc, depth, table]])
    tahmin   = model.predict(features)[0]

    st.success(f"### Tahmini Fiyat: ${tahmin:,.0f}")
