
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(ch) for ch in s]
        n = len(digits)
        if n == 2:
            return digits[0] == digits[1]
        
        diff = 0
        
        B_val = 1
        B2 = 0
        B5 = 0
        
        current_binom = 1  # computed from B_val and B2,B5 below
        diff = (diff + current_binom * (digits[0] - digits[1])) % 10
        
        for i in range(0, n - 2):
            num = n - 2 - i
            den = i + 1
            
            while num % 2 == 0:
                B2 += 1
                num //= 2
            while num % 5 == 0:
                B5 += 1
                num //= 5
            B_val = (B_val * (num % 10)) % 10
            
            while den % 2 == 0:
                B2 -= 1
                den //= 2
            while den % 5 == 0:
                B5 -= 1
                den //= 5
            inv = {1: 1, 3: 7, 7: 3, 9: 9}[den % 10]
            B_val = (B_val * inv) % 10
            
            if B2 > 0 and B5 > 0:
                current_binom = 0  # because a factor 2 and a factor 5 give a factor 10
            else:
                factor = 1
                if B2 > 0:
                    factor = pow(2, B2, 10)
                if B5 > 0:
                    factor = 5
                current_binom = (B_val * factor) % 10
            
            diff = (diff + current_binom * (digits[i+1] - digits[i+2])) % 10
        
        return diff % 10 == 0

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    print(sol.hasSameDigits("3902"))   # Expected output: True
    print(sol.hasSameDigits("34789"))  # Expected output: False
