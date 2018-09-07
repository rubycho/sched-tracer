from kernel4_13_16.helper import Helper

'''
    sched_event: base parser
    class that parses front part of event log

    form: {task_name} [{cpu}] {timestamp}: {event}
    word: 1           1       1            1
'''
class SchedEvent():
    def __init__(self, str):
        splitted = str.split()
        if len(splitted) < 4:
            raise TooLessArgumentException

        self.original = str
        self.splitted = splitted
        self.task_name = splitted[0]
        self.on_cpu = int(Helper.remove_brackets(splitted[1]))
        self.timestamp = float(Helper.remove_colon(splitted[2]))
        self.event = Helper.remove_colon(splitted[3])

    def get_splitted(self):
        return self.splitted

    def get_task_name(self):
        return self.task_name

    def get_cpu(self):
        return self.on_cpu

    def get_timestamp(self):
        return self.timestamp

    def get_event(self):
        return self.event

    def __repr__(self):
        return "task={} cpu={} timestamp={} event={}".format(
            self.task_name,
            self.on_cpu,
            self.timestamp,
            self.event
        )

class TooLessArgumentException(Exception):
    pass

class EventUnmatchException(Exception):
    pass
