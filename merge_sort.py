class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddle(head):
    fast = head.next
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    middle = slow
    return middle


def merge(l1,l2):
    head = ListNode()
    tail = head
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next # Advance one when the condition is True 
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2 # So, how do we move forward one at time the last element is remaining and we need to concatenate it in the list
    return head.next
    
def mergeSort(head):
    if not head or not head.next:
        return head
    
    middle = findMiddle(head)
    after_middle = middle.next
    middle.next = None # Breaks the relation 
    left = mergeSort(head)
    right = mergeSort(after_middle)
    
    sorted_list = merge(left,right)
    
    return sorted_list

def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

def buildLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head




node_6 = ListNode(6)
node_5 = ListNode(1, next =node_6)
node_4 = ListNode(3, next= node_5)
node_3 = ListNode(9, next= node_4)
node_2 = ListNode(10, next= node_3)

my_sorted_list = mergeSort(node_2)

printLinkedList(my_sorted_list)