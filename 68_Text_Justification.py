from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []

        # line = ["This", "is", "an"], length = 8
        # easy to count the number of the words in the line:
        # len(line) = 3
        line, length = [], 0
        i = 0

        while i < len(words):

            if length + len(line) + len(words[i]) > maxWidth:
                # finish the line:
                extra_space = maxWidth - length
                space = extra_space // max(1, len(line) - 1)  # take care of just one word in a line
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0  # reset for the next line

            line.append(words[i])
            length += len(words[i])
            i += 1

            # deal with the last line
        last_line = " ".join(line)
        tail_space = maxWidth - len(last_line)
        last_line += " " * tail_space
        res.append(last_line)

        return res