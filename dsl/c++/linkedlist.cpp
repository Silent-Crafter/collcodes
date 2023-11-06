#include <iostream>
using namespace std;

class Node {
private:
    int data;
    Node* next;

public:
    Node() {
        this->next = nullptr;
    }

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }

    Node(int data, Node* next) {
        this->data = data;
        this->next = next;
    }

    friend Node* next(Node*);
    friend ostream& operator << (ostream&, Node&);
    friend class List;
};

Node* next(Node* n) { return n->next; }

ostream& operator << (ostream& os, Node& n) {
    os << n.data;
    return os;
}

class List {
private:
    unsigned int size;
    Node* head;

public:
    List() {
        this->size = 0;
        this->head = nullptr;
    }

    List(int data) {
        this->size = 1;
        this->head = new Node(data, nullptr);
    }

    unsigned int getSize() { return this->size; }
    int getData(Node* n) { return n->data; }

    void display();
    void push(int);
    void append(int);

    List& operator >> (int);

    friend ostream& operator << (ostream&, List&);
};

ostream& operator << (ostream& os, List& l) {
    Node* curr = l.head;
    cout << "[ ";
    while (curr != nullptr ) {
        os << *curr << " ";
        curr = next(curr);
    }
    cout << "]";

    return os;
}

void
List::display() {
    Node* curr = this->head;
    cout << "[ ";
    while ( curr != nullptr ) {
        cout << curr->data << " ";
        curr = curr->next;
        cout.flush();
        cout.clear();
    }
    cout << "]" << endl;
}

void
List::push(int data) {
    if ( this->head == nullptr ) {
        this->head = new Node(data, nullptr);
        this->size++;
        return;
    }

    Node* nn = new Node(data, this->head);
    this->head = nn;
    this->size++;
}

void
List::append(int data) {
    // Go to end
    Node* end = this->head;
    if ( end == nullptr ) {
        this->head = new Node(data, nullptr);
        return;
    }
    while ( end->next != nullptr )
        end = end->next;

    Node* nn = new Node(data, nullptr);
    end->next = nn;
    this->size++;
}

List&
List::operator >> (int data) {
    append(data);
    return *this;
}

int
main() {
    List l;

//    l.push(10);
//    l.push(20);
//    l.push(30);
//    l.push(40);
//
//    l.display();

    l >> 2 >> 3 >> 4;
    cout << l << endl;

    return 0;
}
