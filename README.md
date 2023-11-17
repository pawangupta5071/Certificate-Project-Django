# Certificate Project - Django

This project involves three levels of development:

## Level 1
Establishes a many-to-many relationship between students and teachers. The data is stored in tables, and selecting a teacher displays the corresponding students, while selecting students displays the corresponding teachers.

## Level 2
Involves choosing a teacher and a student pair to generate a certificate.

## Level 3
Introduces the verification of certificates using JWT (JSON Web Token) authentication.

## Getting Started

1. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Use the following credentials for the Django admin panel:**
    - Username: pawan
    - Password: 2013

4. **Run the local development server:**

    ```bash
    python manage.py runserver
    ```

    Access the home page at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## URLs

- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Generate Token:** [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)
- **Generate Certificate:** [http://127.0.0.1:8000/generate_certificate/](http://127.0.0.1:8000/generate_certificate/)
- **Certificate List:** [http://127.0.0.1:8000/certificate_list/](http://127.0.0.1:8000/certificate_list/)
- **Verify Certificate:** [http://localhost:8000/verify-certificate/](http://localhost:8000/verify-certificate/)

## Testing Verify Certificate

1. **Run the local server:**

    ```bash
    python manage.py runserver
    ```

2. **Use the Thunder Client extension in VS Code.**
    - Import the collection from `thunder-collection_Certificate Project.json`.
    - In the "Certificate Project" collection, you have two requests:
        - `verify-certificate`
        - `Generate Token` (use this to generate a new token for authentication).

3. **Run the `Generate Token` request to obtain an access token.**

4. **Copy the access token from the response.**

5. **Open the `verify-certificate` request, click on Headers, and replace `access_token` in the `Authorization` header with the actual access token.**

6. **Run the `verify-certificate` request to test certificate verification.**
