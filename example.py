from cube import Cube

def main():
    # Create an instance of the Cube class
    cube = Cube()

    # Execute some moves
    moves_to_execute = ["U", "R", "F", "U'", "R'", "F'"]
    cube.move(moves_to_execute)

    # Show the current state
    print("Current state:")
    cube.state()

    # Save the state in a JSON file
    cube.save_state("cube_state.json")
    print("State was saved in 'cube_state.json'.")

if __name__ == "__main__":
    main()
