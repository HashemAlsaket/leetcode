# Link to video: https://youtu.be/N-GJaW20GdQ

class Solution:
    def removeVowels(self, s: str) -> str:
        letter_list = []
        
        vowel_dict = {vowel: True for vowel in 'aeiou'}
        
        for letter in s:
            if not vowel_dict.get(letter, False):
                letter_list.append(letter)
        
        return ''.join(letter_list)