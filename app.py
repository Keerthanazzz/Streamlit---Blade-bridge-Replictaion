import streamlit as st
import base64
import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store feedback data
if 'feedback_data' not in st.session_state:
    st.session_state.feedback_data = pd.DataFrame(columns=["timestamp", "fname", "lname", "company", "phone", "email", "message"])

# Function to convert image to base64
def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return ""
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return ""

# Hide 'Request Demo' from the default Streamlit menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Load images and convert to base64
icon_path = 'C:/Users/Keerthana/Downloads/Bladebridge_yellow_NEW-removebg-preview.png'
base64_icon = image_to_base64(icon_path)
image_path_studio = 'C:/Users/Keerthana/Downloads/images_1-removebg-preview.png'
image_path_warehousing = 'C:/Users/Keerthana/Downloads/data-warehousing1.png'
image_path_onboarding = 'C:/Users/Keerthana/Downloads/R-removebg-preview.png'
image_path_data_vault = 'C:/Users/Keerthana/Downloads/2.png'
base64_image_studio = image_to_base64(image_path_studio)
base64_image_warehousing = image_to_base64(image_path_warehousing)
base64_image_onboarding = image_to_base64(image_path_onboarding)
base64_image_data_vault = image_to_base64(image_path_data_vault)
background_image_path = 'C:/Users/Keerthana/Downloads/bg.jpeg'
base64_background_image = image_to_base64(background_image_path)

# Navigation bar with image on top left
st.markdown(f"""
    <style>
        .navbar-container {{
            position: relative;
            padding: 2px;
        }}
        .navbar-icon {{
            position: absolute;
            top: -20px;
            left: 0;
            height: 80px; /* Adjust size as needed */
            width: auto; /* Maintain aspect ratio */
        }}
        .request-demo {{
            position: absolute;
            top: 0;
            right: 0;
            padding: 10px 20px;
            background-color: #f7c10b; /* Mustard yellow */
            color: white; /* Text color */
            border-radius: 25px;
            text-decoration: none;
            font-size: 18px;
            margin-top: 10px; /* Adjust margin to position correctly */
            margin-right: 10px; /* Adjust margin to position correctly */
        }}
        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background-color: #f8f9fa;
            background-image: url('data:image/jpeg;base64,{base64_background_image}'); /* Base64 encoded image */
            background-size: cover; /* Cover the entire area */
            background-position: center; /* Center the background image */
            margin-top: 80px; /* Adjust margin to accommodate the increased image size */
        }}
        .navbar-center {{
            display: flex;
            justify-content: center;
            flex-grow: 1;
        }}
        .navbar-center a {{
            color: black;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
            position: relative;
            padding-bottom: 5px;
        }}
        .navbar-center a:after {{
            content: "";
            display: block;
            width: 100%;
            height: 2px;
            background-color: #f7c10b; /* Mustard yellow */
            position: absolute;
            left: 0;
            bottom: 0;
            transform: scaleX(0);
            transform-origin: bottom right;
            transition: transform 0.3s ease;
        }}
        .navbar-center a:hover:after {{
            transform: scaleX(1);
            transform-origin: bottom left;
        }}
        .dropdown {{
            position: relative;
            display: inline-block;
        }}
        .dropdown-content {{
            display: none;
            position: absolute;
            background-color: #d2b48c; /* Light brown */
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }}
        .dropdown-content a {{
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }}
        .dropdown:hover .dropdown-content {{
            display: block;
        }}
        .content {{
            display: flex;
            align-items: center;
            gap: 20px;
            margin-top: 30px;
        }}
        .content img {{
            width: 40%; /* Adjust width to fit content */
            height: auto;
        }}
        .content div {{
            flex-grow: 1;
            text-align: justify; /* Justify text */
        }}
        .content h3 {{
            position: relative;
            padding-bottom: 15px; /* Add space for line */
        }}
        .content h3::after {{
            content: "";
            display: block;
            width: 100%;
            height: 2px;
            background-color: #f7c10b; /* Mustard yellow */
            position: absolute;
            left: 0;
            bottom: 0;
        }}
        .data-warehousing {{
            display: flex;
            align-items: center;
            gap: 20px;
            margin-top: 30px;
            /* Removed background-color setting */
        }}
        .data-warehousing div {{
            flex-grow: 1;
        }}
        .data-warehousing img {{
            width: 40%; /* Adjust width to fit content */
            height: auto;
        }}
        .onboarding-container {{
            display: flex;
            align-items: center;
            gap: 20px;
            padding: 20px;
            margin-top: 30px;
        }}
        .onboarding-container img {{
            width: 40%; /* Adjust width to fit content */
            height: auto;
        }}
        .onboarding-container div {{
            flex-grow: 1;
            text-align: justify; /* Justify text */
        }}
        .data-vault-container {{
            display: flex;
            align-items: center;
            gap: 20px;
            padding: 20px;
            margin-top: 30px;
        }}
        .data-vault-container img {{
            width: 40%; /* Adjust width to fit content */
            height: auto;
        }}
        .data-vault-container div {{
            flex-grow: 1;
            text-align: justify; /* Justify text */
        }}
        .contact-container {{
            display: flex;
            align-items: flex-start;
            gap: 20px;
            margin-top: 30px;
        }}
        .contact-container div {{
            flex-grow: 1;
        }}
        .contact-container form {{
            flex-grow: 1;
            background-color: #36454f; /* Dark slate gray background */
            padding: 20px;
            border-radius: 10px;
            color: white; /* Text color */
            border: none; /* Remove border */
        }}
        .studio-title {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80px; /* Adjust height to match navigation bar size */
            background-image: url('data:image/jpeg;base64,{base64_background_image}'); /* Base64 encoded background image */
            background-size: cover;
            background-position: center;
            color: white; /* white text */
            font-size: 30px; /* Adjust font size as needed */
            font-weight: bold;
        }}
        .footer {{
            margin-top: 30px;
            text-align: center;
        }}
        .footer .social-media-icons {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }}
        .footer .social-media-icons a {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: #f7c10b; /* Mustard yellow background */
            color: black; /* Icon color */
            font-size: 20px;
            text-decoration: none;
        }}
        .video-container {{
            margin-top: 30px;
            display: flex;
            justify-content: center;
        }}
        .video-container iframe {{
            width: 100%;
            height: 500px; /* Adjust height as needed */
        }}
        .feedback-form {{
            background-color: #36454f; /* Dark slate gray background */
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            color: white; /* Text color */
            border: none; /* Remove border */
        }}
    </style>
    <div class="navbar-container">
        <img src="data:image/png;base64,{base64_icon}" class="navbar-icon" alt="BladeBridge Icon">
        <a class="request-demo" href="?page=request-demo">iuiuyugv</a>
        <div class="navbar">
            <div class="navbar-center">
                <a href="?page=home">uyrefji</a>
                <div class="dropdown">
                    <a href="?page=products">uikmhtgf</a>
                    <div class="dropdown-content">
                        <a href="?page=analyzer">hbhbfkjnrf</a>
                        <a href="?page=converter">hkjfhkjfr</a>
                        <a href="?page=data-recon">hkjfhhrk</a>
                        <a href="?page=studio">tereytryu</a>
                    </div>
                </div>
                <a href="?page=contact">fdbmnkl</a>
                <a href="?page=partner-portal">nbvcbvbv</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Check the URL fragment to display the appropriate content
page = st.query_params.get("page", ["home"])[0]

# Add the Studio title with the background image
if page == "home":
    st.markdown("""
    <div class="studio-title">
       Phasellus
    </div>
    """, unsafe_allow_html=True)

    # Add the rest of the home page content
    st.markdown(f"""
    <div class="content">
        <img src="data:image/png;base64,{base64_image_studio}" alt="Studio Image">
        <div>
            <h3>euismod sagittis</h3>
            <p>
            Ut interdum sollicitudin lectus a ultricies. Nam cursus faucibus elit, vel convallis justo accumsan sed. Phasellus interdum lectus elit, ut molestie diam efficitur et. Maecenas quis facilisis turpis. Sed at finibus nulla. Proin eu diam elementum, semper libero sit amet, vehicula lorem. Etiam non tellus nisi. 
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Add Data Warehousing section
    st.markdown(f"""
    <div class="data-warehousing">
        <div>
            <h3> posuere era</h3>
            <p>
            molestie sodales nisi. In vitae massa ut eros finibus auctor. Aliquam erat volutpat. Nullam sed dictum est, quis molestie massa. Vestibulum id urna libero. Nam luctus laoreet tristique. Nulla faucibus, libero in ultricies rhoncus, nulla mi convallis velit, malesuada condimentum ipsum velit id augue
            </p>
        </div>
        <img src="data:image/png;base64,{base64_image_warehousing}" alt="Data Warehousing Image">
    </div>
    """, unsafe_allow_html=True)

    # Add YouTube video
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/SBodImQVr6A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # Add On-boarding Data section
    st.markdown(f"""
    <div class="onboarding-container">
        <img src="data:image/png;base64,{base64_image_onboarding}" alt="Onboarding Data Image">
        <div>
            <h3>molestie sodales nisi</h3>
            <p>Ut ac consectetur urna, sed convallis dolor. Phasellus libero diam, tempus varius blandit sit amet, bibendum vel velit. Donec rhoncus, elit at lobortis aliquet, neque magna malesuada ex, eget suscipit eros libero ac arcu. Quisque egestas diam quis aliquet volutpat. Quisque quis justo orci.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Add Data Vault section
    st.markdown(f"""
    <div class="bdfkjhfklgkll,g">
        <div>
            <h3>Quisque</h3>
            <p>
             Nulla ac molestie orci, egestas vehicula est. Donec tincidunt libero ut pharetra euismod. Morbi ut molestie nibh, dapibus finibus quam. Vivamus semper, ligula id euismod sagittis, urna massa porta metus, et pretium eros lacus vehicula dolor. Nam pellentesque mi sit amet nibh scelerisque, sit amet pellentesque tellus vulputate.
            </p>
        </div>
        <img src="data:image/png;base64,{base64_image_data_vault}" alt="Data Vault Image">
    </div>
    """, unsafe_allow_html=True)

    # Add Feedback Form and Contact Information
with st.form(key='feedback_form', clear_on_submit=True):
    st.markdown('<div class="feedback-form">', unsafe_allow_html=True)
    st.markdown("""
    <h3>Feedback Form</h3>
    """, unsafe_allow_html=True)
    fname = st.text_input("First name")
    lname = st.text_input("Last name")
    company = st.text_input("Company name")
    phone = st.text_input("Phone number")
    email = st.text_input("Company Email")
    message = st.text_area("Your message")
    
    submit_button = st.form_submit_button("Send Feedback")

    if submit_button:
        # Extract form data
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fname": fname,
            "lname": lname,
            "company": company,
            "phone": phone,
            "email": email,
            "message": message
        }
        # Save feedback to dataframe
        st.session_state.feedback_data = pd.concat([st.session_state.feedback_data, pd.DataFrame([data])], ignore_index=True)
        st.success("Feedback submitted successfully!")

    elif page == "studio":
        st.markdown("<h2 style='text-align: center;'>Studio</h2>", unsafe_allow_html=True)
        
# Add social media icons at the bottom center
st.markdown("""
    <div class="footer">
        <div class="social-media-icons">
            <a href="https://www.google.com" target="_blank" title="Google">G</a>
            <a href="https://www.facebook.com" target="_blank" title="Facebook">F</a>
            <a href="https://www.linkedin.com" target="_blank" title="LinkedIn">L</a>
            <a href="https://www.instagram.com" target="_blank" title="Instagram">I</a>
        </div>
    </div>
""", unsafe_allow_html=True)
