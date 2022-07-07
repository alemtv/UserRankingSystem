class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.rank_list = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]

    def __str__(self):
        str_txt = 'Rank: ' + str(self.rank) + '\n'
        str_txt += 'Progress: ' + str(self.progress)
        return str_txt

    def inc_progress(self, task_rank):

        if not self.validate_rank(task_rank):
            raise Exception("Rank value is not allowed")

        if self.rank == max(self.rank_list):
            # A user cannot progress beyond rank 8
            self.progress = 0
            return

        self.progress = self.progress + self.calc_progress(task_rank)

        while self.progress >= 100 and self.rank < max(self.rank_list):
            new_index = self.rank_list.index(self.rank) + 1
            self.rank = self.rank_list[new_index]
            self.progress -= 100

        if self.rank >= 8:
            self.progress = 0

        return

    def validate_rank(self, in_rank):
        if in_rank in self.rank_list:
            return True
        else:
            return False

    def calc_progress(self, task_rank):
        d = self.rank_list.index(task_rank) - self.rank_list.index(self.rank)
        if d == 0:
            # Completing an activity that is ranked the same as that of the user's will be worth 3 points
            return 3
        elif d < -1:
            # Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
            return 0
        elif d < 0:
            # Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
            return 1
        else:
            return 10 * d * d

