class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans_string = ''
        for string in strs:
             ans_string = ans_string + "".join([chr(ord(x)+1) for x in string]) + '\n'
        return ans_string

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans_list = []
        for string in s.split('\n'):
            ans_list.append("".join([chr(ord(x)-1) for x in string]))
        return ans_list[:-1]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
