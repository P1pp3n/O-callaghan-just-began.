<!-- index.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment Help Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <img src="logo.png" alt="Assignment Help Services Logo">
            </div>
            <nav>
                <ul>
                    <li><a href="Services.html">Services</a></li>
                    <li><a href="aboutus.html">About Us</a></li>
                    <li><a href="testimonials.html">Testimonials</a></li>
                    <li><a href="contacts.html">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="banner">
        <div class="container">
            <h1>Expert Assignment Help Across IT, Medicine, Engineering, and Literature</h1>
            <p>Your gateway to academic success!</p>
            <a href="#contact" class="btn">Get Started</a>
        </div>
    </section>

    <section id="services">
        <?php include 'services.html'; ?>
    </section>

    <section id="about">
        <?php include 'about.html'; ?>
    </section>

    <section id="testimonials">
        <?php include 'testimonials.html'; ?>
    </section>

    <section id="contact">
        <?php include 'contact.html'; ?>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Assignment Help Services</p>
        </div>
    </footer>
</body>
</html>
