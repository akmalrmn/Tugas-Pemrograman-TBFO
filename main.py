import os, sys
from htmlstring import HTMLToString

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ORANGE = '\033[38;5;208m'

class PDA:
    def __init__(self, file_path):
        """
        Inisialisasi objek PDA dengan file path yang diberikan.

        Args:
            file_path (str): Path file yang berisi konfigurasi PDA.
        """
        self.start_input = ""
        self.accept = False
        self.accepted_config = []
        self.transitions = {}
        self.start_state, self.bottom_stack, self.acceptable_states, self.type = self.parse_file(file_path)

    def parse_file(self, file_path):
        """
        Membaca file konfigurasi PDA dan mengembalikan nilai-nilai yang diperlukan.

        Args:
            file_path (str): Path file yang berisi konfigurasi PDA.

        Returns:
            tuple: Tuple berisi nilai-nilai yang diperlukan untuk inisialisasi objek PDA.
        """
        while not os.path.exists(file_path):
            print(f"Error: File tidak ditemukan - {file_path}")
            file_path = input("Tolong masukkan file path PDA dengan benar: ")

        with open(file_path) as file:
            lines = [line.rstrip() for line in file]

        for line in lines[7:]:
            transition = line.split()
            self.add_transitions(transition[0], transition[1], transition[2], transition[3], transition[4])

        return lines[3], lines[4], lines[5].split(), lines[6]

    def add_transitions(self, state, input_symbol, stack_symbol, next_state, push_stack):
        """
        Menambahkan transisi ke dalam daftar transisi PDA.

        Args:
            state (str): State saat ini.
            input_symbol (str): Simbol input.
            stack_symbol (str): Simbol pada stack.
            next_state (str): State berikutnya.
            push_stack (str): Simbol yang akan ditambahkan ke stack.
        """
        self.transitions.setdefault(state, []).append(tuple(s if s != "~" else "" for s in (input_symbol, stack_symbol, push_stack, next_state)))
    
    def accepted(self, current_state, input, stack):
        """
        Memeriksa apakah konfigurasi saat ini diterima oleh PDA.

        Args:
            current_state (str): State saat ini.
            input (str): Input yang tersisa.
            stack (str): Isi stack.

        Returns:
            bool: True jika konfigurasi diterima, False jika tidak.
        """
        if input is None or len(input) > 0:
            return False

        if (self.type == "E" and len(stack) == 0) or (self.type == "F" and current_state in self.acceptable_states):
            return True

        return False
    
    def finish(self):
        """
        Menampilkan pesan "Accepted" jika konfigurasi diterima, atau "Syntax Error" jika tidak.
        """
        if self.accept:
            print(f"""{Color.GREEN}
                       ..........  .                    
              =@@@....................@@@=              
   .. ..    @@............................@@            
   ...   @@.......:..........:.:.......:.....@@         
   .   @@.................:.......:.:::::......@@   .   
      @........:::.:::..::::..::::::::::.::::....@   .  
    @@.....:......................................@@  . 
   @@...............@@..........@@....:............@@   
  @*...........::..@@@#........@@@=.................*@  
 @%...:..:::.......@@@@........@@@@..................*@ 
 @......:..........@@@@...:....@@@@.....:.......::....@ 
 @.................@@@#........@@@=.:...:.............@ 
=........:..........@@..........@@.....................:
%......::::............................::::............*
*.....:::......:.......................................=
*........................................::............=
%.......@..................::..................@.......*
=.......@......................................@.......:
 @......@@...........:........................@@......@ 
 @....:..@@..............................:...@@.......@ 
 @%...:...@@...............::...:...........@@.......*@ 
  @+..:....@@@............................@@@.......+@  
   @@........@@@.................:......@@@........@@   
    @@...::....@@@@..................@@@@.........@@    
      @....:......@@@@@@@@@@@@@@@@@@@@.....:.....@   .. 
       @@.....:.......#@@@@@@@@@@+.......::....@@     . 
         @@.....::....................:......@@         
       .    @@............................@@            
              =@@%....................%@@=              
                    .  ..........  .                                           
            {Color.END}""")
            print(f"{Color.GREEN}{Color.BOLD}Accepted{Color.END}")
            print(f"{Color.GREEN}Yay! Syntax HTML kamu benar! :D{Color.END}\n")
        else:
            print(f"{Color.RED}{Color.BOLD}Syntax Error{Color.END}\n")
        
        self.reset()

    def reset(self):
        """
        Mengatur ulang status PDA menjadi tidak diterima.
        """
        self.accept = False
        self.accepted_config = []
    
    def print_config(self, config):
        """
        Mencetak konfigurasi PDA.

        Args:
            config (list): Daftar konfigurasi PDA.
        """
        for i in config:
            print(i)

    def generate(self, state, input, stack, config):
        """
        Menghasilkan konfigurasi PDA berikutnya berdasarkan konfigurasi saat ini.

        Args:
            state (str): State saat ini.
            input (str): Input yang tersisa.
            stack (str): Isi stack.
            config (list): Daftar konfigurasi saat ini.

        Returns:
            bool: True jika konfigurasi diterima, False jika tidak.
        """
        if self.accept:
            return False
        
        if self.accepted(state, input, stack):
            self.accept = True
            self.accepted_config.extend(config)
            return True

        valid = False
        moves = self.get_moves(state, input, stack) or []
        for move in moves:
            next_state, next_input, next_stack = move
            valid = self.generate(next_state, next_input, next_stack, config + [move])
            
        return valid

    def get_moves(self, state, input, stack):
        """
        Mendapatkan daftar langkah yang mungkin berikutnya berdasarkan konfigurasi saat ini.

        Args:
            state (str): State saat ini.
            input (str): Input yang tersisa.
            stack (str): Isi stack.

        Returns:
            list: Daftar langkah yang mungkin berikutnya.
        """
        moves = []

        if state in self.transitions:
            for current in self.transitions[state]:
                next_state, read_input, stack_symbol = current[3], current[0], current[1]

                if (not read_input or (input and 
                                       ((input[0] == read_input) or 
                                        (input[0] == ' ' and read_input == '#') or 
                                        (read_input == 'any') or 
                                        (read_input[0] == '!' and len(read_input) == 2 and input[0] != read_input[1])))) and \
                    (not stack_symbol or (stack and stack[0] == stack_symbol)):

                    new_input = input[1:] if read_input else input
                    new_stack = current[2] + stack[1:] if stack_symbol else current[2] + stack
                    moves.append((next_state, new_input, new_stack))
        
        return moves
    
    def process_input(self):
        """
        Memproses input dari pengguna dan menjalankan PDA.
        """
        print(f"""{Color.ORANGE}
  +++++++++++++++++++++++++++++++++++++  
  +++++++++++++++++++++++++++++++++++++  
  +++++++++++++++++++++++++++++++++++++  
  ++++++++++++++++++++++++++++++++++++   
   ++++++:...........          .++++++   
   ++++++:...........          .++++++   
   ++++++-....==================++++++   
   +++++++....=+++++++++++++++++++++++   
   +++++++....-+++++++++++++++++++++++   
    ++++++...........         .++++++    
    ++++++:..........         :++++++    
    +++++++===============.   :++++++    
    +++++++====++++++++++=    -++++++    
    ++++++=....++++++++++-   .+++++++    
    +++++++....-++++++++=:   .+++++++    
     ++++++..........        .++++++     
     ++++++=:........       .=++++++     
     +++++++++++++-:.::=++++++++++++     
     +++++++++++++++++++++++++++++++     
     +++++++++++++++++++++++++++++++     
         +++++++++++++++++++++++         
               +++++++++++                               
        {Color.END}""", end='\n')
        html_path = input("Masukkan file html: ")
        self.start_input = HTMLToString(html_path)

        while html_path != "exit":
            try:
                if not self.generate(self.start_state, self.start_input, self.bottom_stack,
                                        [(self.start_state, self.start_input, self.bottom_stack)]):
                    self.finish()
                else:
                    # self.print_config(self.accepted_config)
                    self.finish()
            except FileNotFoundError:
                print(f"Error: File tidak ditemukan - {html_path}")
            finally:
                html_path = input("Masukkan file html: ")
                if html_path != "exit":
                    self.start_input = HTMLToString(html_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <pda_path>")
    else:
        file_path = sys.argv[1]
        pda = PDA(file_path)
        pda.process_input()
