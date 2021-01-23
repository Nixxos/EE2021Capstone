from collections import namedtuple

Decode = namedtuple("Decode", "lvl1 lvl2 getball hitg1 hitg2 ret")


class DecodeOpcode:
 
    def switch(self, opcode):
        default = "Incorrect code"
        return getattr(self, 'case_' + str(opcode), lambda: default)()
 
    def case_0(self):
        m = Decode(0,0,0,0,0,0)
        return m
 
    def case_1(self):
        m = Decode(0,1,2,2,3,3)
        return m
 
    def case_2(self):
        m = Decode(0,0,0,1,5,8)
        return m
 
    def case_3(self):
        m = Decode(0,0,0,0,0,0)
        return m
 
    def case_4(self):
        m = Decode(1,3,0,0,0,0)
        return m
 
    def case_5(self):
        m = Decode(0,0,0,0,0,0)
        return m
 
    def case_6(self):
        m = Decode(0,1,2,0,0,0)
        return m
        
    def case_7(self):
        m = Decode(1,2,2,0,0,0)
        return m

    def case_8(self):
        m = Decode(1,2,2,0,0,0)
        return m

    def case_9(self):
        m = Decode(1,3,0,0,0,0)
        return m

    def case_10(self):
        m = Decode(1,2,2,0,0,0)
        return m

    def case_11(self):
        m = Decode(1,2,2,0,0,0)
        return m

    def case_12(self):
        m = Decode(0,0,0,0,0,0)
        return m

    def case_13(self):
        m = Decode(0,0,0,0,0,0)
        return m

    def case_14(self):
        m = Decode(1,2,2,0,0,0)
        return m

    def case_15(self):
        m = Decode(1,2,2,0,0,0)
        return m        
    
        
s = DecodeOpcode()
 
t = s.switch(3)

print(t.ret)
