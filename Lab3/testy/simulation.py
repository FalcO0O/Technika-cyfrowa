class MusicPlayerSimulator:
    def __init__(self):
        self.state = {
            'S': 0,  # 0 = STOP, 1 = PLAY
            'Q1': 0, # Higher bit of track number (0-3)
            'Q0': 0  # Lower bit of track number (0-3)
        }
    
    def get_track_number(self):
        return (self.state['Q1'] << 1) | self.state['Q0']
    
    def get_state_name(self):
        mode = "PLAY" if self.state['S'] else "STOP"
        track = self.get_track_number()
        return f"{mode}_{track}"
    
    def update_state(self, b1, b0):
        # Calculate next state using your minimized functions
        s_next = (not b1 and b0) or (self.state['S'] and b1)
        q1_next = ((not self.state['Q1'] and not self.state['Q0'] and b1 and b0) or 
                   (not self.state['Q1'] and self.state['Q0'] and b1 and not b0) or 
                   (self.state['Q1'] and not self.state['Q0'] and not b0) or 
                   (self.state['Q1'] and self.state['Q0'] and b0) or 
                   (self.state['Q1'] and not b1))
        q0_next = ((not self.state['Q0']) and b1) or (self.state['Q0'] and not b1)
        
        # Update state
        self.state['S'] = s_next
        self.state['Q1'] = q1_next
        self.state['Q0'] = q0_next
    
    def process_command(self, command):
        if command == "play":
            self.update_state(0, 1)
        elif command == "stop":
            self.update_state(0, 0)
        elif command == "next":
            self.update_state(1, 0)
        elif command == "prev":
            self.update_state(1, 1)
        else:
            print("Unknown command. Available commands: play, stop, next, prev")

def main():
    player = MusicPlayerSimulator()
    print("Music Player Simulator")
    print("Available commands: play, stop, next, prev, exit")
    print(f"Initial state: {player.get_state_name()}")
    
    while True:
        command = input("\nEnter command: ").lower()
        if command == "exit":
            break
            
        player.process_command(command)
        print(f"Current state: {player.get_state_name()}")
        print(f"Playing: Track {player.get_track_number()}")
        print(f"Mode: {'Playing' if player.state['S'] else 'Stopped'}")

if __name__ == "__main__":
    main()