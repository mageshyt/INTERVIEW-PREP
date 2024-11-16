
from typing import List
def knapstack(
    bag_weight:int,
    item_weight:List[int],
    item_value:List[int]
):

    dp={} # key: (index,remaining_weight) value: max_value

    def dfs(idx,remaining_weight):

        if idx== 0:
            if item_weight[idx] <= remaining_weight:
                return item_value[idx]
            return 0
        if(idx,remaining_weight) in dp:
            return dp[(idx,remaining_weight)]

        take=0
        if item_weight[idx] <= remaining_weight:
            take = item_value[idx] + dfs(idx-1,remaining_weight-item_weight[idx])

        notake = dfs(idx-1,remaining_weight)

        dp[(idx,remaining_weight)] = max(take,notake)


        return max(take,notake)

    return dfs(len(item_weight)-1,bag_weight)

# BOTTOM UP
# Time: O(n*W) | Space: O(n*W)
def knapstack2(bag_weight,item_weight,item_value):
    dp=[[0]*(bag_weight+1) for _ in range(len(item_weight))]
    # BASE CASE
    for i in range(bag_weight+1):
        if item_weight[0] <= i:
            dp[0][i] = item_value[0]




    for i in range(1,len(item_weight)):
        for j in range(bag_weight+1):
            take=0
            if item_weight[i] <= j:
                take = item_value[i] + dp[i-1][j-item_weight[i]]

            notake = dp[i-1][j]

            dp[i][j] = max(take,notake)

    return dp[len(item_weight)-1][bag_weight]

def knapstack3(bag_weight,item_weight,item_value):
    dp=[0]*(bag_weight+1)
    for i in range(bag_weight+1):
        if item_weight[0] <= i:
            dp[i] = item_value[0]

    for i in range(1,len(item_weight)):
        for j in range(bag_weight,item_weight[i]-1,-1):
            take = item_value[i] + dp[j-item_weight[i]]
            notake = dp[j]
            dp[j] = max(take,notake)

    return dp[bag_weight]


# bag_weight=5
# item_weight=[1,2,4,5]
# item_value=[5,4,8,6]
#
testcase=int(input())

for _ in range(testcase):
    n=int(input())
    item_weight=list(map(int,input().split()))
    item_value=list(map(int,input().split()))
    bag_weight=int(input())
    print("----")
    print(knapstack(bag_weight,item_weight,item_value))
    print(knapstack2(bag_weight,item_weight,item_value))
    print(knapstack3(bag_weight,item_weight,item_value))
    print("----")
