#include <iostream>
using namespace std;

// 定义一个结构体 Node，有两个成员：
// int data 和 Node* next
struct Node
{
    int data;
    Node *next;
};

int main()
{
    // 创建两个节点
    Node a;
    a.data = 10;

    Node b;
    b.data = 20;

    // 连接：a.next 指向 b
    a.next = &b;
    b.next = nullptr; // 链表结尾

    // 通过 a 访问 b 的数据
    cout << a.data << endl;       // 10
    cout << a.next->data << endl; // 20（-> 是箭头，通过指针访问成员）

    return 0;
}
