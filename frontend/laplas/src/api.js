import {
  API_BASE_URL,
  API_WITH_CREDENTIALS,
  API_TIMEOUT,
  ENDPOINTS,
  logApi,
} from "./config";

async function request(path, options = {}) {
  const controller = API_TIMEOUT ? new AbortController() : null;
  const timer = controller
    ? setTimeout(() => controller.abort(), API_TIMEOUT)
    : null;

  const url = `${API_BASE_URL}${path}`;
  logApi(options.method || "GET", url);

  try {
    const res = await fetch(url, {
      credentials: API_WITH_CREDENTIALS ? "include" : "same-origin",
      headers: {
        "Content-Type": "application/json",
        ...(options.headers || {}),
      },
      signal: controller?.signal,
      ...options,
    });

    if (!res.ok) {
      let detail = `HTTP ${res.status}`;
      try {
        const j = await res.json();
        detail = j.detail || detail;
      } catch {}
      throw new Error(detail);
    }

    const text = await res.text();
    try {
      return JSON.parse(text);
    } catch {
      return text;
    }
  } finally {
    if (timer) clearTimeout(timer);
  }
}

export const api = {
  // ── user ──────────────────────────────
  register: (d) =>
    request(ENDPOINTS.userRegister, {
      method: "POST",
      body: JSON.stringify(d),
    }),

  login: (d) =>
    request(ENDPOINTS.userLogin, {
      method: "POST",
      body: JSON.stringify(d),
    }),

  getUsers: () => request(ENDPOINTS.userAll),

  // ── lessons ───────────────────────────
  getAllLessons: () => request(ENDPOINTS.lessonsAll),

  getLessonsBySubject: (s) =>
    request(ENDPOINTS.lessonsBySubject(s)),

  getLessonByNum: (n) => request(ENDPOINTS.lessonByNum(n)),

  completeLesson: (lessonId) =>
    request(ENDPOINTS.lessonComplete, {
      method: "POST",
      body: JSON.stringify({ lesson_id: lessonId }),
    }),

  getMyCompleted: () => request(ENDPOINTS.lessonsMyCompleted),

  // ── tests ─────────────────────────────
  createTest: (d) =>
    request(ENDPOINTS.testCreate, {
      method: "POST",
      body: JSON.stringify(d),
    }),

  answerTest: (d) =>
    request(ENDPOINTS.testAnswer, {
      method: "POST",
      body: JSON.stringify(d),
    }),

  getTestById: (id) => request(ENDPOINTS.testById(id)),
};