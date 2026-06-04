variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "student_name" {
  description = "Student name used for resource naming"
  type        = string
}

variable "cohort" {
  description = "Training cohort name"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
}

variable "jwt_secret_key" {
  description = "JWT secret key for backend authentication"
  type        = string
  sensitive   = true
}