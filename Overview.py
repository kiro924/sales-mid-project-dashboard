
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Overview Page',
                  page_icon='🪙')
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: green;">Overview Of Top Profits In Sales Dataset</h1>
    </div>
""", unsafe_allow_html=True)
a, b, c = st.columns(3)

st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: green;">Overview Of Top Returns In Sales Dataset</h1>
    </div>
""", unsafe_allow_html=True)



a.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">Total Profit</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{48356299:,}</p>
    </div>
""", unsafe_allow_html=True)

b.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">North America</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{18871555:,}</p>
    </div>
""", unsafe_allow_html=True)

c.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">United States</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{15335141:,}</p>
    </div>
""", unsafe_allow_html=True)

a.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">Australia</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{14177206:,}</p>
    </div>
""", unsafe_allow_html=True)

b.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">December</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{8244480:,}</p>
    </div>
""", unsafe_allow_html=True)

c.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">Saturday</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{7092825:,}</p>
    </div>
""", unsafe_allow_html=True)

x, y, z = st.columns(3)

x.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">Spring</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{14495966:,}</p>
    </div>
""", unsafe_allow_html=True)

y.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">May</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{5523120:,}</p>
    </div>
""", unsafe_allow_html=True)

z.markdown(f"""
    <div style="background-color:#f5fffa; padding: 10px; border-radius: 10px;width: 50%; max-width: 300px;">
        <h3 style="color:#008080;">Monday</h3>
        <p style="font-size: 30px; color:#008080; font-weight: bold;">{8369875:,}</p>
    </div>
""", unsafe_allow_html=True)
