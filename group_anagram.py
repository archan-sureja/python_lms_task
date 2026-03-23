from collections import defaultdict
def group_anagrams(words : list[str])->list[list[str]]:
    """
        Groups anagrams together from the list of words
        params:
            words : list of strings
        return:
            list of list of strings : list of anagram groups
    """ 
    anagram_group = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        anagram_group[key].append(word)
    res = []
    for grp in anagram_group.values():
        res.append(grp)
    return res


def main():
    """ main function """
    input = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(input))

main()
