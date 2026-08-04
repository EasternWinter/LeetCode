class SummaryRanges {
set<int> st;
public:
    SummaryRanges() {
        
    }
    
    void addNum(int value) {
        st.insert(value);
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ans;
        int prev = -1;
        for (int x : st) {
            if (prev == -1) {
                ans.push_back({x, x});
            }
            else {
                if (prev + 1 == x) {
                    (ans.back())[1] = x;
                }
                else {
                    ans.push_back({x, x});
                }
            }
            prev = x;
        }
        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */