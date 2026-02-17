# S3 → Lambda → Jenkins → Docker CI/CD Pipeline

## Architecture

S3 Upload → Lambda → Jenkins → Docker → Deploy

## Workflow

1. Upload file to S3 bucket
2. S3 triggers Lambda function
3. Lambda triggers Jenkins pipeline
4. Jenkins builds Docker image
5. Jenkins deploys container

## Technologies Used

- AWS S3
- AWS Lambda
- Jenkins
- Docker
- GitHub
- EC2
- Nginx

## Author

Aniket Jadhav

