import numpy as np
from itertools import product

class Player(object):
    """

    """
    def __init__(self, policy='standard'):
        self.square = np.empty((4,4))
        self.square[:] = np.nan
        self.drawn = None
        self.inds = list(product(range(4), range(4)))
        self.lessdict = {i: [j for j in self.inds if
                             (j[0]==i[0] and j[1] < i[1]) or
                             (j[1]==i[1] and j[0] < i[0])] for i in self.inds}
        self.grtrdict = {i: [j for j in self.inds if
                             (j[0]==i[0] and j[1] > i[1]) or
                             (j[1]==i[1] and j[0] > i[0])] for i in self.inds}
        self.candidates = self.calculate_candidates()
        self.num_candidates = self.calc_num_candidates(self.candidates)
        self.nanhelper = lambda arr: [str(int(x)) if not np.isnan(x) else "  " for x in arr]
        self.square_display = self.display_prep()
        self.ideal = np.array([[1,     4.167,  7.333,  10.5],
                               [4.167, 7.333,  10.5,   13.67],
                               [7.333, 10.5,   13.667, 16.83],
                               [10.5,  13.667, 16.833, 20]])


    def display_prep(self):
        lines = " ---- ---- ---- ---- "
        line_a = "| {0:>2} | {1:>2} | {2:>2} | {3:>2} |".format(nanhelper(*self.square[0]))
        line_b = "| {0:>2} | {1:>2} | {2:>2} | {3:>2} |".format(nanhelper(*self.square[1]))
        line_c = "| {0:>2} | {1:>2} | {2:>2} | {3:>2} |".format(nanhelper(*self.square[2]))
        line_d = "| {0:>2} | {1:>2} | {2:>2} | {3:>2} |".format(nanhelper(*self.square[3]))
        return [lines, line_a, lines, line_b, lines, line_c, lines, line_d, lines]

    def display_square(self):
        for line in self.display_prep:
            print(line)

    def update(self):
        self.candidates = self.calculate_candidates()
        self.num_candidates = self.calc_num_candidates(self.candidates)

    def calculate_candidates(self):
        """Calculates how many suitable cards for each position remain in the deck/table,
           and also how likely one is to draw one."""
        candidates = {i: [] for i in self.inds}
        for ind in self.inds:
            lowest = np.nanmax(self.square[self.lessdict[ind]]) + 1
            highest = np.nanmin(self.square[self.grtrdict[ind]])
            candidates[ind] = range(lowest, highest)
        return candidates

    def calc_num_candidates(self, candidates):
        return {i: len(v) for i, v in candidates.items()}

    def summarize(self, num_cands):
        empty = np.where(np.isna(self.square))
        num_cands = {i: num_cands for i in empty}
        ncands_arr = np.array(num_cands.values())
        blanks = len(empty)
        min_nc = np.min(ncands_arr)
        max_nc = np.max(ncands_arr)
        mean_nc = np.mean(ncands_arr)
        med_nc = np.median(ncands_arr)
        return np.array([blanks, min_nc, max_nc, mean_nc, med_nc])
        #TODO: policy NN using input vector for change in each indicator
        #TODO: then run this for each card's optimal move and the expectation from the deck







    def loc_policy(self):
        pass

    def draw_policy(self):
        pass