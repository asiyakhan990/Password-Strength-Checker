import streamlit as st
import string

def check_password_strength(password):
    strength = 0
    remarks = "🔴 Weak"
    feedback = ""
    
  
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1
    
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    
    
    if any(char.isdigit() for char in password):
        strength += 1
    
    
    if any(char in string.punctuation for char in password):
        strength += 1
    
    
    if strength <= 2:
        remarks = "🔴 Weak"
    elif strength == 3:
        remarks = "🟡 Moderate"
    elif strength == 4:
        remarks = "🟢 Strong"
        feedback = "✅ Your password is strong! However, adding more length and variety can make it even better."
    elif strength == 5:
        remarks = "🔵 Very Strong"
        feedback = "🎉Excellent! Your password meets the highest security standards. Ensure you store it safely and use unique passwords for different accounts."
    
    return strength, remarks, feedback


st.set_page_config(page_title="Ultimate Password Strength Checker", page_icon="🔐")
st.title("🔐 Ultimate Password Strength Checker")
st.write("Ensure your password is strong and secure! Enter your password below to evaluate its strength.")

password = st.text_input("🔑 Enter Password", type="password")

if st.button("Check Strength"):
    if password:
        strength, remarks, feedback = check_password_strength(password)
        
        st.subheader(f"**Password Strength:** {remarks}")
        st.progress(strength / 5)
        
        if feedback:
            st.success(feedback)
        elif strength < 5:
            st.warning("⚠️ Consider using a longer password with uppercase, lowercase, digits, and special characters for better security.")
# 🌟 Footer
st.markdown("""
---
Made with ❤️ by **Kaladi Developer**  
""")