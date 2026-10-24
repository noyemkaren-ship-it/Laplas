<%inherit file="base.mako"/>
<%def name="title()">New Lesson — Admin — Laplas</%def>

<section class="auth-wrap">
    <div class="auth-card" style="max-width:640px;">
        <h1>New Lesson</h1>
        <p class="auth-sub">Create a lesson. HTML is allowed in the content field.</p>

        % if error:
        <div style="background:rgba(255,90,122,.1); border:1px solid rgba(255,90,122,.4); color:#ff5a7a; padding:12px 16px; border-radius:10px; margin-bottom:20px; font-size:14px;">
            ${error}
        </div>
        % endif

        <form method="POST" action="/admin_panel/lesson/new" class="auth-form">

            <label>Name
                <input name="name" required value="${form.get('name', '')}"
                       placeholder="Introduction to English"/>
            </label>

            <div style="display:grid; grid-template-columns:1fr 120px; gap:12px;">
                <label>Subject
                    <input name="subject" required value="${form.get('subject', '')}"
                           placeholder="English"/>
                </label>
                <label>Num
                    <input name="num" type="number" min="1" required value="${form.get('num', '')}"
                           placeholder="1"/>
                </label>
            </div>

            <label>Type
                <select name="lesson_type"
                        style="padding:12px 16px; border-radius:10px; background:rgba(255,255,255,.04); border:1px solid var(--border); color:var(--text); font-size:15px; font-family:inherit;">
                    <option value="text" ${'selected' if form.get('lesson_type') == 'text' else ''}>text</option>
                    <option value="test" ${'selected' if form.get('lesson_type') == 'test' else ''}>test</option>
                    <option value="video" ${'selected' if form.get('lesson_type') == 'video' else ''}>video</option>
                </select>
            </label>

            <label>Lesson HTML
                <textarea name="lesson_html" required rows="12"
                          style="padding:12px 16px; border-radius:10px; background:rgba(255,255,255,.04); border:1px solid var(--border); color:var(--text); font-size:14px; font-family:'SF Mono', Monaco, monospace; resize:vertical;"
                          placeholder="&lt;h2&gt;Title&lt;/h2&gt;&lt;p&gt;Content...&lt;/p&gt;">${form.get('lesson_html', '')}</textarea>
            </label>

            <div style="display:flex; gap:12px; margin-top:8px;">
                <button type="submit" class="btn-primary btn-lg" style="flex:1;">Create Lesson</button>
                <a href="/admin_panel?tab=lessons" class="btn-outline btn-lg">Cancel</a>
            </div>
        </form>
    </div>
</section>