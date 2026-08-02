class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        pref = [0]
        for x in tasks:
            pref.append(pref[-1] + x)
        total = pref[-1]
        pos = 0
        done = 0
        ans = []
        for s in shifts:
            work = pref[pos] + done + s
            if work >= total:
                ans.append(0)
                pos = 0
                done = 0
                continue
            pos = bisect_right(pref, work) - 1
            done = work - pref[pos]
            ans.append(n - pos)
        return ans