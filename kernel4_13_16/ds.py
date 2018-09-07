from kernel4_13_16.helper import Helper

# class used by "USER"
class Process():
    def __init__(self, task):
        self.pid = task.get_pid()
        self.name = task.get_name()

        self.runtime = []
        self.period = []
        self.in_stamp = []
        self.out_stamp = []

        self.start = 0
        self.end = 0
        self.running = False

        self.waker = []
        self.wakee = []

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_runtime(self):
        return self.runtime

    def get_period(self):
        return self.period

    def get_runtime_average(self):
        if len(self.runtime) == 0:
            return 0
        return sum(self.runtime) / float(len(self.runtime))

    def get_runtime_max(self):
        if len(self.runtime) == 0:
            return 0
        return max(self.runtime)

    def get_runtime_min(self):
        if len(self.runtime) == 0:
            return 0
        return min(self.runtime)

    def get_runtime_dispersion(self):
        if len(self.runtime) == 0:
            return 0

        vsum = 0
        mean = self.get_runtime_average()
        for r in self.runtime:
            vsum = vsum + (r - mean) ** 2
        return (vsum/float(len(self.runtime)))

    def get_period_average(self):
        if len(self.period) == 0:
            return 0
        return sum(self.period) / float(len(self.period))

    def get_period_max(self):
        if len(self.period) == 0:
            return 0
        return max(self.period)

    def get_period_min(self):
        if len(self.period) == 0:
            return 0
        return min(self.period)

    def get_period_dispersion(self):
        if len(self.period) == 0:
            return 0

        vsum = 0
        mean = self.get_period_average()
        for r in self.period:
            vsum = vsum + (r - mean) ** 2
        return (vsum/float(len(self.period)))

    def get_in_stamp(self):
        return self.in_stamp

    def get_out_stamp(self):
        return self.out_stamp

    def get_wakers(self):
        return self.waker

    def get_wakees(self):
        return self.wakee

    @staticmethod
    def find_or_create(list, from_to):
        process_from = Process.__find_or_create(list, from_to.get_task_from())
        process_to = Process.__find_or_create(list, from_to.get_task_to())
        return process_from, process_to

    @staticmethod
    def __find_or_create(list, task):
        tmp = Process(task)
        for process in list:
            if process.pid == tmp.pid:
                return process

        list.append(tmp)
        return tmp

    @staticmethod
    def apply_switch(list, switch):
        process_from, process_to = Process.find_or_create(list, switch)
        process_from.calculate_runtime(switch)
        process_to.calculate_period(switch)

    @staticmethod
    def apply_wakeup(list, wakeup):
        process_from, process_to = Process.find_or_create(list, wakeup)
        process_from.wakee.append(process_to.get_name())
        process_to.waker.append(process_from.get_name())

    # process is switch [from]
    def calculate_runtime(self, switch):
        self.end = switch.get_timestamp()
        self.out_stamp.append(self.end)
        self.running = False
        if self.start != 0:
            self.runtime.append(self.end - self.start)

    # process is switch [to]
    def calculate_period(self, switch):
        new_start = switch.get_timestamp()
        self.in_stamp.append(new_start)
        self.running = True
        if self.start != 0:
            self.period.append(new_start - self.start)
        self.start = new_start

    def __repr__(self):
        return "[{}]".format(self.name) + \
            "\nIN_STAMP: " + str(self.in_stamp) + \
            "\nOUT_STAMP: " + str(self.out_stamp) + \
            "\nRUNTIME: " + str(self.runtime) + \
            "\nPERIOD: " + str(self.period) + \
            "\nWAKER: " + str(self.waker) + \
            "\nWAKEE: " + str(self.wakee)

'''
    class Task: class used on parsing
    form: {task_name} [{priority}] {state}
    word: 1-2         1            0-1+ (like D or D|W)

    Task -converted-> Process
'''
class Task():
    def __init__(self, strs):
        if Helper.is_status(strs[-1]):
            self.status = strs[-1]
            self.priority = Helper.remove_brackets(strs[-2])
            self.name = Helper.join_array(strs, 0, len(strs)-2)
        else:
            self.status = ""
            self.priority = Helper.remove_brackets(strs[-1])
            self.name = Helper.join_array(strs, 0, len(strs)-1)

    def get_name(self):
        return self.name

    def get_pid(self):
        return int(self.name.split(":")[-1])

    def __repr__(self):
        return "name={} prio={} status={}".format(
            self.name,
            self.priority,
            self.status
        )
