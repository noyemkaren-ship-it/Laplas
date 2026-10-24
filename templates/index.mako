<%inherit file="base.mako"/>
<%def name="title()">Laplas — Learn deeper. Think sharper.</%def>

<section class="hero">
    <div class="hero-content">
        <span class="hero-tag">✦ Next-generation learning</span>
        <h1 class="hero-title">
            Master any subject<br/>
            <span class="gradient-text">without the noise.</span>
        </h1>
        <p class="hero-sub">
            Laplas is a business-grade learning platform that adapts to you.
            Structured lessons, intelligent tests, measurable progress.
        </p>
        <div class="hero-actions">
            <a href="/lessons" class="btn-primary btn-lg">Start Learning →</a>
            <a href="/register" class="btn-outline btn-lg">Create Account</a>
        </div>
        <div class="hero-stats">
            <div class="stat">
                <span class="stat-num">${lessons_count}+</span>
                <span class="stat-label">Lessons available</span>
            </div>
            <div class="stat">
                <span class="stat-num">${len(subjects)}</span>
                <span class="stat-label">Subjects</span>
            </div>
            <div class="stat">
                <span class="stat-num">5 XP</span>
                <span class="stat-label">per lesson</span>
            </div>
        </div>
    </div>

    <div class="hero-visual">
        <div class="glass-card float-1">
            <div class="gc-head">🎯 Focused learning</div>
            <div class="gc-bar"><div class="gc-fill" style="width:78%"></div></div>
            <div class="gc-sub">78% mastery</div>
        </div>
        <div class="glass-card float-2">
            <div class="gc-head">⚡ Streak</div>
            <div class="gc-big">12 days</div>
            <div class="gc-sub">Keep going</div>
        </div>
        <div class="glass-card float-3">
            <div class="gc-head">🏆 Achievements</div>
            <div class="gc-sub">First lesson completed!</div>
        </div>
    </div>
</section>

<section class="features">
    <h2 class="section-title">Built for people who take learning seriously</h2>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="fc-icon">📚</div>
            <h3>Structured Lessons</h3>
            <p>Hand-crafted content across subjects, organized by difficulty and progress.</p>
        </div>
        <div class="feature-card">
            <div class="fc-icon">🧠</div>
            <h3>Smart Testing</h3>
            <p>Validate understanding with targeted tests that reward real comprehension.</p>
        </div>
        <div class="feature-card">
            <div class="fc-icon">📈</div>
            <h3>Progress Tracking</h3>
            <p>Track XP, streaks and completions in a clean, distraction-free dashboard.</p>
        </div>
        <div class="feature-card">
            <div class="fc-icon">🔒</div>
            <h3>Secure Sessions</h3>
            <p>Cookie-based auth, admin-protected content creation, role-based access.</p>
        </div>
    </div>
</section>

% if subjects:
<section class="subjects-preview">
    <h2 class="section-title">Explore subjects</h2>
    <div class="subject-chips">
        % for s in subjects:
            <a href="/tests/subject/${s}" class="chip">${s}</a>
        % endfor
    </div>
</section>
% endif