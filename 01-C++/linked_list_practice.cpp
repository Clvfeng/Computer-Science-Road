#include <iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
};
int main(){
    Node a, b, c;
    a.data = 10;
    b.data = 20;
    c.data = 30;
    Node *head = &a;
    Node *cur = head;
    a.next = &b;
    b.next = &c;
    c.next = nullptr;
    // 从第一个节点开始
    while (cur != nullptr){                            // 没到终点就继续
        cout << cur->data << " "; // 输出当前节点的数据
        cur = cur->next;          // 移到下一个节点
    }
}
