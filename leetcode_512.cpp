class Solution {
public:
  vector<int> inorderTraversal(TreeNode *root) {
    vector<int> result;
    const TreeNode *p = root;
    vector<const TreeNode *> s;

    while (!s.empty() || p != nullptr) {
      if (p != nullptr) {
        s.push(p);
        p = p->left;
      } else {
        p = s.top();
        s.pop();
        result.push_back(p);
        p = p->right;
      }
    }

    return result;
  }
}


















