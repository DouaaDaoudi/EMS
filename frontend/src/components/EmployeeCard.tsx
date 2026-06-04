import { useState } from "react";

type EmployeeCardProps = {
  employee: {
    employee_id: string;
    name: string;
    email: string;
    position: string;
    department: string;
    status: string;
  };

  isAdmin?: boolean;

  onDelete?: (employeeId: string) => void;

  onUpdate?: (
    employeeId: string,
    updatedEmployee: any
  ) => void;
};

function EmployeeCard({
  employee,
  isAdmin,
  onDelete,
  onUpdate,
}: EmployeeCardProps) {

  const [isEditing, setIsEditing] =
    useState(false);

  const [editedEmployee, setEditedEmployee] =
    useState(employee);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setEditedEmployee({
      ...editedEmployee,
      [e.target.name]: e.target.value,
    });
  };

  const handleSave = async () => {
    if (onUpdate) {
      await onUpdate(
        employee.employee_id,
        editedEmployee
      );
    }

    setIsEditing(false);
  };

  return (
    <div className="employee-card">

      {isEditing ? (
        <div className="employee-edit-form">

          <input
            name="name"
            value={editedEmployee.name}
            onChange={handleChange}
          />

          <input
            name="email"
            value={editedEmployee.email}
            onChange={handleChange}
          />

          <input
            name="position"
            value={editedEmployee.position}
            onChange={handleChange}
          />

          <input
            name="department"
            value={editedEmployee.department}
            onChange={handleChange}
          />

          <button
            className="save-button"
            onClick={handleSave}
          >
            Save
          </button>

        </div>
      ) : (
        <>
          <div className="employee-card-header">

            <div>
              <h3>{employee.name}</h3>

              <p className="employee-position">
                {employee.position}
              </p>
            </div>

            <span className="employee-status">
              {employee.status}
            </span>

          </div>

          <div className="employee-details">

            <p>
              <strong>ID:</strong>{" "}
              {employee.employee_id}
            </p>

            <p>
              <strong>Email:</strong>{" "}
              {employee.email}
            </p>

            <p>
              <strong>Department:</strong>{" "}
              {employee.department}
            </p>

          </div>

          {isAdmin && (
            <div className="employee-actions">

              <button
                className="edit-button"
                onClick={() =>
                  setIsEditing(true)
                }
              >
                Edit
              </button>

              <button
                className="delete-button"
                onClick={() =>{
                   if (confirm("Delete this employee?")) {
                  onDelete?.(
                    employee.employee_id
                  );
                }
              }}  
              >
                Delete
              </button>

            </div>
          )}
        </>
      )}
    </div>
  );
}

export default EmployeeCard;