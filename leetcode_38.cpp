class Solution {
public:
  string longestCommonPrefix(vector<string> &strs) {
    if (strs.empty()) return "";

    int right_most = strs[0].size() - 1;
    for (int i = 0; i < strs.size(); i++) {
      for (int j = 0; j < right_most + 1; j++) {
        if (strs[i][j] != strs[0][j]) {
          right_most = j - 1;
        }
      }
    }

    return strs[0].substr(0, right_most + 1);
  }
}


















