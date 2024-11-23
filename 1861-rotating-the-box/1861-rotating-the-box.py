class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box or not box[0]:
            return []
        m,n=len(box),len(box[0])
        r=[["" for _ in range(m)]for _ in range(n)]
        for i in range(m):
            for j in range(n):
                r[j][m-1-i]=box[i][j]
        for c in range(m):
            b=n-1
            for row in range(n-1,-1,-1):
                if r[row][c]=='#':
                    if row!=b:
                        r[b][c]='#'
                        r[row][c]='.'
                    b-=1
                elif r[row][c]=='*':
                    b=row-1
        return r
        