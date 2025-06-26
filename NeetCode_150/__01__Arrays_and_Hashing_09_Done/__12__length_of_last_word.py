class Solution:
    def length_of_last_word(self,s : str):
        words = s.split()
        return len(words[len(words) -1])


    def driver_len_of_last_word(self):
        s = "Hello World"
        assert 5 == self.length_of_last_word(s)

        s = "   fly me   to   the moon  "
        assert 4 == self.length_of_last_word(s)

        s = "luffy is still joyboy"
        assert 6 == self.length_of_last_word(s)
