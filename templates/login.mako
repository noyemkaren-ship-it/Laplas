<%inherit file="base.mako"/>
<%def name="title()">Sign In — Laplas</%def>

<section class="auth-wrap">
    <div class="auth-card">
        <h1>Welcome back</h1>
        <p class="auth-sub">Sign in to continue your learning journey.</p>
        <form id="login-form" class="auth-form">
            <label>Email
                <input type="email" name="email" required placeholder="you@example.com"/>
            </label>
            <label>Password
                <input type="password" name="password" required placeholder="••••••••"/>
            </label>
            <button type="submit" class="btn-primary btn-lg">Sign In</button>
            <p class="auth-switch">No account? <a href="/register">Create one</a></p>
        </form>
    </div>
</section>

<script>
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    const body = { email: fd.get('email'), password: fd.get('password') };
    const res = await fetch('/user/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
        body: JSON.stringify(body)
    });
    if (res.ok) window.location.href = '/profile';
    else alert('Invalid email or password');
});
</script>