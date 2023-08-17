import re


def solution(word, pages):
    word = word.lower()
    score = {}
    link = {}

    tmp = []

    for i in range(len(pages)):
        k = pages[i].lower()

        base_score = 0
        for f in re.findall(r'[a-zA-Z]+'.format(word), k):
            if f == word:
                base_score += 1
        page_name = re.search(r'<meta[^>]*content="https://([\S]*)"/>', k).group(1)

        other_link = re.findall(r'<a href="https://([\S]*)"', k)
        other_link_score = len(other_link)

        score[page_name] = []
        score[page_name].append(base_score)
        score[page_name].append(other_link_score)

        if page_name not in link:
            link[page_name] = []

        for l in other_link:
            link[page_name].append(l)

    for l in link:
        for j in link[l]:
            if j in score:
                score[j].append(score[l][0] / score[l][1])

    for case in score:
        tmp.append(sum(score[case])-score[case][1])

    return tmp.index(max(tmp))