#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 创建空 vector
    vector<int> nums;
    
    // 添加元素
    nums.push_back(10);
    nums.push_back(20);
    nums.push_back(30);
    
    // 访问元素
    cout << nums[0] << endl;       // 10
    cout << nums.size() << endl;   // 3
    
    // 遍历
    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;
    
    nums.insert(nums.begin() + 1, 99);
    
    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;
    
    nums.pop_back();
    
    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;
    
    nums.erase(nums.begin());
    
    for (int n : nums) {
        cout << n << " ";
    }
    cout << endl;
    return 0;
}