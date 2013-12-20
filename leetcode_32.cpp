class Solution {
public:
  char *strStr(const char *heystack, const char *needle) {
    if (!*needle) return heystack;

    const char *p1;
    const char *p2;
    const char *p1_advance = heystack;

    for (p2 = &needle[1]; *p2; p2++) {
      p1_advance++;
    }

    for (p1 = heystack; *p1_advance; p1_advance++) {
      const char *p1_old = p1;
      p2 = needle;
      while (*p1 && *p2 && *p1 == *p2) {
        p1++;
        p2++;
      }
      if (!*p2) return p1_old;
      p1 = p1_old + 1;
    }

    return nullptr;
  }
}


















