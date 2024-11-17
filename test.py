from IPython.core.display import display, HTML

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jalur5</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f5f5;
        }

        header {
            background: #0d6efd;
            color: white;
            text-align: center;
            padding: 20px 0;
        }

        main {
            padding: 20px;
            max-width: 800px;
            margin: auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        section {
            margin-bottom: 20px;
        }

        h2 {
            color: #0d6efd;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        ul li {
            margin: 10px 0;
        }

        footer {
            text-align: center;
            background: #0d6efd;
            color: white;
            padding: 10px 0;
            margin-top: 20px;
            position: relative;
        }

        a {
            color: #0d6efd;
            text-decoration: none;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Jalur5</h1>
        <p>Your Mobility and Transportation Hub</p>
    </header>
    <main>
        <section>
            <h2>About Jalur5</h2>
            <p>Jalur5 provides reliable information about public transportation in Jakarta, Depok, Bogor, Bekasi, and Tangerang. Join us in making commuting easier!</p>
        </section>
        <section>
            <h2>Follow Us</h2>
            <ul id="social-links">
                <li><a href="https://www.youtube.com/@Jalur5" target="_blank">YouTube</a></li>
                <li><a href="https://www.instagram.com/jalur5" target="_blank">Instagram</a></li>
                <li><a href="https://www.tiktok.com/@jalur5" target="_blank">TikTok</a></li>
                <li><a href="https://linktr.ee/jalur5" target="_blank">Linktree</a></li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Jalur5. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

# Display the website result
display(HTML(html_content))
