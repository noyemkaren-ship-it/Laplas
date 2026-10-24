<%inherit file="base.mako"/>
<%def name="title()">Profile — Laplas</%def>

<section class="page-header">
    <h1>Hey, ${user.name} 👋</h1>
    <p>Your learning dashboard.</p>
</section>

<div class="profile-grid">
    <div class="profile-card stat-card">
        <div class="stat-label">Total XP</div>
        <div class="stat-value">⚡ ${user.xp or 0}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Lessons completed</div>
        <div class="stat-value">${len(completed)}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Role</div>
        <div class="stat-value">${'Admin' if user.admin else 'Learner'}</div>
    </div>
</div>

<section class="profile-section">
    <h2>Recent completions</h2>
    % if completed:
        <ul class="completed-list">
            % for c in completed:
                <li>
                    <span class="cl-dot"></span>
                    Lesson ID: ${c.lesson_id}
                    <span class="cl-xp">+5 XP</span>
                </li>
            % endfor
        </ul>
    % else:
        <p class="empty">No lessons completed yet. <a href="/lessons">Start now →</a></p>
    % endif
</section>