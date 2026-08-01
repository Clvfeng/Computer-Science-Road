#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

// 头插法：在链表头部插入新节点
void add_head(Node *&head, int value)
{
    // TODO: ① 创建新节点并赋值 ② 新节点->next = head ③ head = 新节点
    Node *_new = new Node;
    _new->data = value;
    _new->next = head;
    head = _new; ;
}

// 遍历打印（昨天学过，复习一下）
void print_list(Node *head)
{
    // TODO
    Node* flag = head;
    while(flag != nullptr){
        cout<<flag->data<<endl;
        flag = flag->next;
    }
}

// 删除第一个值为 value 的节点
void delete_value(Node *&head, int value)
{
    // 情况1：头节点就是要删的
    //   head = head->next;  delete 旧头;  return;
    if(head->data == value){
        Node *p = head;
        head = head->next;
        delete p;
        return;
    }
    // 情况2：普通情况
    Node* prev = head;
    Node* cur = head->next;
      while (cur != nullptr) {
          if (cur->data == value) {
              prev->next = cur->next;
              delete cur;
              return;
          }
          prev = cur;         // 往前走一步：prev 跟上
          cur = cur->next;    // cur 往前
      }
    //   走完都没找到 → 什么都不做（函数自然结束）


}

int main()
{
    Node *head = nullptr; // 空链表
    add_head(head, 3);
    add_head(head, 2);
    add_head(head, 1);
    print_list(head); // 期望输出: 1 2 3
    delete_value(head, 2);
    print_list(head); // 期望输出: 1 3
    return 0;
}
