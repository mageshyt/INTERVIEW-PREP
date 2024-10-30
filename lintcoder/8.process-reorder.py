"""
John has a list of N system requests to be processed based on
their priority. Each request has three fields: Priority Number (PN),
Process Number (PR), and Process Request ID (ID). The system
processes requests in this order:
1. More set bits (1s) in the Priority Number.
2. If equal, the larger Priority Number.
3. If still equal, more set bits in the Process Number.
4. If still equal, the larger Proclass Number.
5. If all the above are equal, the request appearing first
in the list is processed, and others with the same
values are rejected.
Your task is to return the "Reorder" which is the list of Process
Request IDs in the order they are processed by the system.

Testcase Input
3
111
112
1 3 3
Testcase Output
3 1
"""


from typing import List, Tuple
import heapq

def count_set_bits(x: int) -> int:
    return bin(x).count('1')

def reorder_requests(n: int, requests: List[Tuple[int, int, int]]) -> List[int]:
    heap=[] # ( bit_count, priority_number, process_number, id)

    for i in range(n):
        pn,pr,id = requests[i]
        bit_count = count_set_bits(pn)
        bit_pr = count_set_bits(pr)
        heapq.heappush(heap,(-bit_count,-bit_pr,-pn,-pr,id)) # (bit_count, priority_number, process_number, id)

    result = []

    seen = set()

    while heap:
        _,_,pn,pr,id = map(abs,heapq.heappop(heap))

        if (pn,pr) in seen:
            continue

        seen.add((pn,pr))
        result.append(id)

    return result



# test the solution
requests = [
    (1,1,1),
    (1,1,2),
    (1,3,3),
]
print(reorder_requests(3,requests)) # [1, 2, 3]
