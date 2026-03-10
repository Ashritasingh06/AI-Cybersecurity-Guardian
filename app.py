import streamlit as st

st.title("AI Personal Cybersecurity Guardian")

message = st.text_area("Enter email or message to analyze")

if st.button("Analyze"):

    suspicious_words = ["urgent","click","verify","password","bank","login"]

    risk = False

    for word in suspicious_words:
        if word in message.lower():
            risk = True

    if risk:
        st.error("⚠️ Potential Phishing Detected")
        st.write("This message contains suspicious keywords often used in phishing attacks.")
        st.write("Advice: Do not click unknown links or share personal information.")
    else:
        st.success("Message appears safe.")