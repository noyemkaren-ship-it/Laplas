<%inherit file="base.mako"/>
<%def name="title()">${lesson.name} — Laplas</%def>

<article class="lesson-article">
    <div class="lesson-meta">
        <span class="lc-subject">${lesson.subject}</span>
        <span class="lc-num">Lesson #${lesson.num}</span>
        <span class="lc-type">${lesson.lesson_type}</span>
    </div>
    <h1 class="lesson-title">${lesson.name}</h1>

    <div class="lesson-body">
        ${lesson.lesson_html | n}
    </div>

    <div class="lesson-actions">
        % if user:
            % if is_completed:
                <button class="btn-success" disabled>✓ Completed</button>
            % else:
                <button class="btn-primary" id="complete-btn" data-num="${lesson.num}">
                    Mark as completed (+5 XP)
                </button>
            % endif
        % else:
            <a href="/login" class="btn-primary">Sign in to track progress</a>
        % endif
        <a href="/lessons" class="btn-ghost">← Back to lessons</a>
    </div>
</article>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('complete-btn');
    if (!btn) return;

    btn.addEventListener('click', async () => {
        const originalText = btn.textContent;
        btn.disabled = true;
        btn.textContent = 'Saving...';

        try {
            const res = await fetch('/lesson/completed_lesson', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',              // ← КЛЮЧЕВО: отправлять cookie
                body: JSON.stringify({ lesson_id: Number(btn.dataset.num) })
            });

            if (res.status === 401) {
                btn.textContent = 'Please sign in again';
                btn.classList.replace('btn-primary', 'btn-outline');
                setTimeout(() => { window.location.href = '/login'; }, 1200);
                return;
            }

            if (!res.ok) {
                const text = await res.text();
                console.error('Server error:', res.status, text);
                btn.disabled = false;
                btn.textContent = originalText;
                alert('Failed: ' + res.status);
                return;
            }

            const data = await res.json();
            btn.textContent = data.xp > 0 ? '✓ Completed (+' + data.xp + ' XP)' : '✓ Completed';
            btn.classList.replace('btn-primary', 'btn-success');
        } catch (err) {
            console.error(err);
            btn.disabled = false;
            btn.textContent = originalText;
        }
    });
});
</script>