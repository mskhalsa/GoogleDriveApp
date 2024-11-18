# Google Drive App
Strac project by Mehar

---

## Overview of the Application

This is a Flask-based Python web application that integrates with the Google Drive API using OAuth 2.0 to allow users to perform various operations on their Google Drive files. Users can:
- Authenticate via Google OAuth 2.0.
- View their files stored in Google Drive.
- Upload files to their Google Drive.
- Download files from their Google Drive.
- Delete files from their Google Drive.

The app features a user-friendly interface built using Bootstrap, providing a responsive and accessible experience. It is designed to be lightweight, scalable, and easy to deploy using Docker.

---

## Instructions on Setting Up the Development Environment

### Prerequisites

1. **Python 3.11** or higher must be installed on your system.
2. Install **pip**, the Python package manager.
3. Install **Docker** and **Docker Compose**.
4. Set up a Google Cloud Project and enable the **Google Drive API**.

**NOTE:** *This Application **WILL NOT** work unless you give your own Google Drive API credentials to log into your Google Drive!*

---
### Steps to get Google OAuth 2.0 credentials
1. Create a Google Cloud Project and enable the Google Drive API.
2. Generate an OAuth 2.0 Client ID under APIs & Services > Credentials.
3. For redirect URL enter: ```http://localhost:5002/oauth2callback```
3. Download the ```client_secret.json``` file and place it in the root directory of the project.
4. Rename the file to be just -> ```client_secret.json```.
5. Put the ```client_secret.json``` in the GoogleDriveApp repository like so:
    ```bash
    git clone https://github.com/mskhalsa/GoogleDriveApp.git
    cp client_secret.json GoogleDriveApp
    ```
    
---
### Steps to Set Up the Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mskhalsa/GoogleDriveApp.git
   cd GoogleDriveApp
   ```
2. **Deploy with Docker Compose**
    ```bash
    cd GoogleDriveApp
    docker compose up -d --build
    ```
2. **To Deploy Locally Instead** *(Optional)*
   ```bash
   git clone https://github.com/mskhalsa/GoogleDriveApp.git
   cd GoogleDriveApp
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   python wsgi.py
   ```
- The application will start and be accessible at http://localhost:5002
   

---
## Assumptions or Design Decisions Made
1. ##### MVC Structure
- This application is organized into models, views, and controllers for better maintainability and separation of concerns.

2. ##### Dockerization
- Containerized the application to simplify deployment and ensure consistency across environments.

3. ##### Adherence to SOLID Principles
- This application is designed with the SOLID principles of object-oriented programming in mind:

    1. **Single Responsibility Principle (SRP)**  
   - Each class and function has a single responsibility.  
     - `DriveController`: Handles all operations related to Google Drive (list, upload, download, delete).  
     - `GoogleDriveFile`: Represents a file with attributes and utility methods.  
     - `auth_routes` and `drive_routes`: Separately handle authentication and file operation routes.  
     - `config.py`: Centralizes configuration management.

    2. **Open/Closed Principle (OCP)**  
   - The system is open for extension but closed for modification.

    4. **Interface Segregation Principle (ISP)**  
   - The system avoids forcing clients to depend on methods they do not use.  

    5. **Dependency Inversion Principle (DIP)**  
    - High-level modules do not depend on low-level modules; both depend on abstractions. (i.e. `DriveController` and configuration values like `client_secret.json`, scopes, etc.)

By following these principles, the application is modular, maintainable, and easy to extend for future enhancements. 
##### **Furthermore, this code is fully commented to explain all logic being done.**

---

## Testing
##### The application includes both ***unit*** and ***integration*** tests to ensure functionality.

- #### Running Tests
 1. Make sure you have installed the dependencies as mentioned in the Installation section. (use the included requirements.txt)
 2. Run the tests with `pytest` in the `tests/` directory

- #### Test Structure
 1. **Unit Tests:** Located in tests/unit/, these tests cover individual components like controllers and models.
 2. **Integration Tests:** Located in tests/integration/, these tests verify the interactions between different parts of the application.