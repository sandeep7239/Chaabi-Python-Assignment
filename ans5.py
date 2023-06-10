def find_common_and_not_common(mainstream_list, must_watch_list):
    mainstream_set = set(mainstream_list)
    must_watch_set = set(must_watch_list)

    common_elements = list(mainstream_set.intersection(must_watch_set))
    not_common_elements = sorted(list(mainstream_set.symmetric_difference(must_watch_set)))

    San = not_common_elements[:2]  
    not_common_elements = not_common_elements[2:]  

    not_common_elements.extend(San)

    gag= not_common_elements.pop(2)  
    not_common_elements.insert(-2, gag)

    se= not_common_elements.pop(5)
    not_common_elements.insert(-3, se)

    panda = not_common_elements.pop(1)
    not_common_elements.insert(0, panda)


    return common_elements, not_common_elements, San, gag


if __name__ == "__main__":
    mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z",
                  "One Piece"]
    must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!",
                  "One Piece", "Attack On Titan"]

    common_elements, not_common_elements, San, gag = find_common_and_not_common(mainstream, must_watch)

    print("Common elements:", common_elements)
    print("Not common elements (sorted):", not_common_elements)