# Graph Database Modeling and Querying (Neo4j)

## Summary
This project involves designing and implementing a Graph Database Model in Neo4j for an e-commerce system named ShopSmart. The objective is to represent entities such as Users, Products, Brands, Categories, and Reviews as interconnected nodes. These nodes are linked through relationships like BOUGHT, VIEWED, RATED, and BELONGS_TO.

CRUD (Create, Read, Update, Delete) operations and analytical queries are performed using the Cypher Query Language to evaluate product performance, user activity, and recommendation trends. The project emphasizes how graph databases efficiently handle complex and highly connected datasets.

---

## Tools Used
- Neo4j Desktop
- Neo4j Browser
- Cypher Query Language

---

## Lab Stages

### Stage 1: Installation and Setup
- Install Neo4j Desktop
- Create and start the ShopSmart database
- Access it using Neo4j Browser

### Stage 2: Graph Creation (Data Modeling)
- Define nodes for User, Product, Category, Brand, and Review
- Establish relationships such as :BOUGHT, :VIEWED, :RATED, and :BELONGS_TO
- Validate the graph structure and connections

### Stage 3: Basic Data Retrieval
- Use MATCH, WHERE, RETURN, and WITH for data queries

### Stage 4: Data Modification
- Modify nodes and relationships using SET, MERGE, and REMOVE

### Stage 5: Data Deletion
- Delete data using DELETE and DETACH DELETE commands safely

### Stage 6: Advanced Analytical Queries
- Execute aggregations and pattern analysis with COUNT, SUM, and AVG

---

## Expected Output
- A fully functional ShopSmart graph model
- Successful CRUD and analytical query execution
- Visual representation of relationships in the Neo4j Browser
