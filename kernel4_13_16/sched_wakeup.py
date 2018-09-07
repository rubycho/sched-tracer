from kernel4_13_16.helper import Helper
from kernel4_13_16.ds import Task

from kernel4_13_16.sched_event import SchedEvent, EventUnmatchException

'''
    massive_intr-2819  [001]  1124.611128: sched_waking:         comm=trace-cmd pid=2866 prio=120 target_cpu=001
    massive_intr-2819  [001]  1124.611130: sched_wakeup:         trace-cmd:2866 [120] success=1 CPU:001

    event sched_wakeup
    form: {task_name} [{cpu}] {timestamp}: {event}: {waked task name:pid} [{priority}] success={success} CPU:{cpu}
    word: 1           1       1            1        1                     1            1                 1
'''
class SchedWakeup(SchedEvent):
    def __init__(self, str):
        super().__init__(str)
        splitted = super().get_splitted()

        if super().get_event() != 'sched_wakeup':
            raise EventUnmatchException

        dash_name = super().get_task_name()
        dash = dash_name.rfind('-')
        new_name = dash_name[:dash] + ':' + dash_name[dash+1:]

        # prio default to 999
        self.task_from = Task([new_name, '[999]'])
        self.task_to = Task([splitted[-4], splitted[-3]])

    def get_task_from(self):
        return self.task_from

    def get_task_to(self):
        return self.task_to

    def __repr__(self):
        return super().__repr__() + \
            "\nfrom: " + self.task_from.__repr__() + \
            "\nto: " + self.task_to.__repr__()
