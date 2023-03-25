# Description: This file contains the functions for the database
# > This class is a wrapper for the database
class Database():

    def __init__(self, path: str):
        """
        This function takes a path to a text file, creates a database of words and resorts the words
        
        :param path: The path to the database file
        :type path: str
        """
        self.path = path
        self.open_db()
        self.sort_words()

    def open_db(self)-> list:
        """
        It opens a file, reads it, splits it into a list of lists, and assigns it to the content
        attribute of the class
        """
        with open(self.path, "r") as file:
            text = file.read()
            text = text.split("\n")
            text = [i.split(",") for i in text]
            self.content = text

    def add_word(self, word: str, meaning: str, pronunciation: str, definition: str):
        """
        It opens the file, writes the word, meaning, pronunciation, and definition to the file, and then
        sorts the words
        
        :param word: The word you want to add
        :type word: str
        :param meaning: The meaning of the word
        :type meaning: str
        :param pronunciation: the way the word is pronounced
        :type pronunciation: str
        :param definition: The definition of the word
        :type definition: str
        """
        with open(self.path, "a") as file:
            file.write(f"{meaning},{word},{pronunciation},{definition}")
        self.sort_words()
    
    def sort_words(self):
        """
        It sorts the words in the database alphabetically
        """
        self.rewrite_db(self.content.sort())
        
    
    def rewrite_db(self, new_content: list):
        """
        It takes a list of lists, and writes each list to a new line in a file
        
        :param new_content: The list of lists you want to write to the file
        :type new_content: list
        """
        with open(self.path, "w") as file:
            for i in new_content:
                file.write(f"{i[0]},{i[1]},{i[2]},{i[3]}")
    
    def merge_awk_db(self, other_db: str):
        """
        It takes a text file made of awkword export and adds each line to the database
        
        :param other_db: The path to the other database file
        :type other_db: str
        """
        with open(other_db, "r") as file:
            text = file.read()
            text = text.split("\n")
        for word in text:
            self.add_word(word, "", "", "")
        self.sort_words()
    
    def merge_db(self, other_db: str):
        """
        It takes a file name as an argument, reads the file, splits the file into a list of lists, and
        then adds each word to the database
        
        :param other_db: str = the path to the other database
        :type other_db: str
        """
        with open(other_db, "r") as file:
            text = file.read()
            text = text.split("\n")
            text = [i.split(",") for i in text]
        for word in text:
            self.add_word(word[1], word[0], word[2], word[3])
        self.sort_words()