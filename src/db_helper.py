import mysql.connector

class DbHelper:
    def __init__(self):
        # Establishing connection to MySQL db
        self.connection = mysql.connector.connect(
            host="localhost",
            user="#####",
            password="#######",
            database="company"
        )
        self.cursor = self.connection.cursor()

    def get_maximum_salary(self):
        
        # its SQL query to fetch the maxmum salary
        self.cursor.execute("SELECT MAX(salary) FROM employee")
        max_salary = self.cursor.fetchone()[0]  # Fetch the first row and first column value
        return max_salary

    def get_minimum_salary(self):
        
        # Execute SQL query to fetch the minimum salary
        self.cursor.execute("SELECT MIN(salary) FROM employee")
        min_salary = self.cursor.fetchone()[0]  # Fetch the first row and first column value
        return min_salary

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print("Maximum Salary:", max_salary)
    print("Minimum Salary:", min_salary)
