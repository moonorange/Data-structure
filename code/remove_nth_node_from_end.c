/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// My first c solution. Couldn't come with the solution without using "call by reference"

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* curr = head;
    int size = 0;
    int counter;

    while (curr)
    {
        curr = curr->next;
        size++;
    }
    if (size - n <= 0)
    {
        head = head->next;
        return (head);
    }
    struct ListNode *tmp = head;
    counter = size - n - 1;
    while (counter)
    {
        tmp = tmp->next;
        counter--;
    }
    tmp->next = tmp->next->next;
    return head;
}
