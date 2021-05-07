class Int_prime():
    def __init__(self, number):
        self._representation = {}

        factor = 2
        while (number != 1):
            if (number % factor == 0):
                self._representation[factor] += 1
                number /= factor
            else:
                factor += 1

    def add_factor(self, n):
        self._representation[n] += 1

    def gcf(self, other):
        gcf = Int_prime(1)

        for i in self._representation:
            if i in other._representation:
                common = min(self._representation, other._representation)
                gcf.add_factor(common)
        
        return gcf
    
    def lcm(self, other):
        lcm = Int_prime(1)
        gcf._representation = self._representation + other._representation
        return gcf
    
    def remove_factor(self, n):
        if n in self._representation:
            if self._representation[n] > 0:
                self._representation[n] -= 1
                return
        return False
    

