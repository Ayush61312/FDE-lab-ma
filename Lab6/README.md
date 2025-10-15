# Workflow Orchestration using Apache Airflow

### Experiment No: 6  
**Name:** Atreyaa Subramanya A V S  
**USN:** 1RVU23CSE088 

---

## Objective

This exercise provides hands-on experience with **Apache Airflow**, an open-source platform for programmatically creating, scheduling, and managing workflows.  
You will learn to design and deploy **Directed Acyclic Graphs (DAGs)** to automate **ETL (Extract, Transform, Load)** processes used in data engineering applications.

---

## Outcomes

- Gain an understanding of the **core components and architecture** of Apache Airflow.  
- Learn to **define DAGs and tasks** programmatically using **Python**.  
- Set up and run **Airflow locally using Docker**, and explore its **web interface**.  
- Execute **ETL pipelines** using Airflow’s **operators** and **scheduler**.

---

## Requirements

- **Apache Airflow** (Docker installation setup)  
- **Docker** and **Docker Compose**  
- **Python** environment  
- **PostgreSQL** or **MySQL** for metadata storage  

---

## Setup and Installation

### Step 1: Build and Start Airflow

```bash
docker build -t airflowsqlserver -f Dockerfile --no-cache .
docker-compose up
```

Once the containers start successfully, access the Airflow Web UI at:  
**http://localhost:9099/home**

---

## Understanding Airflow Components

| Component | Description |
|------------|--------------|
| **DAG (Directed Acyclic Graph)** | Defines the structure of your workflow as a graph of tasks. |
| **Task** | A unit of work executed by an operator. |
| **Worker** | Executes the actual commands or scripts. |
| **Web Server (UI)** | Dashboard for monitoring DAGs and task runs. |
| **Metadata Database** | Stores the state and execution history of DAGs. |

---

## Creating and Running a Sample DAG

1. Navigate to the Airflow DAGs directory.  
2. Create a new Python file, e.g. `code.py`.  
3. Define your DAG with `extract`, `transform`, and `load` tasks.  
4. Set task dependencies, for example:

   ```python
   extract >> transform >> load
   ```

5. Deploy the DAG and monitor its execution in the **Airflow Web UI**.

---

## Database Schema Setup

Execute the following SQL commands in your Airflow-connected database:

```sql
CREATE SCHEMA IF NOT EXISTS etl_staging;
GRANT ALL PRIVILEGES ON SCHEMA etl_staging TO etl;
```

---

## Screenshots

Include relevant screenshots from the `images/` folder, such as:

- Airflow Web UI  
- DAG execution graph  
- Task logs or success states  

Example (Markdown syntax):

```markdown
![Airflow UI](images/image_2.png)
![DAG Run](images/image_3.png)
```

---
