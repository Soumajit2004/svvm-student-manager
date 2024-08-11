# School Marks Management ERP

This is a simple ERP (Enterprise Resource Planning) system designed for small schools or educational institutions to manage student information and academic performance. The system allows for student registration, profile management, and marks entry for various subjects across multiple tests.

## Features

- Student Registration: Capture essential student details including name, parents' information, and contact details.
- Student Profile: View and manage individual student profiles.
- Marks Entry: Enter and edit marks for different subjects across multiple tests.
- User-friendly Interface: Easy-to-navigate web-based interface for administrators and teachers.

## Technologies Used

- Backend: Python with Flask framework
- Frontend: HTML, CSS
- Database: MySQL

## Requirements

- Python
- Docker

## Setup Locally

1. Clone the repository:
   ```
   git clone https://github.com/Soumajit2004/svvm-student-manager.git
   ```

2. Run MySQL in Docker:
   ```
   docker run -d --name test-mysql -e MYSQL_ROOT_PASSWORD=strong_password -p 3307:3306 mysql
   ```

3. Access the MySQL container:
   ```
   docker exec -it test-mysql bash
   ```

4. Connect to MySQL:
   ```
   mysql --host=127.0.0.1 --port=3307 -u root -p
   ```

5. Create the necessary database and tables by running the migration script:
   
   get it from here: [migration.sql](https://github.com/Soumajit2004/svvm-student-manager/blob/70b947a72138015f44cf59ed4bf5127f8a1a9c32/migration.sql)
   
   ```
   mysql> source [PATH_TO_MIGRATION_SQL_FILE]
   ```

6. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

7. Create a `.env` file in the root directory and add the necessary environment variables. You can use the `.env.example` file in the repository as a template.

8. Run the application:
   - For development:
     ```
     python app.py
     ```
   - For production:
     ```
     gunicorn --bind 0.0.0.0:5000 wsgi:app
     ```

9. Access the application through your web browser at `http://localhost:5000`

For a detailed guide on installing MySQL with Docker, refer to this external resource: [Set Up and Configure MySQL in Docker](https://www.datacamp.com/tutorial/set-up-and-configure-mysql-in-docker)

## Usage

1. Register new students using the registration form.
2. View and edit student profiles.
3. Enter marks for different subjects and tests.
4. View academic performance reports.

## Screenshots

The repository includes several screenshots demonstrating key features of the application:

1. Dashboard Screen
![dashboard](https://github.com/Soumajit2004/svvm-student-manager/blob/f0d324a2c697e206969a64390d50b6b6511553e1/screenshots/dashboard_screen.png?raw=true)

2. Register Screen
![register](https://github.com/Soumajit2004/svvm-student-manager/blob/f0d324a2c697e206969a64390d50b6b6511553e1/screenshots/register_screen.png?raw=true)

3. Student Profile Screen
![profile](https://github.com/Soumajit2004/svvm-student-manager/blob/f0d324a2c697e206969a64390d50b6b6511553e1/screenshots/student_profile_screen.png?raw=true)

4. Select Test Screen
![select_test](https://github.com/Soumajit2004/svvm-student-manager/blob/f0d324a2c697e206969a64390d50b6b6511553e1/screenshots/select_test_screen.png?raw=true)

5. Edit Marks Screen
![edit_marks](https://github.com/Soumajit2004/svvm-student-manager/blob/f0d324a2c697e206969a64390d50b6b6511553e1/screenshots/edit_marks_screen.png?raw=true)

These screenshots provide a visual overview of the system's functionality and user interface.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

Soumajit Ghosh - soumojitghosh02@gmail.com

Project Link: https://github.com/Soumajit2004/svvm-student-manager
