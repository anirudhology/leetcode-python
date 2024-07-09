from typing import List


class EncodeAndDecodeStrings:

    @staticmethod
    def encode(strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            current_encoded = str(len(s)) + "/" + s
            encoded += current_encoded
        return encoded

    @staticmethod
    def decode(s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '/':
                j += 1
            size = int(s[i:j])
            word = s[j + 1: j + 1 + size]
            i = j + 1 + size
            decoded.append(word)
        return decoded
