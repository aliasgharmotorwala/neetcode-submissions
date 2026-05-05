class TreeNode:

    def __init__(self):

        self.children = {}

        self.end_of_word = False

class PrefixTree:

    def __init__(self):

        self.root = TreeNode()
        

    def insert(self, word: str) -> None:

        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                new_child = TreeNode()
                current.children.update({char:new_child})
                current = new_child
        current.end_of_word = True


    def search(self, word: str) -> bool:

        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if current.end_of_word:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True  
        
        