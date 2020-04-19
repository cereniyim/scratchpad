def KUniqueCharacters(string):

    unique_counter = int(string[0])

    all_k_substrings = []

    for i in range(1, len(string)):

        counter = 0

        substring = ""

        for j in range(i, len(string)):

            if string[j] not in substring:
                counter += 1

            if counter > unique_counter:
                break

            substring += string[j]

        all_k_substrings.append(substring)

    longest_substr = ""

    for s in all_k_substrings:
        if len(s) > len(longest_substr):
            longest_substr = s

    return longest_substr

print(KUniqueCharacters("2aabbacbaa"))