class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        smap = {}
        tmap = {}

        if len(s) != len(t):
            return False

        else:
            for word in s:
                if word in smap:
                    smap[word] += 1
                else:
                    smap[word] = 1

            for word in t:
                if word in tmap:
                    tmap[word] += 1
                else:
                    tmap[word] = 1


        return smap == tmap                              
               