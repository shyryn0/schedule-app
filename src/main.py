class ScheduleManager:
    def __init__(self):
        self.schedule = {}

    def add_lesson(self, day: str, lesson: str):
        if not day or not lesson:
            raise ValueError("День недели и название предмета не могут быть пустыми.")
        day = day.capitalize()
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append(lesson)
        return True

    def get_lessons(self, day: str):
        day = day.capitalize()
        return self.schedule.get(day, [])

    def clear_schedule(self):
        self.schedule.clear()
        return True