## FIFO API Gateway Server

> [!NOTE]
> #### This project is independently maintained and is not supported by GitHub.

### Overview
A simple FIFO API Gateway for managing API calls, storing them in MySQL, and processing in order.

### Prerequisites
- ```Python 3.x```, ```Flask```, ```MySQL```, ```pip```

#### Instructions for Production Deployment found [Here](docker/README.md).

### Setup - Dev Environment / Small Deployment

1. Create a ```MySQL``` **User** and **Database** on ```MySQL 8``` or better.
   ```mysql
   CREATE DATABASE IF NOT EXISTS api_gateway_fifo;
   CREATE USER IF NOT EXISTS 'api_gateway'@'%' IDENTIFIED BY 'your_mysql_password';
   GRANT ALL PRIVILEGES ON api_gateway_fifo.* TO 'api_gateway'@'%';
   FLUSH PRIVILEGES;
   ```
   
2. Clone Repository:
   ```bash
   git clone https://github.com/appatalks/fifo_api_gateway_server.git
   cd api_fifo_limiter
   ```

3. Install Dependencies:
   ```bash
   pip install flask mysql-connector-python
   ```
   
4. Initialize MySQL Database:
   ```bash
   python fifo_init.py
   ```

### Usage

- Start Server
  ```bash
  python api_fifo_server.py
  ```
- Direct API to Server Endpoint
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "example data"}'
  ```
- Retrieve from MySQL and Delete Data;
  ```bash
  curl -k -X GET https://127.0.0.1:5000/api/deliver
  ```

(Remeber to use Valid Certificates, otherwise accept self-signed as valid with ```curl -k``` flag)

### Example: GitHub API Integration

- Save GitHub API Call:
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"headers\": {\"Accept\": \"application/vnd.github+json\", \"Authorization\": \"Bearer 
  <TOKEN>\", \"X-GitHub-Api-Version\": \"2022-11-28\"}, \"url\": \"https://git.example.com/api/v3/user\"}"}'
  {"status": "success"}
  ```

- Retrieve GitHub API Call:
  ```bash
  bash github_api_delivery.sh
  { "login": "octocat", "id": 10, ... }
  ```

### Example: OpenAI API Integration

- Save OpenAI API Call
  ```bash
  curl -k -X POST https://127.0.0.1:5000/api/save -H "Content-Type: application/json" -d '{"data": "{\"openai_token\": \"<OPENAI_API_KEY>\", \"data\": {\"model\": \"gpt-4\", \"messages\": 
  [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"Hello!\"}]}}"}'
  {"status":"success"}
  ```

- Retrieve OpenAI API Call:
  ```bash
  bash openai_api_delivery.sh 
  { "id": "c***", "object": "chat.completion", "created": 1***, "model": "gpt-4-0613", "choices": [ { "index": 0, "message": { "role": "assistant", 
  "content": "Hello! How can I assist you today?" } ... }
  ```

----

# Highlights

## Task Queue Management

### Background Processing
- **Use Case**: Applications that need to manage background tasks.
- **Benefit**: Ensures tasks are processed in the order they were received.

### Job Scheduling
- **Use Case**: Managing job scheduling systems.
- **Benefit**: Ensures jobs are executed in a specific order.
- **Example**: Regularly process queued request in-line with endpoint ```ratelimit``` gates.

## Logging and Analytics

### Event Logging
- **Use Case**: Serving as an event logging system.
- **Benefit**: Events are stored and processed in the order they occur.

### Data Analytics
- **Use Case**: Data analytics pipelines.
- **Benefit**: Processes data in the sequence it was received to maintain temporal consistency.
