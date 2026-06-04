import { useState } from "react";

type EmployeeFormProps = {
  onSubmit: (employee: any) => void;
};

function EmployeeForm({ onSubmit }: EmployeeFormProps) {
  const initialEmployee = {
    employee_id: "",
    name: "",
    email: "",
    position: "",
    department: "",
    status: "Active",
  };

  const [employee, setEmployee] = useState(initialEmployee);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    setEmployee({
      ...employee,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    onSubmit(employee);
    setEmployee(initialEmployee);
  };

  return (
    <div className="employee-form-card">
      <div className="form-header">
        <h2>Add New Employee</h2>
        <p>Create a new employee profile in the system</p>
      </div>

      <form className="employee-form" onSubmit={handleSubmit}>
        <input
          name="employee_id"
          placeholder="Employee ID"
          value={employee.employee_id}
          onChange={handleChange}
          required
        />

        <input
          name="name"
          placeholder="Full Name"
          value={employee.name}
          onChange={handleChange}
          required
        />

        <input
          name="email"
          type="email"
          placeholder="Email Address"
          value={employee.email}
          onChange={handleChange}
          required
        />

        <input
          name="position"
          placeholder="Position"
          value={employee.position}
          onChange={handleChange}
          required
        />

        <input
          name="department"
          placeholder="Department"
          value={employee.department}
          onChange={handleChange}
          required
        />

        <select
          name="status"
          value={employee.status}
          onChange={handleChange}
        >
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>

        <button className="create-button" type="submit">
          Add Employee
        </button>
      </form>
    </div>
  );
}

export default EmployeeForm;