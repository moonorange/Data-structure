/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// My first c solution. Couldn't come with the solution without using "call by reference"

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
	struct ListNode* tmp = head;
	int size = 0;
    int counter;

	while (tmp)
	{
		tmp = tmp->next;
		size++;
    }
    if (size - n <= 0)
    {
        head = head->next;
        return (head);
    }
    struct ListNode *curr = head;
    counter = size - n - 1;
    while (counter)
    {
		curr = curr->next;
		counter--;
    }
	curr->next = curr->next->next;
	return head;
}
