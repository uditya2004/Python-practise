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

//Insert element at the Head
void InsertAtHead(Node* &head, int d) {

    Node* temp = new Node(d);     //new node "temp" created
    temp ->next = head;           // placing the next element address as the Head, in temp node.
    head = temp;                  // making this temp node as NEW HEAD
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
    print(head);

    InsertAtHead(head, 12);   //Adding "12" at the head
    print(head);

    InsertAtHead(head, 15);   //Adding "15" at the head
    print(head);

    return 0;
}