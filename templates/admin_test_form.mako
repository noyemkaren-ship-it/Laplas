<%inherit file="base.mako"/>
<%def name="title()">New Test — Admin — Laplas</%def>

<section class="auth-wrap">
    <div class="auth-card" style="max-width:560px;">
        <h1>New Test</h1>
        <p class="auth-sub">Create a question. Answer is compared as-is.</p>

        % if error:
        <div style="background:rgba(255,90,122,.1); border:1px solid rgba(255,90,122,.4); color:#ff5a7a; padding:12px 16px; border-radius:10px; margin-bottom:20px; font-size:14px;">
            ${error}
        </div>
        % endif

        <form method="POST" action="/admin_panel/test/new" class="auth-form">

            <label>Subject
                <input name="subject" required value="${form.get('subject', '')}"
                       placeholder="English"/>
            </label>

            <label>Question
                <input name="question" required value="${form.get('question', '')}"
                       placeholder="What is the first letter of the English alphabet?"/>
            </label>

            <label>Answer
                <input name="answer" required value="${form.get('answer', '')}"
                       placeholder="A"/>
            </label>

            <div style="display:flex; gap:12px; margin-top:8px;">
                <button type="submit" class="btn-primary btn-lg" style="flex:1;">Create Test</button>
                <a href="/admin_panel?tab=tests" class="btn-outline btn-lg">Cancel</a>
            </div>
        </form>
    </div>
</section>