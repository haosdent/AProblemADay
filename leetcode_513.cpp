class Solution {
public:
  vector<int> postorderTraversal(TreeNode *root) {
    vector<int> result;
    TreeNode *p = root;
    TreeNode *q;
    stack<TreeNode *> s;

    while (!s.empty() || p != nullptr) {
      if (p != nullptr) {
        s.push(p);
        p = p->left;
      } else {
        p = s.top();
        if (p->right == q || p->right == nullptr) {
          s.pop();
          q = p;
          result.push_back(p->val);
          p = nullptr;
        } else {
          p = p->right;
          q = nullptr;
        }
      }
    }
    return result;
  }
};
