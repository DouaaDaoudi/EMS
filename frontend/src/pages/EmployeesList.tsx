import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import {
  getEmployees,
  createEmployee,
  updateEmployee,
  deleteEmployee,
} from "../api/employeeApi";
import { getCurrentUser } from "../api/profileApi";
import EmployeeCard from "../components/EmployeeCard";
import EmployeeForm from "../components/EmployeeForm";

function EmployeesList() {
  const [employees, setEmployees] =
    useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  const fetchEmployees = async () => {
    try {
      const data = await getEmployees();

      setEmployees(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
  fetchEmployees();

  getCurrentUser()
    .then(setCurrentUser)
    .catch(console.error);
}, []);

  const handleCreateEmployee =
    async (employee: any) => {
      try {
        await createEmployee(employee);

        fetchEmployees();
      } catch (err) {
        console.error(err);
      }
    };

    const handleUpdateEmployee = async (
  employeeId: string,
  updatedEmployee: any
) => {
  await updateEmployee(employeeId, updatedEmployee);
  fetchEmployees();
};

const handleDeleteEmployee = async (employeeId: string) => {
  await deleteEmployee(employeeId);
  fetchEmployees();
};
 return (
  <div className="dashboard-page">

    <Navbar />

    <div className="dashboard-container">

      <div className="dashboard-header">
        <h1>Employees</h1>

        <p>
          Manage your employee records
        </p>
      </div>

      {currentUser?.role === "admin" && (
        <div className="dashboard-form">
          <EmployeeForm
            onSubmit={handleCreateEmployee}
          />
        </div>
      )}

      <div className="employees-grid">
  {employees.map((employee) => (
    <EmployeeCard
      key={employee.employee_id}
      employee={employee}
      isAdmin={currentUser?.role === "admin"}
      onDelete={handleDeleteEmployee}
      onUpdate={handleUpdateEmployee}
    />
  ))}
</div>

    </div>
  </div>
);
}

export default EmployeesList;