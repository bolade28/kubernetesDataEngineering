from airflow import DAG
from airflow.operators.bash import BashOperator
from datatime import datetime, timedelta

default_args = {
    'owner': 'bren_investech.com',
    'start_date': datetime(2025,1, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
    'catchup': false
}

dag = DAG(
    'hello_world',
    default_args = default_args,
    schedule = timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command = 'echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_dml',
    bash_command = 'echo "Hello princess"',
    dag = dag
)

t1 >> t2
