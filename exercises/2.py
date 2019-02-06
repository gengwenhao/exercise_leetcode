# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
# 并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return

        cur1, cur2, flag = l1, l2, False

        head_val = l1.val + l2.val

        if 9 < head_val:
            flag = True
            head_val -= 10

        cur3 = head = ListNode(head_val)

        while cur1.next is not None and cur2.next is not None:
            cur1, cur2 = cur1.next, cur2.next
            cur3_val = 1 if flag else 0
            cur3_val += cur1.val + cur2.val

            flag = False

            if 9 < cur3_val:
                flag = True
                cur3_val = cur3_val - 10

            cur3.next = ListNode(cur3_val)
            cur3 = cur3.next

        while cur1.next:
            cur1 = cur1.next
            cur3.next = cur1

            if flag:
                cur3.next.val += 1
                flag = False
            if 9 < cur3.next.val:
                cur3.next.val -= 10
                flag = True

            cur3 = cur3.next

        while cur2.next:
            cur2 = cur2.next
            cur3.next = cur2

            if flag:
                cur3.next.val += 1
                flag = False
            if 9 < cur3.next.val:
                cur3.next.val -= 10
                flag = True

            cur3 = cur3.next

        if flag:
            cur3.next = ListNode(1)

        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)

    l3 = Solution().addTwoNumbers(l1, l2)
    pass
