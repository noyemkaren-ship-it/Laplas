<%inherit file="base.mako"/>
<%def name="title()">Subjects — Laplas</%def>

<section class="page-header">
    <h1>Subjects</h1>
    <p>Browse every subject available on Laplas.</p>
</section>

<div class="subject-cards">
    % for s in subjects:
        <a href="/tests/subject/${s}" class="subject-card">
            <div class="sc-glow"></div>
            <h3>${s}</h3>
            <span class="sc-arrow">Explore →</span>
        </a>
    % endfor
</div>