import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  const user = JSON.parse(
    localStorage.getItem("user") || "{}"
  );

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        Employee Management System
      </div>

      <div className="navbar-right">
        <div className="navbar-links">
          <Link
            to="/employees"
            className="nav-link"
          >
            Employees
          </Link>

          <Link
            to="/users"
            className="nav-link"
          >
            Users
          </Link>
        </div>

        <div className="navbar-user">
          <span>{user.email}</span>

          <strong>{user.role}</strong>
        </div>

        <button
          onClick={handleLogout}
          className="logout-button"
        >
          Logout
        </button>
      </div>
    </nav>
  );
}

export default Navbar;