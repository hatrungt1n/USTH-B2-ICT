class Tape(object):
   blank_symbol = " "
   def __init__(self,
                input=""):
       self.__tape = {}
       for i in range(len(input)):
           self.__tape[i] = input[i]
      
   def __str__(self):
       s = ""
       min_used_index = min(self.__tape.keys())
       max_used_index = max(self.__tape.keys())
       for i in range(min_used_index,max_used_index):
           s += self.__tape[i]
       return s   
  
 
   def __getitem__(self,index):
       if index in self.__tape:
           return self.__tape[index]
       else:
           return blank_symbol
 
   def __setitem__(self, pos, char):
       self.__tape[pos] = char
 
      
class TuringMachine(object):
   def __init__(self,
                tape = "",
                blank_symbol = " ",
                tape_alphabet = ["0", "1"],
                initial_state = "",
                accepting_states = [],
                final_states = [],
                transition_function = {}):
       self.__tape = Tape(tape)
       self.__head_position = 0
       self.__blank_symbol = blank_symbol
       self.__current_state = initial_state
       self.__transition_function = transition_function
       self.__tape_alphabet = tape_alphabet
       self.__final_states = final_states
      
   def show_tape(self):
       print(self.__tape)
       return True
  
   def step(self):
       char_under_head = self.__tape[self.__head_position]
       x = (self.__current_state, char_under_head)
       if x in self.__transition_function:
           y = self.__transition_function[x]
           self.__tape[self.__head_position] = y[1]
           if y[2] == "R":
               self.__head_position += 1
           elif y[2] == "L":
               self.__head_position -= 1
           self.__current_state = y[0]
 
   def final(self):
       if self.__current_state in self.__final_states:
           return True
       else:
           return False
 
initial_state = "init",
accepting_states = ["final"],
transition_function = {("init","0"):("init", "1", "R"),
                      ("init","1"):("init", "0", "R"),
                      ("init"," "):("final"," ", "N"),
                      }
final_states = ["final"]
inp = input("Input on Tape: ")
blank_symbol = " "
t = TuringMachine(inp + blank_symbol,
                 initial_state = "init",
                 final_states = final_states,
                 transition_function=transition_function)
 
print("Your input on Tape:")
t.show_tape()
 
while not t.final():
   t.step()
 
print("Result of the Turing machine calculation:")   
t.show_tape()
