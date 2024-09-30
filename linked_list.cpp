#include <iostream>
#include <string>

using namespace std;

struct Node {
    string name;
    long prn;
    Node* next;
    Node() : prn(0), next(nullptr) {}
};

class List {
private:
    Node* head;
    Node* tail;
    int count;

public:
    List() : head(nullptr), tail(nullptr), count(0) {}
    void addingMember(){
		int n;
		cout<<"Enter the number of members to add :"<<endl;
		cin>>n;
        for(int i = 0;i<n;i++){
		    Node* newNode = new Node;
            cout << "Enter  new Member name: ";
            cin >> newNode->name;
            cout << "Enter PRN of Member: ";
            cin >> newNode->prn;

            if(!head || newNode->prn < head->prn){
                newNode->next = head;
                head = newNode;
                if (!tail){
                    tail = newNode; 
                }
            } 
            else if (!tail || newNode->prn > tail->prn) {
                tail->next = newNode;
                tail = newNode;
            } 
            else {
                Node* current = head;
                while (current->next && current->next->prn < newNode->prn) {
                    current = current->next;
                }
                newNode->next = current->next;
                current->next = newNode;
                if (!newNode->next) tail = newNode; 
            }
            count++;
        }
    }

    void remove() {
        if (!head) {
            cout<< "Error, Underflow!" << endl;
            return;
        }
        long prn;
        cout << "Enter PRN of member to remove: ";
        cin >> prn;

        if(head->prn == prn) {
            Node* temp = head;
            head = head->next;
            if (!head) tail = nullptr; 
            delete temp;
        } 
        else{
            Node* current = head;
            while (current->next && current->next->prn != prn) {
                current = current->next;
            }
            if(current->next) {
                Node* temp = current->next;
                current->next = current->next->next;
                if (!current->next) tail = current; 
                delete temp;
            } 
            else{
                cout << "Member not found!" << endl;
                return;
            }
        }
        count--;
    }

    void display() {
        Node* current = head;
        while (current) {
            cout << "Name: " << current->name << endl;
            cout << "PRN: " << current->prn << endl;
            current = current->next;
        }
    }

    void displayReverse() {
        Node* current = head;
        if (!current) {
            cout << "List is empty!" << endl;
            return;
        }

        while (current->next) {
            current = current->next;
        }

        while (current){
            cout << "Name: " << current->name << endl;
            cout << "PRN: " << current->prn << endl;
            current = prev(current, head); 
        }
    }

    Node* prev(Node* node, Node* head) {
        if (node == head) return nullptr; 

        Node* current = head;
        while (current->next && current->next != node) {
            current = current->next;
        }
        return current;
    }

    ~List() {
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main(){
    List list;
    int choice;
    do{
        cout<<"----------Menu-----------"<<endl;
        cout<<"1. Add members to the list: "<<endl;
        cout<<"2. Display all the members of the list: "<<endl;
        cout<<"3. Remove a member : "<<endl;
        cout<<"4. Display all the members in reverse order :"<<endl;
        cout<<"5. Exit"<<endl;
        cout<<"Enter your choice : "<<endl;
        cin>>choice;
        
        if(choice==1){
            list.addingMember();
        }
        else if(choice==2){
            list.display();
        }
        else if(choice==3){
            list.remove();
        }
        else if(choice==4){
            list.displayReverse();
        }
        else if(choice==5){
            break;
        }
    }
    while(choice!=5);
    return 0;
}