class Helper():
    @staticmethod
    def remove_colon(str):
        return str.replace(":", "")

    @staticmethod
    def remove_brackets(str):
        return str.replace("[", "").replace("]", "")

    @staticmethod
    def is_status(str):
        if len(str) == 1:
            return True

        if len(str) < 1:
            return False

        strs = str.split("|")
        if len(strs) < 1:
            return False

        for s in strs:
            if len(s) != 1:
                return False
        return True

    @staticmethod
    def find_arrow(strs):
        for idx, str in enumerate(strs):
            if str == "==>":
                return idx
        return -1

    @staticmethod
    def join_array(strs, start, end):
        return " ".join(strs[start:end])
