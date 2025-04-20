# Step 1: Install Docker
# Step 2: Install Docker Compose
# Step 3: Create a Docker Compose file
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'

# Step 4: Create directories for DAGs, logs, and plugins
mkdir -p ./dags ./logs ./plugins ./config

# Step 5: Set environment variables
# Step 6: Initialize the database
# Step 7: Start the Airflow services




# Set environment variables
echo -e "AIRFLOW_UID=$(id -u)" > .env

# 
docker-compose up airflow-init

# 
docker-compose up

