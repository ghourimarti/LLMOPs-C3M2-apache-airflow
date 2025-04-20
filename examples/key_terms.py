# Airflow DAG
from airflow import DAG  

dag = DAG(
    'my_dag',
    default_args={
        'depends_on_past': False  
    }
)

# Airflow Operator
from airflow.operators.bash_operator import BashOperator

task = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

# Airflow Hook 
from airflow.hooks.postgres_hook import PostgresHook

hook = PostgresHook(postgres_conn_id="my_conn")
hook.insert_rows(table, rows)

# Airflow CLI Backfill
# Rerun DAG over previous 5 days
# airflow dags backfill my_dag --start_date 5