<%inherit file="base.mako"/>
<%def name="title()">Admin Panel — Laplas</%def>

<section class="page-header">
    <div style="display:flex; align-items:center; justify-content:space-between; gap:20px; flex-wrap:wrap;">
        <div>
            <h1>Admin Panel</h1>
            <p>Manage lessons, tests and users.</p>
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a href="/admin_panel/lesson/new" class="btn-primary">+ New Lesson</a>
            <a href="/admin_panel/test/new" class="btn-outline">+ New Test</a>
            <a href="/" class="btn-ghost">← Back to site</a>
        </div>
    </div>
</section>

<!-- Stats -->
<div class="profile-grid" style="margin-bottom:40px;">
    <div class="profile-card stat-card">
        <div class="stat-label">Lessons</div>
        <div class="stat-value">${len(lessons)}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Tests</div>
        <div class="stat-value">${len(tests)}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Users</div>
        <div class="stat-value">${len(users)}</div>
    </div>
</div>

<!-- Tabs -->
<div class="filter-row">
    <a href="/admin_panel?tab=lessons" class="chip ${'active' if active_tab == 'lessons' else ''}">Lessons</a>
    <a href="/admin_panel?tab=tests" class="chip ${'active' if active_tab == 'tests' else ''}">Tests</a>
    <a href="/admin_panel?tab=users" class="chip ${'active' if active_tab == 'users' else ''}">Users</a>
</div>

<!-- ================= LESSONS TAB ================= -->
% if active_tab == 'lessons':
<section>
    % if lessons:
    <div class="lessons-grid">
        % for l in lessons:
        <div class="lesson-card" style="cursor:default;">
            <div class="lc-head">
                <span class="lc-subject">${l.subject}</span>
                <span class="lc-num">#${l.num}</span>
            </div>
            <h3 class="lc-title">${l.name}</h3>
            <div class="lc-foot">
                <span class="lc-type">${l.lesson_type}</span>
                <div style="display:flex; gap:8px; align-items:center;">
                    <a href="/lesson/${l.num}" class="btn-ghost" style="padding:6px 10px; font-size:13px;">View</a>
                    <form method="POST" action="/admin_panel/lesson/${l.id}/delete"
                          onsubmit="return confirm('Delete lesson «${l.name}»?');"
                          style="display:inline;">
                        <button type="submit" class="btn-ghost"
                                style="padding:6px 10px; font-size:13px; color:#ff5a7a;">Delete</button>
                    </form>
                </div>
            </div>
        </div>
        % endfor
    </div>
    % else:
        <p class="empty">No lessons yet. <a href="/admin_panel/lesson/new">Create the first one →</a></p>
    % endif
</section>
% endif

<!-- ================= TESTS TAB ================= -->
% if active_tab == 'tests':
<section>
    % if tests:
    <div class="tests-grid">
        % for t in tests:
        <div class="test-card">
            <div class="lc-subject">${t.subject}</div>
            <h3>${t.question}</h3>
            <div class="test-result ok" style="margin-bottom:12px;">Answer: <strong>${t.answer}</strong></div>
            <form method="POST" action="/admin_panel/test/${t.id}/delete"
                  onsubmit="return confirm('Delete this test?');">
                <button type="submit" class="btn-ghost"
                        style="padding:6px 10px; font-size:13px; color:#ff5a7a;">Delete</button>
            </form>
        </div>
        % endfor
    </div>
    % else:
        <p class="empty">No tests yet. <a href="/admin_panel/test/new">Create the first one →</a></p>
    % endif
</section>
% endif

<!-- ================= USERS TAB ================= -->
% if active_tab == 'users':
<section>
    % if users:
    <div style="display:flex; flex-direction:column; gap:12px;">
        % for u in users:
        <div class="profile-card" style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
            <div class="avatar">${u.name[0].upper()}</div>
            <div style="flex:1; min-width:180px;">
                <div style="font-weight:600; font-size:15px;">
                    ${u.name}
                    % if u.admin:
                        <span class="lc-subject" style="margin-left:8px; font-size:11px;">ADMIN</span>
                    % endif
                </div>
                <div style="color:var(--muted); font-size:13px;">${u.email}</div>
            </div>
            <div style="color:var(--muted); font-size:13px;">
                Age ${u.age} · ${u.num}
            </div>
            <div class="xp-badge">⚡ ${u.xp or 0} XP</div>
            % if u.id != user.id:
            <form method="POST" action="/admin_panel/user/${u.id}/delete"
                  onsubmit="return confirm('Delete user «${u.name}»?');">
                <button type="submit" class="btn-ghost"
                        style="padding:6px 10px; font-size:13px; color:#ff5a7a;">Delete</button>
            </form>
            % else:
            <span style="color:var(--muted); font-size:13px;">(you)</span>
            % endif
        </div>
        % endfor
    </div>
    % else:
        <p class="empty">No users yet.</p>
    % endif
</section>
% endif