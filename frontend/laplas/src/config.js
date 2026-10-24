// ⚙️ Конфиг фронтенда — меняй только здесь
const PROTOCOL = "http";
const HOST = "46.253.132.225";
const PORT = 7600;

export const API_BASE_URL = import.meta.env.DEV
  ? "/api"
  : import.meta.env.VITE_API_URL || `${PROTOCOL}://${HOST}:${PORT}`;

export const API_WITH_CREDENTIALS = true; // cookies (JWT в cookie "data")
export const API_TIMEOUT = 15000;
export const DEBUG_API = true;

export const ENDPOINTS = {
  userRegister: "/user/register",
  userLogin: "/user/login",
  userAll: "/user/all",

  lessonsAll: "/lesson/all_lessons",
  lessonsBySubject: (s) => `/lesson/subject/${encodeURIComponent(s)}`,
  lessonByNum: (n) => `/lesson/lesson/${n}`,
  lessonComplete: "/lesson/completed_lesson",
  lessonsMyCompleted: "/lesson/my_completed_lesson",

  testCreate: "/test",
  testAnswer: "/answer",
  testById: (id) => `/test_by_id/${id}`,
};

export function logApi(...a) {
  if (DEBUG_API) console.log("[api]", ...a);
}