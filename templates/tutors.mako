<%inherit file="base.mako"/>
<%def name="title()">Private Tutors — Laplas</%def>

<section class="page-header">
    <div style="display:flex; align-items:flex-end; justify-content:space-between; gap:20px; flex-wrap:wrap;">
        <div>
            <span class="hero-tag" style="margin-bottom:12px; display:inline-block;">🎓 Private Tutors</span>
            <h1>Learn with a personal tutor</h1>
            <p>One-on-one sessions with vetted experts across every subject on Laplas.</p>
        </div>
        % if user:
            <a href="/tutors/apply" class="btn-primary">Become a tutor →</a>
        % else:
            <a href="/register" class="btn-primary">Sign up to book →</a>
        % endif
    </div>
</section>

<!-- Stats -->
<div class="profile-grid" style="margin-bottom:48px;">
    <div class="profile-card stat-card">
        <div class="stat-label">Tutors</div>
        <div class="stat-value">${tutors_count}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Subjects</div>
        <div class="stat-value">${len(subjects)}</div>
    </div>
    <div class="profile-card stat-card">
        <div class="stat-label">Avg. rating</div>
        <div class="stat-value">4.9</div>
    </div>
</div>

% if subjects:
<section style="margin-bottom:48px;">
    <h2 class="section-title" style="text-align:left; font-size:24px; margin-bottom:20px;">Filter by subject</h2>
    <div class="filter-row">
        <a href="/private-tutors"
           class="chip ${'active' if not active_subject else ''}">All</a>
        % for s in subjects:
            <a href="/private-tutors?subject=${s}"
               class="chip ${'active' if s == active_subject else ''}">${s}</a>
        % endfor
    </div>
</section>
% endif

<!-- Tutors grid -->
<section>
    % if tutors:
        <div class="tutors-grid">
            % for t in tutors:
            <div class="tutor-card">
                <div class="tutor-top">
                    <div class="tutor-avatar">${(t.name or "?")[0].upper()}</div>
                    <div class="tutor-info">
                        <h3 class="tutor-name">${t.name}</h3>
                        <div class="tutor-subject">${t.subject}</div>
                    </div>
                    % if getattr(t, "rating", None):
                        <div class="tutor-rating">★ ${t.rating}</div>
                    % endif
                </div>

                % if getattr(t, "bio", None):
                    <p class="tutor-bio">${t.bio}</p>
                % endif

                <div class="tutor-meta">
                    % if getattr(t, "price", None):
                        <span class="tutor-price">${t.price} / hour</span>
                    % endif
                    % if getattr(t, "experience", None):
                        <span class="tutor-exp">${t.experience} yrs exp.</span>
                    % endif
                </div>

                <div class="tutor-actions">
                    % if user:
                        <a href="/private-tutors/${t.id}/book" class="btn-primary" style="flex:1;">Book a session</a>
                    % else:
                        <a href="/login" class="btn-primary" style="flex:1;">Sign in to book</a>
                    % endif
                </div>
            </div>
            % endfor
        </div>
    % else:
        <div style="text-align:center; padding:60px 20px; color:var(--muted);">
            <h3 style="margin-bottom:8px;">No tutors found</h3>
            <p>
                % if active_subject:
                    По предмету «${active_subject}» пока нет репетиторов.
                    <a href="/private-tutors" style="color:var(--accent);">Показать всех</a>
                % else:
                    Пока нет ни одного репетитора. Загляните позже или станьте первым!
                % endif
            </p>
        </div>
    % endif
</section>

<!-- CTA -->
<section style="margin-top:80px; padding:48px 40px; border-radius:20px; background:linear-gradient(135deg, rgba(109,92,255,.12), rgba(0,212,255,.06)); border:1px solid var(--border); text-align:center;">
    <h2 class="section-title" style="margin-bottom:12px;">Teach on Laplas</h2>
    <p style="color:var(--muted); max-width:520px; margin:0 auto 28px; font-size:16px; line-height:1.6;">
        Share your expertise, set your own schedule, and get paid for what you love.
        Join our growing network of private tutors.
    </p>
    <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
        <a href="/lessons" class="btn-primary btn-lg">Apply as tutor</a>
        <a href="/lessons" class="btn-outline btn-lg">Browse lessons</a>
    </div>
</section>