class WordBreak:

    def get_combinations(self, str, dictionary, combination=(),
                         parent_indices=frozenset(), index=0):
        if index > len(str): return []
        if index == len(str): return [combination]
        word_set = set()
        combinations = []
        for (i, word) in enumerate(dictionary):
            if (word not in word_set
                    and i not in parent_indices
                    and str.startswith(word, index)):
                word_set.add(word)
                combinations += self.get_combinations(str, dictionary,
                                                      combination + (word,),
                                                      frozenset(parent_indices | {i}),
                                                      index + len(word))
        return combinations
