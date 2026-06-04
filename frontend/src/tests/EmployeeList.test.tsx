import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import EmployeesList from "../pages/EmployeesList";
import * as employeeApi from "../api/employeeApi";
import * as profileApi from "../api/profileApi";

vi.mock("../api/employeeApi");
vi.mock("../api/profileApi");
vi.mock("../components/Navbar", () => ({
  default: () => <nav data-testid="navbar" />,
}));

const mockEmployees = [
  {
    employee_id: "E001",
    name: "Alice Smith",
    email: "alice@example.com",
    position: "Engineer",
    department: "Engineering",
    status: "Active",
  },
  {
    employee_id: "E002",
    name: "Bob Jones",
    email: "bob@example.com",
    position: "Designer",
    department: "Design",
    status: "Active",
  },
];

const adminUser = { role: "admin", name: "Admin User" };
const regularUser = { role: "employee", name: "Regular User" };

beforeEach(() => {
  vi.clearAllMocks();
  vi.mocked(employeeApi.getEmployees).mockResolvedValue(mockEmployees);
  vi.mocked(profileApi.getCurrentUser).mockResolvedValue(regularUser);
});

describe("EmployeesList", () => {
  it("renders the page heading", async () => {
    render(<EmployeesList />);

    expect(screen.getByText("Employees")).toBeInTheDocument();
    expect(screen.getByText("Manage your employee records")).toBeInTheDocument();
  });

  it("renders the navbar", async () => {
    render(<EmployeesList />);

    expect(screen.getByTestId("navbar")).toBeInTheDocument();
  });

  it("fetches and displays employees on mount", async () => {
    render(<EmployeesList />);

    await waitFor(() => {
      expect(employeeApi.getEmployees).toHaveBeenCalledTimes(1);
    });

    expect(await screen.findByText("Alice Smith")).toBeInTheDocument();
    expect(await screen.findByText("Bob Jones")).toBeInTheDocument();
  });

  it("hides EmployeeForm for non-admin users", async () => {
    vi.mocked(profileApi.getCurrentUser).mockResolvedValue(regularUser);

    render(<EmployeesList />);

    await waitFor(() => {
      expect(profileApi.getCurrentUser).toHaveBeenCalledTimes(1);
    });

    expect(screen.queryByText("Add New Employee")).not.toBeInTheDocument();
  });

  it("shows EmployeeForm for admin users", async () => {
    vi.mocked(profileApi.getCurrentUser).mockResolvedValue(adminUser);

    render(<EmployeesList />);

    expect(await screen.findByText("Add New Employee")).toBeInTheDocument();
  });

  it("creates an employee and refreshes the list", async () => {
    vi.mocked(profileApi.getCurrentUser).mockResolvedValue(adminUser);
    vi.mocked(employeeApi.createEmployee).mockResolvedValue({});

    render(<EmployeesList />);

    await screen.findByText("Add New Employee");

    fireEvent.change(screen.getByPlaceholderText("Employee ID"), {
      target: { value: "E003" },
    });
    fireEvent.change(screen.getByPlaceholderText("Full Name"), {
      target: { value: "Carol White" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email Address"), {
      target: { value: "carol@example.com" },
    });
    fireEvent.change(screen.getByPlaceholderText("Position"), {
      target: { value: "Manager" },
    });
    fireEvent.change(screen.getByPlaceholderText("Department"), {
      target: { value: "HR" },
    });

    fireEvent.click(screen.getByRole("button", { name: /add employee/i }));

    await waitFor(() => {
      expect(employeeApi.createEmployee).toHaveBeenCalledWith(
        expect.objectContaining({
          employee_id: "E003",
          name: "Carol White",
          email: "carol@example.com",
          position: "Manager",
          department: "HR",
        })
      );
    });

    expect(employeeApi.getEmployees).toHaveBeenCalledTimes(2);
  });

  it("deletes an employee and refreshes the list", async () => {
    vi.mocked(profileApi.getCurrentUser).mockResolvedValue(adminUser);
    vi.mocked(employeeApi.deleteEmployee).mockResolvedValue({});
    vi.spyOn(window, "confirm").mockReturnValue(true);

    render(<EmployeesList />);

    await screen.findByText("Alice Smith");

    const deleteButtons = screen.getAllByRole("button", { name: /delete/i });
    fireEvent.click(deleteButtons[0]);

    await waitFor(() => {
      expect(employeeApi.deleteEmployee).toHaveBeenCalledWith("E001");
    });

    expect(employeeApi.getEmployees).toHaveBeenCalledTimes(2);
  });

  it("updates an employee and refreshes the list", async () => {
    vi.mocked(profileApi.getCurrentUser).mockResolvedValue(adminUser);
    vi.mocked(employeeApi.updateEmployee).mockResolvedValue({});

    render(<EmployeesList />);

    await screen.findByText("Alice Smith");

    const editButtons = screen.getAllByRole("button", { name: /edit/i });
    fireEvent.click(editButtons[0]);

    const nameInput = screen.getByDisplayValue("Alice Smith");
    fireEvent.change(nameInput, { target: { value: "Alice Updated" } });

    fireEvent.click(screen.getByRole("button", { name: /save/i }));

    await waitFor(() => {
      expect(employeeApi.updateEmployee).toHaveBeenCalledWith(
        "E001",
        expect.objectContaining({ name: "Alice Updated" })
      );
    });

    expect(employeeApi.getEmployees).toHaveBeenCalledTimes(2);
  });

  it("handles getEmployees API error gracefully", async () => {
    const consoleSpy = vi.spyOn(console, "error").mockImplementation(() => {});
    vi.mocked(employeeApi.getEmployees).mockRejectedValue(
      new Error("Network error")
    );

    render(<EmployeesList />);

    await waitFor(() => {
      expect(employeeApi.getEmployees).toHaveBeenCalledTimes(1);
    });

    expect(consoleSpy).toHaveBeenCalled();
    consoleSpy.mockRestore();
  });

  it("handles getCurrentUser API error gracefully", async () => {
    const consoleSpy = vi.spyOn(console, "error").mockImplementation(() => {});
    vi.mocked(profileApi.getCurrentUser).mockRejectedValue(
      new Error("Unauthorized")
    );

    render(<EmployeesList />);

    await waitFor(() => {
      expect(profileApi.getCurrentUser).toHaveBeenCalledTimes(1);
    });

    expect(consoleSpy).toHaveBeenCalled();
    consoleSpy.mockRestore();
  });

  it("renders no employee cards when list is empty", async () => {
    vi.mocked(employeeApi.getEmployees).mockResolvedValue([]);

    render(<EmployeesList />);

    await waitFor(() => {
      expect(employeeApi.getEmployees).toHaveBeenCalledTimes(1);
    });

    expect(screen.queryByText("Alice Smith")).not.toBeInTheDocument();
    expect(screen.queryByText("Bob Jones")).not.toBeInTheDocument();
  });
});
