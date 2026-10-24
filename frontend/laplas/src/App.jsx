import { useState } from "react";
import { AuthProvider, useAuth } from "./context/AuthContext";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";
import Subject from "./pages/Subject";
import Lesson from "./pages/Lesson";
import Navbar from "./components/Navbar";
import "./App.css";

function Router() {
  const { user } = useAuth();
  const [page, setPage] = useState({ name: "home" });
  const [refreshKey, setRefreshKey] = useState(0);

  if (!user) {
    return page.name === "register" ? (
      <Register onSwitch={() => setPage({ name: "login" })} />
    ) : (
      <Login onSwitch={() => setPage({ name: "register" })} />
    );
  }

  return (
    <>
      <Navbar onNavigate={setPage} />
      <main className="container">
        {page.name === "home" && (
          <Home
            key={`home-${refreshKey}`}
            onOpenSubject={(s) => setPage({ name: "subject", subject: s })}
          />
        )}
        {page.name === "subject" && (
          <Subject
            key={`subject-${page.subject}-${refreshKey}`}
            subject={page.subject}
            onOpenLesson={(num) =>
              setPage({ name: "lesson", num, subject: page.subject })
            }
            onBack={() => setPage({ name: "home" })}
          />
        )}
        {page.name === "lesson" && (
          <Lesson
            num={page.num}
            onBack={() =>
              setPage({ name: "subject", subject: page.subject })
            }
            onCompleted={() => setRefreshKey((k) => k + 1)}
          />
        )}
      </main>
    </>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <Router />
    </AuthProvider>
  );
}