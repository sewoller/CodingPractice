def hIndex(citations) -> int:
    # citations.sort(reverse = True)
    # num = 0
    # for i in range(len(citations)):
    #     print(citations[i])
    #     num = num+1
    #     if num >= citations[i]:
    #         return(citations[i])
    # return 0

    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h = i+1
    return h

citations = [100]
print(hIndex(citations))