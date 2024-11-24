from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_length = len(words[0])
        result = []
        # with duplicate: use hashmap; without duplicate: use hashset
        word_count = {}

        for word in words:
            word_count[word] = word_count[word] + 1 if word in word_count else 1

        for i in range(word_length):

            left = i
            sub_count = {}
            count = 0

            for j in range(i, len(s) - word_length + 1, word_length):

                sub_word = s[j:j + word_length]

                if sub_word in word_count:

                    sub_count[sub_word] = sub_count[sub_word] + 1 if sub_word in sub_count else 1
                    count += 1

                    while sub_count[sub_word] > word_count[sub_word]:
                        sub_count[s[left:left + word_length]] -= 1
                        count -= 1
                        left += word_length

                    if count == len(words):
                        result.append(left)

                else:
                    left = j + word_length
                    sub_count = {}
                    count = 0

        return result