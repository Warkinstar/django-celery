from django.urls import reverse
from tasks import sample_tasks
from unittest.mock import patch
import json


def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


"""full integration test"""


def test_task_status(client):
    response = client.post(reverse("run_task"), {"type": 0})
    content = json.loads(response.content)
    task_id = content["task_id"]
    assert response.status_code == 202
    assert task_id

    response = client.get(reverse("get_status", args=[task_id]))
    content = json.loads(response.content)
    assert content == {
        "task_id": task_id,
        "task_status": "PENDING",
        "task_result": None,
    }
    assert response.status_code == 200

    while content["task_status"] == "PENDING":
        response = client.get(reverse("get_status", args=[task_id]))
        content = json.loads(response.content)
    assert content == {
        "task_id": task_id,
        "task_status": "SUCCESS",
        "task_result": True,
    }


"""В вашем примере, код @patch("tasks.sample_tasks.create_task.run") указывает, что метод create_task.run из 
модуля tasks.sample_tasks будет заменен фиктивной версией во время выполнения теста. Это делается с целью ускорения 
выполнения тестов, так как задачи будут выполняться внутри теста без задержки, которую обычно вызывает выполнение 
задачи через Celery."""


@patch("tasks.sample_tasks.create_task.run")
def test_task(mock_run):
    assert sample_tasks.create_task.run(1)
    sample_tasks.create_task.run.assert_called_once_with(1)

    assert sample_tasks.create_task.run(2)
    assert sample_tasks.create_task.run.call_count == 2

    assert sample_tasks.create_task.run(3)
    assert sample_tasks.create_task.run.call_count == 3


"""Simple test"""


def test_task():
    assert sample_tasks.create_task.run(1)
    assert sample_tasks.create_task.run(2)
    assert sample_tasks.create_task.run(3)
