output "frontend_url" {
  value = aws_cloudfront_distribution.cdn.domain_name
}

output "api_url" {
  value = aws_apigatewayv2_api.api.api_endpoint
}

output "mongodb_public_ip" {
  value = aws_instance.mongodb.public_ip
}