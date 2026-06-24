class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        copies = {}

        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        return copies[head]
