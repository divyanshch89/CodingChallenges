from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #we can a delimiter like length of the string +'#'. The '#'
        # will let us know the end of length integer and the begining of the actual data
        res =''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res,i = [],0
        
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            #we found the delimiter
            len_current_chunk = int(s[i:j])
            res.append(s[j+1:j+1+len_current_chunk])
            #move current index i to the beginning of next chunks length
            i = j+1+len_current_chunk
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))




# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = [""]
s = codec.encode(strs)
print(s)
print(codec.decode(s))