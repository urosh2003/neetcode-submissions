class Solution:

    def encode(self, strs: List[str]) -> str:
        big = ""
        for string in strs:
            size = len(string)
            big += str(size)
            big += '#'
            big += string
        
        print(big)
        return big

    def decode(self, s: str) -> List[str]:
        out = []
        readNumber = True
        numberString = ""
        i = 0
        while i < len(s):
            if readNumber:
                while s[i] != "#":
                    numberString += s[i]
                    i += 1
                i += 1
                readNumber = False
                number = int(numberString)
                numberString = ""
                if number == 0:
                    out.append("")
                    readNumber = True
            else:
                string = ""
                while number > 0:
                    string += s[i]
                    i += 1
                    number -= 1
                out.append(string)
                readNumber = True

        return out