# FastAPI S3 Bucket Monitoring Application

This project demonstrates a FastAPI application that checks an S3 bucket every minute and lists any new items on the console.

## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed
- Poetry installed
- AWS access key and secret access key set as environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/my_fastapi_project.git
   ```

2. Navigate to the project directory:
   ```
   cd my_fastapi_project
   ```

3. Initialize a new Poetry project:
   ```
   poetry init
   ```

4. Open the `pyproject.toml` file and add the required dependencies to the `[tool.poetry.dependencies]` section. For example, to add FastAPI and boto3, you can add the following lines:
   ```toml
   [tool.poetry.dependencies]
   fastapi = "^0.73.0"
   boto3 = "^1.21.1"
   ```

5. Save the `pyproject.toml` file and install the dependencies:
   ```
   poetry install
   ```

## Usage

1. Set the AWS access key and secret access key as environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).

2. Run the application using Poetry:
   ```
   poetry run uvicorn main:app --reload
   ```

3. Access the application at `http://localhost:8000`.

## Features

- Checks an S3 bucket every minute and lists any new items on the console.
- Uses the FastAPI framework for building the API.
- Uses the boto3 library for interacting with AWS S3.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use this project according to your needs.
