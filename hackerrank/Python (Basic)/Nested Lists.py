if __name__ == '__main__':
    n = int(input())
    records = []
    scores = []
    out = []
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
        
    # Removing duplicates from the list
    new_scores = list(set(scores))
    # Sorting the list
    new_scores.sort()
    # crete a new list : studens having lowest grade
    for i in range(n):
        if new_scores[1]==records[i][1]:
            out.append(records[i]) 
    # order names alphabetically in the new_scores 
    new_out = sorted(out)
    for i in range(len(new_out)):
        print(new_out[i][0])