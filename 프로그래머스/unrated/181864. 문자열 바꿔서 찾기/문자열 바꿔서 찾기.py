def solution(myString, pat):
    pat = pat.replace("A", "b")
    pat = pat.replace("B", "A")
    pat = pat.replace("b", "B")
    
    if pat in myString:
        return 1
    else:
        return 0