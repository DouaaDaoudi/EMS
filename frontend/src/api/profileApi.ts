import api from "./axios";

export const getCurrentUser = async () => {
  const response = await api.get("/profile/me");
  return response.data;
};