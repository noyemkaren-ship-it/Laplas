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
        <div class="stat-value">${lessons_count}</div>
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
        <a href="/tutors" class="chip active">All</a>
        % for s in subjects:
            <a href="/tutors?subject=${s}" class="chip">${s}</a>
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
                        <a href="/tutors/${t.id}" class="btn-primary" style="flex:1;">Book session</a>
                    % else:
                        <a href="/login" class="btn-primary" style="flex:1;">Sign in to book</a>
                    % endif
                    <a href="/tutors/${t.id}" class="btn-outline">Profile</a>
                </div>
            </div>
            % endfor
        </div>
    % else:
        <!-- Fallback: контроллер не передал tutors, показываем заглушку по subjects -->
        % if subjects:
            <div class="subject-cards">
                % for s in subjects:
                <a href="/tutors?subject=${s}" class="subject-card">
                    <div class="sc-glow"></div>
                    <h3>${s}</h3>
                    <span class="sc-arrow">Find tutors →</span>
                </a>
                % endfor
            </div>
        % else:
            <div class="empty" style="padding:80px 20px;">
                <div style="font-size:48px; margin-bottom:16px;">🎓</div>
                <h3 style="font-family:'Space Grotesk',sans-serif; font-size:22px; margin-bottom:8px; color:var(--text);">No tutors yet</h3>
                <p>Be the first to join as a private tutor on Laplas.</p>
                % if user:
                    <a href="/tutors/apply" class="btn-primary" style="margin-top:20px;">Become a tutor →</a>
                % else:
                    <a href="/register" class="btn-primary" style="margin-top:20px;">Create account →</a>
                % endif
            </div>
        % endif
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
        <a href="/tutors/apply" class="btn-primary btn-lg">Apply as tutor</a>
        <a href="/lessons" class="btn-outline btn-lg">Browse lessons</a>
    </div>
</section>