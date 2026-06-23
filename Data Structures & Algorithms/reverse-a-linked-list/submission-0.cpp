class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* nextNode = curr->next; // 1. Save the rest of the list
            curr->next = prev;               // 2. Reverse the pointer
            prev = curr;                     // 3. Move prev forward
            curr = nextNode;                 // 4. Move curr forward
        }

        return prev; // prev will be standing at the new head of the reversed list
    }
};