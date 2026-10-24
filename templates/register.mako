<%inherit file="base.mako"/>
<%def name="title()">Create Account — Laplas</%def>

<section class="auth-wrap">
    <div class="auth-card">
        <h1>Create your account</h1>
        <p class="auth-sub">Join Laplas and start mastering subjects.</p>
        <form id="register-form" class="auth-form">
            <label>Name <input name="name" required/></label>
            <label>Email <input type="email" name="email" required/></label>
            <label>Phone <input name="num" required placeholder="+7 ..."/></label>
            <label>Age <input type="number" name="age" min="0" max="80" required/></label>
            <label>Password <input type="password" name="password" required/></label>
            <button type="submit" class="btn-primary btn-lg">Create Account</button>
            <p class="auth-switch">Already registered? <a href="/login">Sign in</a></p>
        </form>
    </div>
</section>

<script>
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    const body = {
        name: fd.get('name'), email: fd.get('email'),
        num: fd.get('num'), age: Number(fd.get('age')),
        password: fd.get('password')
    };
    const res = await fetch('/user/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
        body: JSON.stringify(body)
    });
    if (res.ok) window.location.href = '/profile';
    else alert('Registration failed. Try a different email/name.');
});
</script>