from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape

# Luis Gerson Rodriguez Sanchez
# Turin Machine 
# Run a multiplication turin Machine 
# Theory of computation 
# December 3 rd 2020 
print('insert your tape with a 0 at the END !!!!')
in_User=input(); 
tape = Tape(in_User, '')
states = [
            State("s0", StateType.Start),
            State("s1", StateType.Empty),
            State("s2", StateType.Empty),
            State("s3", StateType.Empty),
            State("s4", StateType.Empty),
            State("s5", StateType.Empty),
            State("s6", StateType.Empty),
            State("sf", StateType.Final)
         ]
 
transitions = [
                 Transition("s0", "S", "s0", "S", Direction.Right),
                 Transition("s0", "0", "s6", "S", Direction.Right),
                 Transition("s0", "1", "s1", "S", Direction.Right),
                 Transition("s1", "1", "s1", "1", Direction.Right),
                 Transition("s1", "0", "s2", "0", Direction.Right),
                 Transition("s2", "1", "s3", "Y", Direction.Right),
                 Transition("s2", "0", "s5", "0", Direction.Left),
                 Transition("s3", "1", "s3", "1", Direction.Right),
                 Transition("s3", "0", "s3", "0", Direction.Right),
                 Transition("s3", "S", "s4", "1", Direction.Left),
                  Transition("s4", "1", "s4", "1", Direction.Left),
                 Transition("s4", "0", "s4", "0", Direction.Left),
                 Transition("s4", "Y", "s2", "Y", Direction.Right),
                 Transition("s5", "0", "s5", "0", Direction.Left),
                 Transition("s5", "1", "s5", "1", Direction.Left),
                 Transition("s5", "Y", "s5", "1", Direction.Left),
                 Transition("s5", "S", "s0", "S", Direction.Right),
                 Transition("s6", "1", "s6", "S", Direction.Right),
                 Transition("s6", "0", "sf", "S", Direction.Neutral)
              ]
 
tm = TuringMachine(states, transitions, tape)
tm.process(True)
print(tm.get_tape())