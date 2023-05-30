#include<bits/stdc++.h>

using namespace std;

class SNode{
  public:
  int data;
  SNode *next;
  
  SNode(int info){
    this->data = info;
    this->next = nullptr;
  }
};

class SLList{
  public:
  SNode *head;
  SNode *tail;
  
  SLList(){
    this->head = nullptr;
    this->tail = nullptr;
  }
  
  void insert_node(int info){
    SNode* node = new SNode(info);
    if(!this=>head){
      this->head = node;
      else{
        this->tail->next= node;
      }
      this->tail = node;
};

void freeSLList(SNode* node){
  while(node){
    SNode* temp = node;
    node= node->next
    free(temp);
  }
}
