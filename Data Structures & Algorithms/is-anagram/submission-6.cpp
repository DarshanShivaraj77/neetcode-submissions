class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()) return false;
        unordered_map<char,int> mp;
        for(char st: s){
            mp[st]++;
        }
        for(char ts: t){
            if(mp[ts]<=0){
                return false;
            }
            mp[ts]--;
        }
        return true;
    }
};
