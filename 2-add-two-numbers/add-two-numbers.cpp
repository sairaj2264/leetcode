/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* answer = new ListNode(0);
        ListNode* head = answer;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry!=0) {
            int p1;
            int p2;
            if (l1 == nullptr) {
                p1 = 0;
            } else {
                p1 = l1->val;
            }
            if (l2 == nullptr) {
                p2 = 0;
            } else {
             p2 = l2->val;
            }
            int sum = p1 + p2 + carry;
            int temp = sum % 10;
            carry = sum / 10;
            answer->next = new ListNode(temp);
            answer = answer->next;
            if(l1!= nullptr){
            l1 = l1->next;
            }
            if(l2!= nullptr){
            l2 = l2->next;
            }
        }

        return head->next;
    }
};