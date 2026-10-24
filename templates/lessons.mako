<%inherit file="base.mako"/>
<%def name="title()">Lessons — Laplas</%def>

<section class="page-header">
    <h1>All Lessons</h1>
    <p>Pick a lesson and start building your knowledge.</p>
</section>

<div class="filter-row">
    <a href="/lessons" class="chip ${'active' if not request.query_params.get('subject') else ''}">All</a>
    % for s in subjects:
        <a href="/lessons?subject=${s}" class="chip">${s}</a>
    % endfor
</div>

<div class="lessons-grid">
    % for l in lessons:
        <a href="/lesson/${l.num}" class="lesson-card">
            <div class="lc-head">
                <span class="lc-subject">${l.subject}</span>
                <span class="lc-num">#${l.num}</span>
            </div>
            <h3 class="lc-title">${l.name}</h3>
            <div class="lc-foot">
                <span class="lc-type">${l.lesson_type}</span>
                <span class="lc-arrow">→</span>
            </div>
        </a>
    % endfor
    % if not lessons:
        <p class="empty">No lessons yet. Ask an admin to create some.</p>
    % endif
</div>