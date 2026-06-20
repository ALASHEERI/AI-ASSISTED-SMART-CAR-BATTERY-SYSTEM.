import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI-Assisted Smart Car Battery System",
    page_icon="🔋",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/uob.png", width=120)

with col2:
    st.title("🔋 AI-Assisted Smart Car Battery System")

    st.write("University of Bahrain")
    st.write("Department of Electrical and Electronics Engineering")
    st.write("Senior Design Project 2026")

st.markdown("---")

# ==========================================
# TEAM & SUPERVISOR
# ==========================================

st.subheader("Project Team")

st.write("""
Mohamed Jaber Al-Asheeri

Ahmed Jaber Busafwan

Jaafar AbdulJalil Al-Shaikh Yousif
""")

st.write("**Supervisor:** Dr. Mohammed Al Khaldi")

st.markdown("---")

# ==========================================
# VIDEO
# ==========================================

st.header("🎥 Project Demonstration")

st.video("assets/intro.mp4")

st.markdown("---")

# ==========================================
# WHY DO VEHICLE BATTERIES FAIL?
# ==========================================

st.header("🚗 Why Do Vehicle Batteries Fail?")

st.write("""
Vehicle battery failure is one of the most common causes of unexpected vehicle breakdowns.

Major causes include battery aging, parasitic electrical loads, human error,
poor charging conditions, unsafe jump-starting practices, and high accessory load demand.
""")

st.image(
    "assets/causes.png",
    use_container_width=True
)

st.markdown("---")

# ==========================================
# IMPACT ON DRIVERS
# ==========================================

st.header("⚠️ Impact on Drivers")

c1, c2, c3 = st.columns(3)

with c1:
    st.warning("🚗 Vehicle Won't Start")

with c2:
    st.warning("💰 Towing Costs")

with c3:
    st.warning("⏰ Delays & Lost Time")

c4, c5, c6 = st.columns(3)

with c4:
    st.warning("🔋 Battery Replacement")

with c5:
    st.warning("⚡ Electrical Problems")

with c6:
    st.warning("🛑 Safety Concerns")
    st.markdown("---")

# ==========================================
# OUR SOLUTION
# ==========================================

st.header("💡 Our Solution")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🔋 Battery Monitoring")

with c2:
    st.success("📡 IoT Dashboard")

with c3:
    st.success("⚡ Jump Assist")

with c4:
    st.success("🧠 AI Prediction")

st.markdown("---")

# ==========================================
# PROJECT OBJECTIVES
# ==========================================

st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("🔋 Monitor Main Battery Voltage")
    st.success("⚡ Detect Abnormal Current Drain")
    st.success("📊 Estimate SOC and SOH")
    st.success("🚨 Provide Early Warning Alerts")

with col2:
    st.success("🔌 Control Non-Essential Loads")
    st.success("📡 Enable IoT Monitoring")
    st.success("🚗 Provide Jump-Assist Support")
    st.success("🧠 Predict Battery Health Using AI")

st.markdown("---")

# ==========================================
# WHAT MAKES THIS PROJECT DIFFERENT?
# ==========================================

st.header("🏆 What Makes This Project Different?")

st.success("""
Most existing solutions focus on only one aspect of battery management,
such as monitoring, diagnostics, or prediction.

Our system integrates battery monitoring, load management,
leakage detection, controlled jump-assist functionality,
IoT remote monitoring, and AI-based battery health prediction
into a single intelligent platform.
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("🔋 Monitoring")

with c2:
    st.info("📡 IoT Connectivity")

with c3:
    st.info("🧠 AI Prediction")

c4, c5, c6 = st.columns(3)

with c4:
    st.info("⚡ Load Management")

with c5:
    st.info("🚨 Leakage Detection")

with c6:
    st.info("🚗 Jump Assist")
    st.markdown("---")

# ==========================================
# SYSTEM GALLERY
# ==========================================

st.header("📸 Hardware Prototype")

g1, g2 = st.columns(2)

st.image(
    "assets/prototype.png.jpg",
    caption="Hardware Prototype",
    use_container_width=True
)
st.markdown("---")

st.header("📱 IoT Dashboard")
st.image(
    "assets/dashboard.png.jpg",
    caption="IoT Monitoring Dashboard",
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI ANALYSIS
# ==========================================

st.header("🧠 AI-Based Battery Health Prediction")
g1, g2 = st.columns(2)

st.image(
    "assets/prediction.png.png",
    caption="Actual vs Predicted SOH",
    use_container_width=True
)
st.markdown("---")
st.image(
    "assets/forecast.png.png",
    caption="Battery Health Forecast",
    use_container_width=True
)
st.markdown("---")
st.image(
    "assets/importance.png.png",
    caption="Feature Importance Analysis",
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI PERFORMANCE
# ==========================================

# ==========================================
# AI PERFORMANCE
# ==========================================

st.markdown("---")

st.header("📊 AI Performance")

st.metric("R² Score", "0.998")

st.metric("MAE", "0.29%")

st.metric("Critical Cycle", "203")

st.metric("Remaining Cycles", "35")

st.success(
    "Gradient Boosting achieved the highest prediction accuracy and successfully forecasted the battery critical health threshold."
)

# ==========================================
# REAL-WORLD BENEFITS
# ==========================================


st.markdown("---")

st.header("🚘 Real-World Benefits")

st.info("🔋 Reduce Unexpected Battery Failures")

st.info("💰 Lower Maintenance Costs")

st.info("🚗 Improve Vehicle Reliability")

st.info("⚡ Prevent Battery Drain")

st.info("📡 Enable Continuous Monitoring")

st.info("🚨 Provide Early Failure Warnings")

# ==========================================
# FUTURE WORK
# ==========================================

st.header("🚀 Future Work")

st.write("""
Future development of the proposed system will focus on:

• Collecting real automotive battery data.

• Integrating AI directly into embedded controllers.

• Implementing adaptive AI-generated thresholds.

• Improving abnormal current drain detection.

• Integrating CAN Bus communication.

• Developing cloud-based analytics.

• Building a fully autonomous battery management platform.
""")
st.markdown("---")

# ==========================================
# PROJECT TEAM
# ==========================================

st.markdown("---")

st.header("👨‍💻 Meet The Team")

# ==========================================
# MOHAMED
# ==========================================

st.image(
    "assets/mohamed.jpg.jpg",
    width=250
)

st.subheader("Mohamed Jaber Al-Asheeri")

st.link_button(
    "💼 LinkedIn",
    "https://www.linkedin.com/in/asheeri/"
)

with open("assets/cv_mohamed.pdf.pdf", "rb") as file:
    st.download_button(
        "📄 View CV",
        file,
        file_name="Mohamed_Jaber_CV.pdf",
        mime="application/pdf",
        key="cv_mohamed"
    )

st.markdown("---")

# ==========================================
# AHMED
# ==========================================

st.image(
    "assets/Ahmed.jpg",
    width=250
)

st.subheader("Ahmed Jaber Busafwan")

st.link_button(
    "💼 LinkedIn",
    "https://www.linkedin.com/in/ahmed-busafwan-88283b357"
)

with open("assets/cv_ahmed.pdf", "rb") as file:
    st.download_button(
        "📄 View CV",
        file,
        file_name="Ahmed_Jaber_CV.pdf",
        mime="application/pdf",
        key="cv_ahmed"
    )

st.markdown("---")

# ==========================================
# JAAFAR
# ==========================================

st.image(
    "assets/jaffar.jpeg",
    width=250
)

st.subheader("Jaafar AbdulJalil Al-Shaikh Yousif")

st.link_button(
    "💼 LinkedIn",
    "https://linkedin.com/in/jaafar-abdulljalil-b83bbb3b0"
)

with open("assets/cv_jaffar.pdf", "rb") as file:
    st.download_button(
        "📄 View CV",
        file,
        file_name="Jaafar_CV.pdf",
        mime="application/pdf",
        key="cv_jaffar"
    )
# ==========================================
# ACKNOWLEDGEMENTS
# ==========================================

st.markdown("---")

st.header("🙏 Acknowledgements")

st.write("""
We would like to express our sincere gratitude to:

• Dr. Mohammed Al Khaldi for his continuous guidance, support, and valuable feedback throughout this project.

• The University of Bahrain for providing the academic environment and resources required for this work.

• The Department of Electrical and Electronics Engineering for their support during our undergraduate studies.
""")

# ==========================================
# SHARE YOUR THOUGHTS
# ==========================================

st.markdown("---")

st.header("💡 Future Improvements & Suggestions")

st.write(
    """
Have an idea that could improve this system?

We would love to hear your suggestions for future features and enhancements.
"""
)

st.link_button(
    "📝 Submit Your Suggestion",
    "https://docs.google.com/forms/d/e/1FAIpQLSeABh5i-aVtvRexjjt3Vce9xZw3ifjT8iLkHLq8yZrzKRqRtA/viewform?usp=publish-editor"
)