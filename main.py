import streamlit as st
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="centered")

if "step" not in st.session_state:
    st.session_state.step = 0
if "done" not in st.session_state:
    st.session_state.done = False
if "sub_step" not in st.session_state:
    st.session_state.sub_step = 0
if "final_step" not in st.session_state:
    st.session_state.final_step = False
if "final_single" not in st.session_state:
    st.session_state.final_single = False  # show only the last sub-step button

yes_texts = [
    "Yes",
    "စိတ်ဆိုးပါနဲ့",
    "စိတ်ဆိုးမပြေသေးတာ သေချာပြီပေါ့",
    "စိတ်ဆိုးတဲ့သူ အီးရှု 😝"
]

sub_texts = [
    "စိတ်ဆိုးရတော့ဘူးလေနော်",
    "ဟာ အဲ့လိုဆိုးရဘူးလေ",
    "ဒါလဲ No ပဲ"
]

st.markdown("<br>", unsafe_allow_html=True)

if st.session_state.done:
    st.image(
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        caption="Me non-stop typing to chort you",
        use_container_width=True
    )
    st.markdown(
        "<h3 style='text-align:center;'>yayyyyyyyyyyyyyyy sate ma soe tok wo lo thet mtt lyk b nor</h3>",
        unsafe_allow_html=True
    )
    st.stop()

st.image(
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    use_container_width=True
)

st.markdown(
    "<h2 style='text-align:center;'>စိတ်ဆိုးနေတုန်းပဲလား ဆရာမကြီး 🥺</h2>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

if not st.session_state.final_single:
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.step < len(yes_texts) - 1:
            if st.button(yes_texts[st.session_state.step], key="yes_button"):
                st.session_state.step += 1
                st.rerun()
        else:
            if st.session_state.sub_step < len(sub_texts):
                if st.button(sub_texts[st.session_state.sub_step], key=f"sub_{st.session_state.sub_step}"):
                    st.session_state.sub_step += 1
                    if st.session_state.sub_step == len(sub_texts):
                        st.session_state.final_single = True
                    st.rerun()

    with col2:
        if st.button("No", key="no_button"):
            st.session_state.done = True
            st.rerun()
else:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    if st.button("ဒါလဲ No ပဲ", key="final_no"):
        st.session_state.done = True
        st.rerun()
