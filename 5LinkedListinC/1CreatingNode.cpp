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


int main() {
    Node* node1= new Node(10);    //creating a node with data "10"

    cout << node1 ->data <<endl;   
    cout<< node1 ->next <<endl;



    return 0;
}