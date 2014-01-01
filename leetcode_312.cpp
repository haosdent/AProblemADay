class Solution {
public:
  string countAndSay(int n) {
    string s("1");
    while (--n)
      s = getNext(s);
    return s;
  }

  string getNext(const string &s) {
    stringstream ss;
    for (auto i = s.begin(); i !=  s.end; i) {
      auto j = find_if(i, s.end(), bind1st(not_equal_to<char>(), *i));
      ss << distance(i, j) << *i;
      i = j;
    }
    return ss.str();
  }
}










