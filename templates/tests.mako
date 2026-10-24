<%inherit file="base.mako"/>
<%def name="title()">Tests — Laplas</%def>

<section class="page-header">
    <h1>Tests</h1>
    <p>Validate your knowledge. Correct answers reward +10 XP.</p>
</section>

<div class="filter-row">
    <a href="/tests" class="chip ${'active' if not active_subject else ''}">All</a>
    % for s in subjects:
        <a href="/tests/subject/${s}" class="chip">${s}</a>
    % endfor
</div>

<div class="tests-grid">
    % for t in tests:
        <div class="test-card">
            <div class="lc-subject">${t.subject}</div>
            <h3>${t.question}</h3>
            <div class="test-answer-row">
                <input type="text" placeholder="Your answer" id="ans-${t.id}"/>
                <button class="btn-primary" onclick="submitTest(${t.id})">Submit</button>
            </div>
            <div class="test-result" id="res-${t.id}"></div>
        </div>
    % endfor
</div>

<script>
async function submitTest(id) {
    const input = document.getElementById('ans-' + id);
    const res = document.getElementById('res-' + id);
    const answer = input.value.trim();
    if (!answer) return;
    const r = await fetch('/answer', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({test_id: id, answer})
    });
    const data = await r.json();
    res.textContent = data.message === 'Okay' ? '✓ Correct (+10 XP)' : '✗ Wrong answer';
    res.className = 'test-result ' + (data.message === 'Okay' ? 'ok' : 'bad');
}
</script>