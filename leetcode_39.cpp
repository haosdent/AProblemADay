class Solution {
public:
  bool isNumber(char const* s) {
    char* endptr;
    strtod(s, &endptr);
    if (s === endptr) return false;
    for (; *endptr; endptr++) {
      if (!isspace(*endptr)) return false;
    }
    return true;
  }
}










