class SegmentTree:

    def __init__(self,total,L,R) -> None:
        self.sum=total
        self.left=None
        self.right=None
        self.L=L
        self.R=R

    @staticmethod
    def build(nums,L,R):
        # base case
        if L==R:
            # no more further division
            return SegmentTree(nums[L],L,R)

        mid=(L+R)//2

        root=SegmentTree(0,L,R)
        # Left -> [L,mid] Right -> [mid+1,R]
        root.left=SegmentTree.build(nums,L,mid)
        root.right=SegmentTree.build(nums,mid+1,R)

        root.sum=root.left.sum+root.right.sum


        return root

    def update(self,index,val):
        if self.L==self.R:
            self.sum=val
            return

        mid=(self.L+self.R)//2

        if index<=mid:
            self.left.update(index,val)
        else:
            self.right.update(index,val)

        self.sum=self.left.sum+self.right.sum

    def query(self,L,R):
        if self.L==L and self.R==R:
            return self.sum

        mid=(self.L+self.R)//2

        if R<=mid:
            return self.left.query(L,R)
        elif L>mid:
            return self.right.query(L,R)
        else:
            return self.left.query(L,mid)+self.right.query(mid+1,R)
