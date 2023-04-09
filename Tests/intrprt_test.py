from Interpreter.token_0_9 import *
from Interpreter.token_1_9 import *
from Interpreter.token_0_9_plus import *
from Interpreter.token_n import *
from Interpreter.token_z import *


t1 = Tokenizer0_9()
t2 = Tokenizer1_9()
t3 = Tokenizer0_9_plus()
t4 = Tokenizer_N()
t5 = Tokenizer_Z()
test_set = '+01023456789'

#
# print(t1.interpret(test_set, 1))
# print(t1.interpret(test_set, 9))
# print(t2.interpret(test_set, 0))
# print(t2.interpret(test_set, 7))


print(t3.interpret(test_set, 7))
print(t4.interpret(test_set, 0))
print(t5.interpret(test_set, 0))