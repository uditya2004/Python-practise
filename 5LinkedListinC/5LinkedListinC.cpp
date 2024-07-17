#include <iostream>
using namespace std;

class Node {
public: 
    int data;     //For storing data of the node.
    Node*next;   //creating a pointer , pointing to the location of the next element
};

int main() {
    Node* node1= new Node();
    cout << node1 ->data <<endl;

    return 0;
}