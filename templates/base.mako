<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>${self.title()}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css"/>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
<canvas id="bg-canvas"></canvas>

<nav class="navbar">
    <a class="logo" href="/">
        <span class="logo-mark">◈</span>
        <span class="logo-text">Laplas</span>
    </a>
    <div class="nav-links">
        <a href="/lessons">Lessons</a>
        <a href="/tests">Tests</a>
        <a href="/subjects">Subjects</a>
        % if user and user.admin:
            <a href="/admin_panel">Admin</a>
        % endif
        <a href="/private-tutors">Private Tutors</a>
    </div>
    <div class="nav-user">
        % if user:
            <a href="/profile" class="nav-profile">
                <span class="xp-badge">⚡ ${user.xp or 0} XP</span>
                <span class="avatar">${user.name[0].upper()}</span>
            </a>
        % else:
            <a href="/login" class="btn-ghost">Sign in</a>
            <a href="/register" class="btn-primary">Get Started</a>
        % endif
    </div>
</nav>

<main class="page">
    ${self.body()}
</main>

<footer class="footer">
    <p>© Laplas — Learn deeper. Think sharper.</p>
</footer>

<script src="/static/js/main.js"></script>
</body>
</html>

<%def name="title()">Laplas</%def>