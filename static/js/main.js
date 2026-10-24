/* ============================================================
   Laplas — main.js
   ============================================================ */

/* ---------- 1. 3D animated background (Three.js) ---------- */
(function initBg() {
    if (typeof THREE === "undefined") return;
    const canvas = document.getElementById("bg-canvas");
    if (!canvas) return;

    const renderer = new THREE.WebGLRenderer({
        canvas,
        alpha: true,
        antialias: true,
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
        60,
        window.innerWidth / window.innerHeight,
        0.1,
        100
    );
    camera.position.z = 10;

    // Particles layer 1 (violet)
    const geo = new THREE.BufferGeometry();
    const count = 900;
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count * 3; i++) {
        positions[i] = (Math.random() - 0.5) * 40;
    }
    geo.setAttribute("position", new THREE.BufferAttribute(positions, 3));

    const mat = new THREE.PointsMaterial({
        color: 0x6d5cff,
        size: 0.04,
        transparent: true,
        opacity: 0.7,
        blending: THREE.AdditiveBlending,
    });
    const points = new THREE.Points(geo, mat);
    scene.add(points);

    // Particles layer 2 (cyan)
    const mat2 = new THREE.PointsMaterial({
        color: 0x00d4ff,
        size: 0.03,
        transparent: true,
        opacity: 0.5,
        blending: THREE.AdditiveBlending,
    });
    const points2 = points.clone();
    points2.material = mat2;
    points2.position.z = -3;
    scene.add(points2);

    let mouseX = 0;
    let mouseY = 0;
    window.addEventListener("mousemove", (e) => {
        mouseX = e.clientX / window.innerWidth - 0.5;
        mouseY = e.clientY / window.innerHeight - 0.5;
    });

    const clock = new THREE.Clock();
    function animate() {
        requestAnimationFrame(animate);
        const t = clock.getElapsedTime();
        points.rotation.y = t * 0.03 + mouseX * 0.3;
        points.rotation.x = t * 0.01 + mouseY * 0.2;
        points2.rotation.y = -t * 0.04 + mouseX * 0.4;
        points2.rotation.x = t * 0.02 + mouseY * 0.3;
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener("resize", () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
})();

/* ---------- 2. Card cursor glow (делегирование) ---------- */
document.addEventListener("mousemove", (e) => {
    const card = e.target.closest(".lesson-card");
    if (!card) return;
    const rect = card.getBoundingClientRect();
    card.style.setProperty("--mx", `${e.clientX - rect.left}px`);
    card.style.setProperty("--my", `${e.clientY - rect.top}px`);
});

/* ---------- 3. Scroll reveal ---------- */
(function initReveal() {
    const selectors =
        ".feature-card, .lesson-card, .test-card, .subject-card, .profile-card";
    const elements = document.querySelectorAll(selectors);
    if (!elements.length) return;

    // Fallback для старых браузеров
    if (!("IntersectionObserver" in window)) {
        elements.forEach((el) => el.classList.add("revealed"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("revealed");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
    );

    elements.forEach((el) => observer.observe(el));
})();