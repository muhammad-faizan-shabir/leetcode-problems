class Solution:
    def compress(self, chars: list[str]) -> int:
        
        compressedString = ""
        currentCh = chars[0]
        currentCount = 1
        
        chars.pop(0)

        for ch in chars:
            if(ch == currentCh):
                currentCount += 1
            else:
                compressedString += currentCh
                if(currentCount > 1):
                    compressedString += str(currentCount)
                
                currentCh = ch
                currentCount = 1
            
        compressedString += currentCh
        if(currentCount > 1):
            compressedString += str(currentCount)

        i = 0
        for ch in compressedString:
            chars.insert(i, ch)
            i += 1
        
        return len(compressedString)