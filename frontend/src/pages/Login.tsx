import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import { loginUser } from "../api/authApi";
import { useAuth } from "../context/AuthContext";

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");

  const handleSubmit = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    try {
      const data = await loginUser(email, password);

      login(data.access_token);

      navigate("/employees");
    } catch (err) {
      setError("Invalid email or password");
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-header">
          <h1 className="auth-title">
            User Login
          </h1>

         
        </div>

        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email address"
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

          <button
            className="auth-button"
            type="submit"
          >
            Login
          </button>
        </form>

        <p className="link-text">
          Don&apos;t have an account?{" "}
          <Link to="/register">
            Register
          </Link>
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

export default Login;