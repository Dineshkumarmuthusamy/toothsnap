import streamlit as st

st.markdown(
    """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ToothSnap - Your Dental Companion</title>
  <link rel="stylesheet" href="styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&amp;display=swap" rel="stylesheet">
</head>
<body>
  <header>
    <nav>
      <h1>ToothSnap</h1>
      <ul>
        <li>
          <a href="#features">Features</a>
        </li>
        <li>
          <a href="#about">About</a>
        </li>
        <li>
          <a href="#contact">Contact</a>
        </li>
      </ul>
    </nav>
  </header>
  <main>
    <section class="hero">
      <div class="hero-content">
        <h2>Your Dental Companion</h2>
        <p>Transforming dental care through technology and innovation.</p><a href="#features" class="cta-button">Discover More</a>
    </section>
    <section id="features" class="features">
      <h2>Features</h2>
      <div class="feature-item">
        <h3>Easy Appointment Scheduling</h3>
        <p>Manage your appointments seamlessly with our user-friendly interface.</p>
      </div>
      <div class="feature-item">
        <h3>Patient Management</h3>
        <p>Keep track of patient records and history effortlessly.</p>
      </div>
      <div class="feature-item">
        <h3>Treatment Plans</h3>
        <p>Create and share personalized treatment plans with your patients.</p>
      </div>
    </section>
    <section id="about" class="about">
      <h2>About Us</h2>
      <p>At ToothSnap, we are dedicated to enhancing the dental experience for both practitioners and patients. Our mission is to leverage technology to improve dental care and make it more accessible.</p>
    </section>
    <section id="contact" class="contact">
      <h2>Contact Us</h2>
      <p>If you have any questions or would like to learn more, feel free to reach out!</p>
      <form action="#" method="post">
        <label for="name">Name:</label> <input type="text" id="name" name="name" required=""> <label for="email">Email:</label> <input type="email" id="email" name="email" required=""> <label for="message">Message:</label> 
        <textarea id="message" name="message" rows="4" required=""></textarea> <button type="submit" class="cta-button">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>© 2023 ToothSnap. All rights reserved.</p>
  </footer>
</body>
</html>""",unsafe_allow_html=True
)
st.markdown(
    f"""
     <style>
     .stApp {{
         background: url("https://wallpapercave.com/wp/wp11901739.jpg");
         background-size: cover
     }}
     </style>
     """,
    unsafe_allow_html=True
)

