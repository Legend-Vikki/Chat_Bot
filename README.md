# Chat Assistant for SQLite Database

This project is a Python-based chat assistant that interacts with an SQLite database. The assistant allows users to ask natural language queries related to employees and departments. The assistant parses these queries, converts them into SQL queries, fetches data from the database, and responds with clear, formatted answers.

## Objective
The goal of this project is to build a chat assistant that can:
- Accept natural language queries.
- Convert those queries into SQL queries.
- Retrieve data from an SQLite database.
- Return well-formatted, meaningful responses to the user.

## Database Schema

The application interacts with an SQLite database containing two tables:

### Table 1: `Employees`

| ID | Name    | Department  | Salary | Hire_Date   |
|----|---------|-------------|--------|-------------|
| 1  | Alice   | Sales      | 50000  | 2021-01-15  |
| 2  | Bob     | Engineering | 70000  | 2020-06-10  |
| 3  | Charlie | Marketing  | 60000  | 2022-03-20  |

### Table 2: `Departments`

| ID | Name        | Manager |
|----|-------------|---------|
| 1  | Sales      | Alice   |
| 2  | Engineering| Bob     |
| 3  | Marketing  | Charlie |

## Supported Queries
The chat assistant supports the following types of queries:

- **“Show me all employees in the [department] department.”**
- **“Who is the manager of the [department] department?”**
- **“List all employees hired after [date].”**
- **“What is the total salary expense for the [department] department?”**
- **And more...**

### Example Queries:
- “Show me all employees in the Sales department.”
- “Who is the manager of the Engineering department?”
- “List all employees hired after 2021-01-01.”
- “What is the total salary expense for the Marketing department?”

## Error Handling
- The assistant gracefully handles invalid queries and returns meaningful error messages when no results are found.
- The assistant can handle incorrect department names or invalid input formats, ensuring smooth user interaction.

## Functionality

The assistant is built using **Flask** and interacts with the SQLite database to fetch data based on user queries. Here’s a high-level breakdown of how the assistant works:

1. The user submits a query through the web interface.
2. The assistant processes the query, checking for key phrases and extracting relevant information (e.g., department names, dates).
3. It converts the query into an appropriate SQL query.
4. The database is queried for the relevant data.
5. The assistant returns a formatted response to the user.

## Deployment

The assistant is deployed as a web application, and you can access it via a public URL. Once deployed, you can interact with the assistant by typing in your queries, and it will respond with answers based on the database.

## How to Run the Project Locally

### Requirements:
- Python 3.8 or later
- Flask (for the web interface)
- SQLite (for the database)

### Steps to Run:

1. **Clone the repository**:

2. **Navigate to the project directory**:

3. **Create a virtual environment**:

4. **Activate the virtual environment**:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. **Install dependencies**:

6. **Run the application**:

7. **Access the chat assistant**:  
Open a web browser and go to `http://127.0.0.1:5000/` to start interacting with the assistant.

## Known Limitations
- The assistant is designed to handle a limited set of queries, which are predefined and focused on the given database schema.
- The assistant doesn't have advanced natural language processing capabilities and might fail for queries with complex sentence structures or ambiguous wording.
- Error handling for malformed queries can be improved in future versions.

## Suggestions for Improvement
- Expand the query types to handle more complex interactions.
- Integrate more robust natural language processing libraries to understand a wider range of queries.
- Add authentication to secure access to the application.

## Code Repository

You can access the source code and database file at the following GitHub repository:
[GitHub Repository](https://github.com/Legend-Vikki/Chat_Bot)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
