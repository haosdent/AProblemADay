class Solution {
public:
  vector<int> preorderTraversal(TreeNode *root) {
    vector<int> result;
    const TreeNode *p;
    stack<const TreeNode *> s;

    p = root;
    if (root != nullptr) s.push(p);

    while (!s.empty()) {
      p = s.top();
      s.pop();
      result.push_back(p);
      if (p->right != nullptr) s.push(p->right);
      if (p->left != nullptr) s.push(p->left);
    }

    return result;
  }
}


















