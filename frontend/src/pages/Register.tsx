import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { registerUser } from "../api/authApi";

function Register() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] =
    useState("");

  const [error, setError] =
    useState("");

  const handleSubmit = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    try {
      await registerUser(email, password);

      navigate("/login");
    } catch (err: any) {
       setError(
    err.response?.data?.detail ||
    "Registration failed"
        );
    }
  };

  return (
  <div className="auth-page">
    <div className="auth-card">
      <h1 className="auth-title">
        Register
      </h1>

      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button className="auth-button" type="submit">
          Register
        </button>
      </form>

      <p className="link-text">
        Already have an account?{" "}
        <a href="/login">Login</a>
      </p>

      {error && (
        <p className="error">
          {error}
        </p>
      )}
    </div>
  </div>
);
}

export default Register;