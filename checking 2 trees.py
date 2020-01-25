def check(p,q):

    if p:
        if q:
            
            if p.val!=q.val:
                return 0
            else:
                return  check(p.left,q.left) and check(p.right,q.right)
        else:
            return 0
    elif q:
        return 0
    else:
        return 1
    