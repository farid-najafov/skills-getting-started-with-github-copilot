from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities():
    initial_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(initial_activities))