import os
import sys

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.main import ScheduleManager


def test_add_and_get_lesson():
    manager = ScheduleManager()
    assert manager.add_lesson("Понедельник", "Прикладные аспекты DevOps") is True
    lessons = manager.get_lessons("понедельник")
    assert "Прикладные аспекты DevOps" in lessons
    assert len(lessons) == 1


def test_add_invalid_lesson():
    manager = ScheduleManager()
    with pytest.raises(ValueError):
        manager.add_lesson("", "Математика")


def test_clear_schedule():
    manager = ScheduleManager()
    manager.add_lesson("Вторник", "Физика")
    manager.clear_schedule()
    assert len(manager.get_lessons("Вторник")) == 0