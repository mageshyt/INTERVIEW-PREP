# Fast and slow Pointer (Floyd's Cycle Detection Algorithm)

# 1. Find the middle of the linked list
def find_middle(self,head):
    fast=slow=head
    # move the fast pointer twice as fast as the slow pointer
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
# 2. Determine cycle in the linked list
def has_cycle(self,head):
    fast=slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True 
    return False

# 3. Find the Cycle in the linked list and return the head of the Cycle
def find_cycle(self,head):
    fast=slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    # if there is no cycle
    if not fast or not fast.next:
        return None
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow

# 4.Maximum Twin Sum of a Linked List

def max_twin_sum(self,head):
    slow=fast=head
    prev=None

    # find the middle of the linked list and reverse the first half of the linked list
    while fast and fast.next:
        temp =slow.next
        slow.next=prev
        prev=slow
        fast=fast.next.next
        slow=temp

    res=0

    while slow:
        res= max(res,slow.val+prev.val)
        slow=slow.next
        prev=prev.next

    return res



