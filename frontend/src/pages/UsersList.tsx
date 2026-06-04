import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import { getUsers } from "../api/userApi";

type User = {
  _id?: string;
  id?: string;
  email: string;
  role: string;
};

function UsersList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const data = await getUsers();

        console.log("USERS DATA:", data);

        setUsers(Array.isArray(data) ? data : []);
      } catch (err: any) {
        console.error(err);

        setError(
          err.response?.data?.detail ||
            "Failed to load users"
        );
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="dashboard-page">
      <Navbar />

      <div className="dashboard-container">
        <div className="dashboard-header">
          <h1>Users</h1>

          <p>
            Registered application users
          </p>
        </div>

        {loading && (
          <p className="info-message">
            Loading users...
          </p>
        )}

        {error && (
          <p className="error">
            {error}
          </p>
        )}

        {!loading &&
          !error &&
          users.length === 0 && (
            <p className="info-message">
              No users found.
            </p>
          )}

        {!loading && !error && users.length > 0 && (
          <div className="users-grid">
            {users.map((user) => (
              <div
                className="user-card"
                key={user._id || user.id || user.email}
              >
                <h3>{user.email}</h3>

                <span className="user-role">
                  {user.role}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default UsersList;