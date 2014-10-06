#include<iostream>

using namespace std;

class Solution {
public:
  string longestPalindrome(string s) {
    const int n = s.size();
    bool f[n][n];
    fill_n(&f[0][0], n * n, false);
    size_t max_len = 1, start = 0;

    for (size_t j = 0; j < n; j++) {
      f[j][j] = true;
      for (size_t i = 0; i < j; i++) {
        f[i][j] = (s[i] == s[j] && (j - i <= 2 || f[i + 1][j - 1]));
        if (f[i][j] && max_len < (j - i + 1)) {
          max_len = j - i + 1;
          start = i;
        }
      }
    }
    return s.substr(start, max_len);
  }
};

void main() {
  Solution s = new Solution();
}










