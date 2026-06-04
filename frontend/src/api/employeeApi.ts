import api from "./axios";

export const getEmployees = async () => {
  const response = await api.get("/employees");
  return response.data;
};

export const createEmployee = async (employee: any) => {
  const response = await api.post("/employees", employee);
  return response.data;
};

export const updateEmployee = async (
  employeeId: string,
  employee: any
) => {
  const response = await api.put(`/employees/${employeeId}`, employee);
  return response.data;
};

export const deleteEmployee = async (employeeId: string) => {
  const response = await api.delete(`/employees/${employeeId}`);
  return response.data;
};