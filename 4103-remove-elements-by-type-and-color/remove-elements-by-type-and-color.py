class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        n = len(types)
        st = []
        for i in range(n):
            t = types[i]
            c = colors[i]
            if st and st[-1][0] == (t, c):
                st[-1][1] += 1
            else:
                st.append([(t, c), 1])
            while st and st[-1][1] >= groupSize[st[-1][0][0]]:
                target_type = st[-1][0][0]
                required = groupSize[target_type]
                if st[-1][1] == required:
                    st.pop()
                else:
                    st[-1][1] -= required
                while len(st) >= 2 and st[-1][0] == st[-2][0]:
                    combined_count = st.pop()[1]
                    st[-1][1] += combined_count
        return len(st) == 0