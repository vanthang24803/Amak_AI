# Running the Application

This is a basic guide on how to run the Python application.

## Prerequisites

To run the application, you will need to have the following installed on your machine:

- Python >= 3.12.6: [Download and Install Python](https://www.python.org/downloads/)
- Git: [Download and Install Git](https://git-scm.com/downloads)

## Environment

Setup env before run dockerfile:

```env
API_KEY=
```

## Running Application

```cmd
uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload
```

## License

This project is licensed under the [MIT License](LICENSE).
