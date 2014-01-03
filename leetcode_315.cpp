class Solution {
public:
  int lengthOfLastWord(const char *s) {
    const string str(s);
    auto first = find_if(str.rbegin(), str.rend(), ::isalpha);
    auto last = find_if_not(str.rbegin(), str.rend(), ::isalpha);
    return distance(first, last);
  }
}


















