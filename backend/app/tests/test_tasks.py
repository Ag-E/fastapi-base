from app import tasks


def test_example_task():
    task_output = tasks.example_task("Hello World")
    assert task_output == "test task returns Hello World"


def test_calculate_substring_task():
    task_output = tasks.calculate_substring_task(
        "bbbbbbaanwernwrewerwkwerkwerkw23423ergfdfg",
        "c3577920-72c5-48af-bc39-1e1d33ba52ca",
    )
    assert task_output == 8
