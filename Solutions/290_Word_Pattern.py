class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # s_words_list = []
        # word = ""
        # for i, c in enumerate(s):
        #     if i == len(s) - 1:
        #         word += c
        #         s_words_list.append(word)
        #     if c != " ":
        #         word += c
        #     if c == " ":
        #         s_words_list.append(word)
        #         word = ""
        #         continue

        s_words_list = s.split(" ")

        if len(pattern) != len(s_words_list):
            return False

        p_map, s_map = {}, {}

        for c_p, word_s in zip(pattern, s_words_list):

            if (c_p in p_map and p_map[c_p] != word_s) or (word_s in s_map and s_map[word_s] != c_p):
                return False

            p_map[c_p] = word_s
            s_map[word_s] = c_p

        return True