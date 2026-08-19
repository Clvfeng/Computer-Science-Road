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

// 尾插法：在链表末尾添加节点
void add_tail(Node *&head, int value)
{
    // ① 创建新节点 p（new，data 赋值，next = nullptr）
    Node *p = new Node;
    p->data = value;
    p->next = nullptr;
    // ② 如果链表是空的：head = p; return;
    if(head == nullptr){
        head = p;
        return;
    }
    // ③ 否则：cur 从头走，走到最后一个节点，cur->next = p;
    else{
        Node *cur = head;
        while(cur->next != nullptr){
            cur = cur->next;
        }
        cur->next = p;
    }
}

// 在值为 target 的节点后面插入新节点
void insert_after(Node *head, int target, int value)
{
    // ① 创建新节点 p
    Node *p =  new Node;
    p->data = value;
    // ② cur 从头找 target
    Node *cur = head;
    // ③ 找到：p->next = cur->next; cur->next = p;
    while(cur != nullptr){
        if(cur->data == target){
            p->next = cur->next;
            cur->next = p;
            return ;
        }
        cur = cur->next;
    }
    // ④ 找不到：什么都不做（函数自然结束）
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
    while (cur != nullptr)
    {
        if (cur->data == value)
        {
            prev->next = cur->next;
            delete cur;
            return;
        }
        prev = cur;      // 往前走一步：prev 跟上
        cur = cur->next; // cur 往前
    }
    //   走完都没找到 → 什么都不做（函数自然结束）


}

int main()
{
    Node *head = nullptr;
    add_head(head, 3);
    add_head(head, 2);
    add_head(head, 1); // 1 2 3
    print_list(head);
    add_tail(head, 4); // 1 2 3 4
    print_list(head);
    insert_after(head, 2, 99); // 1 2 99 3 4
    print_list(head);
    delete_value(head, 2); // 1 99 3 4
    print_list(head);
    return 0;
}
