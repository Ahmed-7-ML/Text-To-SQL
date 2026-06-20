# 🗄️ Text-to-SQL AI Engine (Multi-Table Faculty Database)

An advanced GenAI-powered application that translates natural language questions (English/Arabic) into executable SQL queries, runs them against a relational SQLite database, and visualizes the results instantly. Powered by the latest **Google GenAI SDK (Gemini 2.5 Flash)** and **Streamlit**.

---

## 📸 Application Preview

Below is a live preview of the application dashboard, showing the live schema visualizer, interactive database preview, and the generated SQL results.

![Application Dashboard](image.png)

---

## ✨ Key Features

- **Natural Language to SQL:** Seamlessly converts complex user questions into optimized SQL commands.
- **Multi-Table Relational Schema:** Supports advanced database structures with `FOREIGN KEY` constraints and cross-table `JOIN` operations.
- **Live Database Preview:** Displays real-time interactive previews of the database tables (`Students` & `Marks`) using Pandas DataFrames right inside the UI.
- **Production-Ready UI/UX:** Built with a modern dark-themed interface, using separate structural tabs for *Database Records* and *Generated SQL Code*.
- **Robust Prompt Engineering:** Implements strict guardrails to prevent LLM hallucinations regarding column and table naming mismatches.

---

### 🏢 Real-World Use Cases & Enterprise Value

In modern enterprises, data is stored in massive relational databases (SQL Server, PostgreSQL, Oracle). However, non-technical decision-makers (CEOs, Sales Managers, HR Heads) cannot write SQL queries to extract insights.

This project solves the **"Data Democratization"** problem by allowing anyone in the company to securely text the database in plain English or Arabic and get instant, live business analytics without waiting for a data analyst.

## 🔒 Production Scaling & Security Roadmap (Enterprise Architecture)

To transition this prototype into a production-grade enterprise application, the system is designed to scale across the following three pillars:

### 1. Advanced Security & Data Privacy (Local LLM Deployment)

- **Problem:** Sending sensitive company financial or employee records to external Cloud APIs (like OpenAI or Google Cloud) violates data compliance (GDPR/HIPAA).
- **Enterprise Solution:** The application architecture allows seamless migration to **Locally Hosted LLMs** (e.g., Llama 3.1 8B/70B, Mistral, or Qwen) running entirely on the company's internal secure servers (On-Premises Infrastructure) using tools like **Ollama** or **vLLM**. This ensures **Zero Data Leakage**, as no company data ever leaves the internal secure firewall.

### 2. Robust Authentication & Authorization (RBAC)

To prevent unauthorized access and protect database integrity, the application scales by implementing a **Role-Based Access Control (RBAC)** security layer:

- **🔐 User Authentication:** Secure login screen requiring a unique username, password, and Multi-Factor Authentication (MFA) powered by frameworks like Auth0 or FastAPI Users.
- **🛡️ Role-Based Authorization:**
  - **Admin Role:** Full Access (Read, Write, Update, Delete). Admins can execute structural schema modifications, insert mock evaluation records, and view high-level sensitive logs.
  - **Standard User Role (Viewer):** Strict **Read-Only Access** via highly localized SQL Views. The LLM prompt constraint will strictly block any destructive keywords (`DROP`, `DELETE`, `TRUNCATE`, `ALTER`). This guarantees non-technical users cannot corrupt or break the production database.

### 3. Enterprise Database Scaling

- **Migration Path:** The modular code design decoupled in the `src/` folder allows immediate scaling from a local `SQLite3` environment to enterprise-scale databases such as **Microsoft SQL Server**, **PostgreSQL**, **MySQL**, or **Amazon RDS**.
- **Execution:** Simply swapping the database URI driver in `src/db_manager.py` enables the application to map complex schemas across thousands of production tables with absolute zero changes to the core Streamlit interface.

---

## 🏗️ System Architecture & Workflow

1. **User Input:** User type a question in plain text (e.g., *"Give me the marks of Ahmed Akram in Machine Learning"*).
2. **LLM Translation:** Gemini 2.5 Flash parses the question along with the injected database schema context and structural constraints.
3. **SQL Generation:** The AI agent outputs a raw, valid SQL query string.
4. **Database Execution:** The Python backend securely executes the query on the local `Faculty.db` (SQLite3).
5. **UI Rendering:** Streamlit fetches the raw tuples, wraps them into a DataFrame, and populates the reactive dashboard.

---

## 🗄️ Database Schema Blueprint

The application connects to a localized `Faculty.db` structured as follows:

### 1. `Students` Table (Primary)

| Column Name | Data Type   | Attributes                 |
| :---------- | :---------- | :------------------------- |
| `Id`      | INTEGER     | PRIMARY KEY, AUTOINCREMENT |
| `Name`    | VARCHAR(25) | UNIQUE, NOT NULL           |
| `DoB`     | TEXT        | Date of Birth              |
| `Section` | INTEGER     | Class Section Number       |

### 2. `Marks` Table (Secondary)

| Column Name   | Data Type   | Attributes                       |
| :------------ | :---------- | :------------------------------- |
| `MarkId`    | INTEGER     | PRIMARY KEY, AUTOINCREMENT       |
| `StudentId` | INTEGER     | FOREIGN KEY ➡️`Students(Id)` |
| `Subject`   | VARCHAR(50) | Subject Title                    |
| `Score`     | INTEGER     | Exam Grade                       |

---

## 🚀 Getting Started (Initial Setup)

This project manages its virtual environment and dependencies seamlessly using **Poetry**.

### Prerequisites

- Python `^3.10` or `^3.11`
- [Poetry](https://python-poetry.org/) installed on your machine.
- Google AI Studio API Key ([Get it here](https://aistudio.google.com/)).

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/your-username/text-to-sql-ai-engine.git](https://github.com/your-username/text-to-sql-ai-engine.git)
   cd text-to-sql-ai-engine

   ```
2. **Install Dependencies via Poetry:**
   **Bash**

   ```
   poetry install
   ```
3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and append your Gemini API Key:

   ```
   GEMINI_API_KEY=AIzaSyYourActualAPIKeyHere
   ```
4. **Initialize and Populate the Database:**
   Run the database setup script to compile the tables and insert mock evaluation records:
   **Bash**

   ```
   poetry run python db_setup.py
   ```
5. **Launch the Streamlit Application Dashboard:**
   **Bash**

   ```
   poetry run streamlit run app.py
   ```

## 🛠️ Tech Stack Built With

* **Core Language:** Python 3.11
* **GenAI Orchestration:** Google GenAI SDK (`google-genai` 2026 Release)
* **Foundation Model:** Gemini 2.5 Flash
* **Web Interface:** Streamlit (Wide Layout Layout)
* **Data Engineering:** Pandas & SQLite3
* **Environment Management:** Poetry & Pyenv

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

*Developed with 💻 by **Ahmed Akram** - The Triple AI Portfolio.*
