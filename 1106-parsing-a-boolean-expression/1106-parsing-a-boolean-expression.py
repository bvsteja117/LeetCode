import collections


class Solution:
    def parseBoolExpr(self, e):
        self.e = e
        self.i = 0
        return self.p()

    def p(self):
        c = self.e[self.i]
        if c == 't':
            self.i += 1
            return True
        elif c == 'f':
            self.i += 1
            return False
        elif c == '!':
            return self.p_not()
        elif c == '&':
            return self.p_and()
        else:
            return self.p_or()

    def p_not(self):
        self.i += 2
        r = self.p()
        self.i += 1
        return not r

    def p_and(self):
        self.i += 2
        r = self.p()
        while self.e[self.i] != ')':
            self.i += 1
            r &= self.p()
        self.i += 1
        return r

    def p_or(self):
        self.i += 2
        r = self.p()
        while self.e[self.i] != ')':
            self.i += 1
            r |= self.p()
        self.i += 1
        return r

    def parseBoolExpr2(self, e, t=True, f=False):
        return eval(e.replace('!', 'not |').replace(
            '&(', 'all ([').replace('|(', 'any ([').replace(')', '])'))
