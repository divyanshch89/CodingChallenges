#Link: https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        mast_dic = [
            ("I",1),
            ("IV",4),
            ("V",5),
            ("IX",9),
            ("X",10),
            ("XL",40),
            ("L",50),
            ("XC",90),
            ("C", 100),
            ("CD",400),
            ("D", 500),
            ("CM",900),
            ("M", 1000)
             ]
        '''
        loop from the biggest to the smallest
        find the largest number which can fit the number
        find how many current symbol can fit the number(div mod)
        subtract the symbol value* time symbol can be fitted from the original number and
        continue going down
        '''
        converted = []
        for i in range(len(mast_dic)-1,-1,-1):
            if num==0:
                break
            sym = mast_dic[i][0]
            val = mast_dic[i][1]
            if val > num:
                continue
            count = num//val
            converted.append(sym*count)
            num-=val*count
            
                
        return "".join(converted)
        