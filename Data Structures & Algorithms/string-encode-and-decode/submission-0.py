class Solution:

    def encode(self, strs: List[str]) -> str:
        big = ""
        for string in strs:
            big += string
            big += "RAZ"
        
        return big

    def decode(self, s: str) -> List[str]:
        return s.split("RAZ")[:-1]