import { useEffect, useState } from "react";

import {
  getEmployees,
  createEmployee,
} from "../api/employeeApi";

import EmployeeCard from "../components/EmployeeCard";
import EmployeeForm from "../components/EmployeeForm";

function EmployeesList() {
  const [employees, setEmployees] =
    useState<any[]>([]);

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

  return (
    <div>
      <h1>Employees</h1>

      <EmployeeForm
        onSubmit={handleCreateEmployee}
      />

      <div>
        {employees.map((employee) => (
          <EmployeeCard
            key={employee.employee_id}
            employee={employee}
          />
        ))}
      </div>
    </div>
  );
}

export default EmployeesList;