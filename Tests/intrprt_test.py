from Interpreter.token_0_9 import *
from Interpreter.token_1_9 import *

t1 = Tokenizer0_9()
t2 = Tokenizer1_9()
test_set = '0123456789'

print(t1.interpret(test_set, 1))
print(t1.interpret(test_set, 9))
print(t2.interpret(test_set, 0))
print(t2.interpret(test_set, 7))