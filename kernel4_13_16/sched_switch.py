from kernel4_13_16.helper import Helper
from kernel4_13_16.ds import Task

from kernel4_13_16.sched_event import SchedEvent, EventUnmatchException

'''
    event sched_switch
    form: {task_name} [{cpu}] {timestamp}: {event}: {from(task)} ==> {to(task)}
    word: 1           1       1            1        3-4          1   2-4
'''
class SchedSwitch(SchedEvent):
    def __init__(self, str):
        super().__init__(str)
        splitted = super().get_splitted()

        if super().get_event() != 'sched_switch':
            raise EventUnmatchException

        idx = Helper.find_arrow(splitted)
        self.task_from = Task(splitted[4:idx])
        self.task_to = Task(splitted[idx+1:len(splitted)])

    def get_task_from(self):
        return self.task_from

    def get_task_to(self):
        return self.task_to

    def __repr__(self):
        return super().__repr__() + \
            "\nfrom: " + self.task_from.__repr__() + \
            "\nto: " + self.task_to.__repr__()
