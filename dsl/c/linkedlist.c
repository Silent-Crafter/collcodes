#include <stdio.h>
#include <stdlib.h>

typedef
struct Node {
    int data;
    struct Node* next;
} Node;

typedef
struct List {
    unsigned int size;
    struct Node* head;
} List;


void
init(List* l) {
    l->size = 0;
    l->head = NULL;
}


void
push(List* l, int data) {
    if (l->head == NULL) {
        l->head = (Node*) malloc(sizeof(Node));
        l->head->next = NULL;
        l->head->data = data;
        l->size++;
        return;
    }

    Node* new_node = (Node*) malloc(sizeof(Node));
    Node* head = l->head;

    new_node->data = data;
    new_node->next = head;

    l->head = new_node;
    l->size++;
}


void
iterate(List* l) {
    if (l->head == NULL) {
        printf("[ ]");
        return;
    }
    Node* curr = l->head;
    printf("[ ");
    for ( ; curr;  curr=curr->next) {
        printf("%d ", curr->data);
    }
    printf("]\n");
}

void
append(List* l, int data) {
    if (l->head == NULL) {
        l->head = (Node*) malloc(sizeof(Node));
        l->head->data = data;
        l->head->next = NULL;
        return;
    }
    Node* curr = l->head;
    // Go to end
    while (curr->next)
        curr = curr->next;

    // Add at the end
    Node* new_node = (Node*) malloc(sizeof(Node));

    new_node->next = NULL;
    new_node->data = data;

    curr->next = new_node;
    l->size++;
}

void
insert(List* l, int position, int data) {
    Node* curr = l->head;
    Node* prev = l->head;

    for (int i = 0 ; i < position ; i++) {
        if ( i != position-1 ) {
            prev = curr;
            if ( prev == NULL ) {
                perror("Position Out of range");
                break;
            }
            curr = curr->next;
            continue;
        }

        Node* new_node = (Node*) malloc(sizeof(Node));
        new_node->data = data;
        new_node->next = curr;
        if ( position != 1 )
            prev->next = new_node;
        l->size++;
    }
}

void
delete(List* l, int position) {
    Node* curr = l->head;
    Node* prev = l->head;
    if (curr == NULL) {
        perror("Empty list. Nothing to delete.");
        return;
    }
    for (int i = 0; i < position ; i++ ) {
        if ( i != position - 1 ) {
            prev = curr;
            if (prev == NULL) {
                perror("Index out of range");
                break;
            }
            curr = curr->next;
            continue;
        }

        prev->next = curr->next;
        if ( position == 1 &&  i == 0 )
            l->head = curr->next;

        free(curr);
        l->size--;
        break;
    }
}

int
main() {
    List l;
    init(&l);

    push(&l, 20);
    push(&l, 30);
    push(&l, 40);
    push(&l, 50);

    append(&l, 10);

    insert(&l, 2, 21);

    iterate(&l);

    delete(&l, 2);
    delete(&l, 1);
    delete(&l, (int)l.size);

    iterate(&l);

    delete(&l, 10);

    return 0;
}
