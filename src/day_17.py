class Program:
    def __init__(self, program, A, B, C):
        self.program = program
        self.A = A
        self.B = B
        self.C = C
        self.instruction_pointer = 0
        self.output = []

    def run(self):
        while self.instruction_pointer < len(self.program):
            self.execute_instruction()
            
    def execute_instruction(self):
        opcode = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]
        
        if opcode == 0:
            self.A = int(self.A // 2 ** self.get_combo_operand(operand))
        
        if opcode == 1:
            self.B = self.B ^ operand
        
        if opcode == 2:
            self.B = self.get_combo_operand(operand) % 8
        
        if opcode == 3:
            if self.A == 0:
                pass
            else:
                self.instruction_pointer = operand - 2
            
        if opcode == 4:
            self.B = self.B ^ self.C
            
        if opcode == 5:
            self.output.append(self.get_combo_operand(operand) % 8)
        
        if opcode == 6:
            self.B = int(self.A // 2 ** self.get_combo_operand(operand))
        
        if opcode == 7:
            self.C = int(self.A // 2 ** self.get_combo_operand(operand))
            
        self.instruction_pointer += 2
        
    def get_combo_operand(self, operand):
        if operand < 4:
            return operand
        elif operand < 7:
            return self.A if operand == 4 else self.B if operand == 5 else self.C
        else:
            return None

program_instructions = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]

for init_A in range( 8 ** ( len(program_instructions) - 1), 8 ** len(program_instructions)):
    program = Program(program_instructions, A=init_A, B=0, C=0)
    program.run()

    if program.output == program_instructions:
        print(init_A)
        break