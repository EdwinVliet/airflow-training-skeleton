from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='dag_2_training_id',
    default_args=args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
)

def print_context(execution_date, **context):
    print(execution_date)

PythonOp = PythonOperator(
    task_id='PythonOp',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)

BashOp_1 = BashOperator(
    task_id='BashOp_1',
    bash_command='sleep 1',
    dag=dag,
)

BashOp_2 = BashOperator(
    task_id='BashOp_2',
    bash_command='sleep 5',
    dag=dag,
)

BashOp_3 = BashOperator(
    task_id='BashOp_3',
    bash_command='sleep 10',
    dag=dag,
)

DummyOp = DummyOperator(
    task_id='DummyOp',
    dag=dag,
)

PythonOp >> [BashOp_1,BashOp_2,BashOp_3] >> DummyOp 
