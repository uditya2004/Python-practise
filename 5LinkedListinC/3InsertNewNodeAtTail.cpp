#include <iostream>
using namespace std;

class Node {
public: 
    int data;     //For storing data of the node.
    Node*next;   //creating a pointer , pointing to the location of the next element

    //constructor
    Node(int data) {
        this -> data = data;
        this -> next = NULL;
    }
};

void InsertAtTail(Node* &tail, int d) {

    Node* temp = new Node(d);
    tail -> next = temp;
    tail = temp;    
}

//Printing Linked List
void print(Node* &head) {
    Node* temp = head;

    while (temp != NULL) {
        cout<< temp -> data << " ";
        temp = temp -> next;
    }

    cout<<endl;
}

int main() {
    Node* node1= new Node(10);    //creating a node with data "10"

    //head pointed to node1
    Node* head = node1;
    Node* tail = node1;
    print(head);

    InsertAtTail(tail, 12);   //Adding "12" at the tail
    print(head);

    InsertAtTail(tail, 15);   //Adding "15" at the tail
    print(head);


    return 0;
}