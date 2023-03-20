class Automat:
    def __init__(self, config_file):
        config_file = open(config_file, 'r')
        self.initial_state = ""
        self.final_states = []
        self.transitions = {}
        # transitions = {curentstate{letter[nextstate]}}
        for line in config_file:
            if line.strip() == "":
                continue
            if line.strip() == "Initial_State":
                state = 0
                continue
            elif line.strip() == "Final_States":
                state = 1
                continue
            elif line.strip() == "Transitions":
                state = 2
                continue

            if state == 0:
                if self.initial_state == "":
                    self.initial_state = line.strip()
                else:
                    raise Exception("Can't have more than one initial state!")
            elif state == 1:
                self.final_states.append(line.strip())
            elif state == 2:
                aux = line.strip().split(',')
                current_state = aux[0].strip()
                letter = aux[1].strip()
                next_state = aux[2].strip()
                if current_state not in self.transitions.keys():
                    self.transitions[current_state] = {}

                if letter not in self.transitions[current_state].keys():
                    self.transitions[current_state][letter] = []

                self.transitions[current_state][letter].append(next_state)

        if self.initial_state == "":
            raise Exception("No initial state!")

        config_file.close()

    def acceptWord(self, word, current_state = None, drum = []):
        if current_state == None:
            current_state = self.initial_state
        drum.append(current_state)
        if word == "":
            if current_state in self.final_states:
                return "acceptat"
            else:
                return "neacceptat"
        curent_letter = word[0]
        if curent_letter in self.transitions[current_state].keys():
            for next in self.transitions[current_state][curent_letter]:
                return self.acceptWord(word[1:], next, drum)
        else:
            return "neacceptat"


if __name__ == '__main__':
    myAutomat = Automat("automat.txt")
    cuvinte = open("input.txt", "r")
    for cuvant in cuvinte:
        drum = []
        print(myAutomat.acceptWord(cuvant.strip(), drum=drum), drum)
    cuvinte.close()