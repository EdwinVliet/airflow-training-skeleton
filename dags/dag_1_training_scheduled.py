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
    dag_id='dag_1_training_scheduled_id',
    default_args=args,
    schedule_interval='@daily',
    dagrun_timeout=timedelta(minutes=60),
)

task_1 = DummyOperator(
    task_id='run_task_1',
    dag=dag,
)

task_2 = DummyOperator(
    task_id='run_task_2',
    dag=dag,
)

task_3 = DummyOperator(
    task_id='run_task_3',
    dag=dag,
)

task_4 = DummyOperator(
    task_id='run_task_4',
    dag=dag,
)

task_5 = DummyOperator(
    task_id='run_task_5',
    dag=dag,
)

task_1 >> task_2 >> [task_3, task_4] >> task_5
