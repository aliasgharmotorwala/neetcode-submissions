class TreeNode:

    def __init__(self):

        self.children = {}

        self.endOfWord = False

class WordDictionary:

    def __init__(self):

        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:

        current = self.root

        for char in word:
            if char not in current.children:
                new_node = TreeNode()
                current.children.update({char:new_node})
            current = current.children[char]
        current.endOfWord = True

    def search(self, word: str) -> bool:

        current = self.root

        def search_word(current, word):

            dotFound = False

            for index, char in enumerate(word):
                if char != ".":
                    if char in current.children:
                        current = current.children[char]
                    else:
                        return False
                else:
                    dotFound = True
                    break
        
            if dotFound:
                return find_dots(current, word[index+1:])
            else:
                return current.endOfWord
        
        def find_dots(start, remaining_word):

            if len(remaining_word) == 0:
                if len(start.children.keys()) > 0:
                    for child in start.children:
                        if start.children[child].endOfWord == True:
                            return True
                    return False
                else:
                    return False

            current = start
            next_char = remaining_word[0]
            child_list = list(current.children.keys())
            child_index = 0

            while child_index < len(child_list):

                if next_char == ".":
                    word_found = find_dots(current.children[child_list[child_index]], remaining_word[1:])
                    if word_found:
                        return True

                elif next_char in current.children[child_list[child_index]].children:

                    selected_child = current.children[child_list[child_index]].children[next_char]

                    # If reached the end of word
                    if len(remaining_word) == 1:
                        return selected_child.endOfWord
                    
                    # Else continue matching from next char
                    word_found = search_word(selected_child, remaining_word[1:])

                    if word_found:
                        return True

                child_index += 1

            return False
                

        return search_word(current, word)
                    




        
