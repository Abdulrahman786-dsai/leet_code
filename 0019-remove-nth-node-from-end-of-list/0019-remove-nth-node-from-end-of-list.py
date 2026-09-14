class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Fast ko n steps aage le jao
        for _ in range(n):
            fast = fast.next

        # Dono pointers ko move karo
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Nth node ko remove karo
        slow.next = slow.next.next

        return dummy.next