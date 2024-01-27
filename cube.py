import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os
import json


"""
Before running this code, make sure to install the required libraries by using the following commands:

1. Install Matplotlib:
pip install matplotlib

2. Install NumPy:
pip install numpy

"""


class Cube:
    """
    Represents a cube with defined corners and edges.

    Attributes:
    - corner_front_bottom_left (int): Corner at the front bottom left of the cube.
    - corner_front_bottom_right (int): Corner at the front bottom right of the cube.
    - corner_back_bottom_right (int): Corner at the back bottom right of the cube.
    - corner_back_bottom_left (int): Corner at the back bottom left of the cube.
    - corner_front_top_left (int): Corner at the front top left of the cube.
    - corner_front_top_right (int): Corner at the front top right of the cube.
    - corner_back_top_right (int): Corner at the back top right of the cube.
    - corner_back_top_left (int): Corner at the back top left of the cube.

    - edge_front_bottom (str): Edge at the front bottom of the cube.
    - edge_bottom_right (str): Edge at the bottom right of the cube.
    - edge_back_bottom (str): Edge at the back bottom of the cube.
    - edge_bottom_left (str): Edge at the bottom left of the cube.
    - edge_front_left (str): Edge at the front left of the cube.
    - edge_front_right (str): Edge at the front right of the cube.
    - edge_back_right (str): Edge at the back right of the cube.
    - edge_back_left (str): Edge at the back left of the cube.
    - edge_front_top (str): Edge at the front top of the cube.
    - edge_top_right (str): Edge at the top right of the cube.
    - edge_back_top (str): Edge at the back top of the cube.
    - edge_top_left (str): Edge at the top left of the cube.

    Methods:
    - __init__(self): Initializes the cube with default corner and edge positions.
    - reset_state(self): Resets the cube to its default state.
    - set_state(self, corner_positions, edge_positions): Sets the cube's state based on given corner and edge positions.
    - save_cube_state(self, file_path): Saves the cube's state to a JSON file.
    - load_cube_state(self, file_path): Loads the cube's state from a JSON file.
    - move_u_clockwise(self): Rotates the upper layer of the cube clockwise.
    - move_u_counter_clockwise(self): Rotates the upper layer of the cube counter-clockwise.
    - move_d_clockwise(self): Rotates the lower layer of the cube clockwise.
    - move_d_counter_clockwise(self): Rotates the lower layer of the cube counter-clockwise.
    - move_f_clockwise(self): Rotates the front layer of the cube clockwise.
    - move_f_counter_clockwise(self): Rotates the front layer of the cube counter-clockwise.
    - move_b_clockwise(self): Rotates the back layer of the cube clockwise.
    - move_b_counter_clockwise(self): Rotates the back layer of the cube counter-clockwise.
    - move_l_clockwise(self): Rotates the left layer of the cube clockwise.
    - move_l_counter_clockwise(self): Rotates the left layer of the cube counter-clockwise.
    - move_r_clockwise(self): Rotates the right layer of the cube clockwise.
    - move_r_counter_clockwise(self): Rotates the right layer of the cube counter-clockwise.
    - get_cube_state(self): Returns the current state of the cube as a dictionary.
    - get_cycles(self): Finds and returns cycles in the cube's corner and edge positions.
    - move(self, moves_to_execute): Executes a sequence of cube moves based on input.
    - choose_moves(self): Prompts the user to input cube moves and returns a filtered list of valid moves.
    - state(self): Prints the current position of corners and edges and their cycle representation.
    - draw_cube(ax, position): Draws a single cube at the specified position in a 3D plot.
    - visualize_cube(self): Visualizes the entire cube by drawing multiple cubes in a 3D plot.

    """

    def __init__(self):
        """
        Initializes the cube with default corner and edge positions.
        """
        self.corner_front_bottom_left = 1
        self.corner_front_bottom_right = 2
        self.corner_back_bottom_right = 3
        self.corner_back_bottom_left = 4
        self.corner_front_top_left = 5
        self.corner_front_top_right = 6
        self.corner_back_top_right = 7
        self.corner_back_top_left = 8

        self.edge_front_bottom = 'a'
        self.edge_bottom_right = 'b'
        self.edge_back_bottom = 'c'
        self.edge_bottom_left = 'd'
        self.edge_front_left = 'e'
        self.edge_front_right = 'f'
        self.edge_back_right = 'g'
        self.edge_back_left = 'h'
        self.edge_front_top = 'i'
        self.edge_top_right = 'j'
        self.edge_back_top = 'k'
        self.edge_top_left = 'l'

    def reset_state(self):
        """
        Resets the cube to its default state.
        """
        self.__init__()

    def set_state(self, corner_positions, edge_positions):
        """
        Sets the cube's state based on given corner and edge positions.

        Parameters:
        - corner_positions (dict): Dictionary containing corner positions.
        - edge_positions (dict): Dictionary containing edge positions.

        Raises:
        - ValueError: If the length of corner_positions is not 8 or the length of edge_positions is not 12.
        """
        # Überprüfen, ob die übergebenen Dictionaries die richtige Anzahl von Elementen enthalten
        if len(corner_positions) != 8 or len(edge_positions) != 12:
            raise ValueError("The dictionaries must each contain 8 or 12 elements.")

        # Setzen der Stellungen der Ecken
        self.corner_front_bottom_left = corner_positions["corner_front_bottom_left"]
        self.corner_front_bottom_right = corner_positions["corner_front_bottom_right"]
        self.corner_back_bottom_right = corner_positions["corner_back_bottom_right"]
        self.corner_back_bottom_left = corner_positions["corner_back_bottom_left"]
        self.corner_front_top_left = corner_positions["corner_front_top_left"]
        self.corner_front_top_right = corner_positions["corner_front_top_right"]
        self.corner_back_top_right = corner_positions["corner_back_top_right"]
        self.corner_back_top_left = corner_positions["corner_back_top_left"]

        # Setzen der Stellungen der Kanten
        self.edge_front_bottom = edge_positions["edge_front_bottom"]
        self.edge_bottom_right = edge_positions["edge_bottom_right"]
        self.edge_back_bottom = edge_positions["edge_back_bottom"]
        self.edge_bottom_left = edge_positions["edge_bottom_left"]
        self.edge_front_left = edge_positions["edge_front_left"]
        self.edge_front_right = edge_positions["edge_front_right"]
        self.edge_back_right = edge_positions["edge_back_right"]
        self.edge_back_left = edge_positions["edge_back_left"]
        self.edge_front_top = edge_positions["edge_front_top"]
        self.edge_top_right = edge_positions["edge_top_right"]
        self.edge_back_top = edge_positions["edge_back_top"]
        self.edge_top_left = edge_positions["edge_top_left"]

    def save_state(self, file_path="Cube_State.json"):
        """
        Saves the cube's state to a JSON file.

        Parameters:
        - file_path (str): The path to the file where the cube state will be saved.
        """
        cube_state = self.get_cube_state()

        try:
            # Schutzfunktion: Prüfen, ob die Datei mit einem bestimmten Kennzeichen beginnt
            safe_signature = "Cube State"
            with open(file_path, 'w') as file:
                json.dump({"safe_signature": safe_signature, "cube_state": cube_state}, file)

            print(f"Cube State was saved in {file_path}.")
        except Exception as e:
            print(f"Error when saving the cube state: {e}")

    def load_state(self, file_path="Cube_State.json"):
        """
        Loads the cube's state from a JSON file.

        Parameters:
        - file_path (str): The path to the file from which the cube state will be loaded.
        """
        try:
            # Schutzfunktion: Prüfen, ob die Datei mit dem erwarteten Kennzeichen beginnt
            safe_signature = "Cube State"
            with open(file_path, 'r') as file:

                json_data = json.load(file)

                cube_safe_signature = json_data["safe_signature"]

                # Check whether the cube_safe_signature is correct
                assert cube_safe_signature == safe_signature, "Invalid file or file has been manipulated."

                # Parse the cube state from the JSON part of the file
                cube_state = json_data["cube_state"]
                
                # Set the cube state with the loaded values
                self.set_state(cube_state["corners"], cube_state["edges"])
                print(f"Cube State was loaded from {file_path}.")
        except FileNotFoundError:
            print("The specified file was not found.")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")
        except Exception as e:
            print(f"Error loading the cube state: {e}")

    def move_u_clockwise(self):
        """
        Rotates the cube's upper layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer U-Drehung
        self.corner_front_top_left, self.corner_front_top_right, self.corner_back_top_left, self.corner_back_top_right = \
            self.corner_back_top_right, self.corner_front_top_left, self.corner_front_top_right, self.corner_back_top_left

        # Drehung der Kanten entsprechend einer U-Drehung
        self.edge_front_top, self.edge_back_top, self.edge_top_left, self.edge_top_right = \
            self.edge_top_right, self.edge_front_top, self.edge_back_top, self.edge_top_left

    def move_u_counter_clockwise(self):
        """
        Rotates the cube's upper layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer U'-Drehung
        self.corner_front_top_left, self.corner_front_top_right, self.corner_back_top_left, self.corner_back_top_right = \
            self.corner_back_top_left, self.corner_front_top_right, self.corner_front_top_left, self.corner_back_top_right

        # Drehung der Kanten entsprechend einer U'-Drehung
        self.edge_front_top, self.edge_back_top, self.edge_top_left, self.edge_top_right = \
            self.edge_top_left, self.edge_front_top, self.edge_back_top, self.edge_top_right

    def move_d_clockwise(self):
        """
        Rotates the cube's bottom layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer D-Drehung
        self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_back_bottom_left, self.corner_back_bottom_right = \
            self.corner_back_bottom_right, self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_back_bottom_left

        # Drehung der Kanten entsprechend einer D-Drehung
        self.edge_front_bottom, self.edge_back_bottom, self.edge_bottom_left, self.edge_bottom_right = \
            self.edge_bottom_right, self.edge_front_bottom, self.edge_back_bottom, self.edge_bottom_left

    def move_d_counter_clockwise(self):
        """
        Rotates the cube's bottom layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer D'-Drehung
        self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_back_bottom_left, self.corner_back_bottom_right = \
            self.corner_back_bottom_right, self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_back_bottom_left

        # Drehung der Kanten entsprechend einer D'-Drehung
        self.edge_front_bottom, self.edge_back_bottom, self.edge_bottom_left, self.edge_bottom_right = \
            self.edge_bottom_right, self.edge_front_bottom, self.edge_back_bottom, self.edge_bottom_left

    def move_f_clockwise(self):
        """
        Rotates the cube's front layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_front_top_left, self.corner_front_top_right = \
            self.corner_front_top_left, self.corner_front_bottom_left, self.corner_front_top_right, self.corner_front_bottom_right

        self.edge_front_bottom, self.edge_front_left, self.edge_front_right, self.edge_front_top = \
            self.edge_front_top, self.edge_front_bottom, self.edge_front_top, self.edge_front_right

    def move_f_counter_clockwise(self):
        """
        Rotates the cube's front layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer F'-Drehung
        self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_front_top_left, self.corner_front_top_right = \
            self.corner_front_top_right, self.corner_front_bottom_left, self.corner_front_bottom_right, self.corner_front_top_left

        # Drehung der Kanten entsprechend einer F'-Drehung
        self.edge_front_bottom, self.edge_front_left, self.edge_front_right, self.edge_front_top = \
            self.edge_front_top, self.edge_front_bottom, self.edge_front_top, self.edge_front_right

    def move_b_clockwise(self):
        """
        Rotates the cube's back layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        self.corner_back_bottom_left, self.corner_back_top_left, self.corner_back_top_right, self.corner_back_bottom_right = \
            self.corner_back_top_right, self.corner_back_bottom_left, self.corner_back_bottom_right, self.corner_back_top_left

        self.edge_back_bottom, self.edge_back_left, self.edge_back_right, self.edge_back_top = \
            self.edge_back_top, self.edge_back_bottom, self.edge_back_top, self.edge_back_right

    def move_b_counter_clockwise(self):
        """
        Rotates the cube's back layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer B'-Drehung
        self.corner_back_bottom_left, self.corner_back_bottom_right, self.corner_back_top_left, self.corner_back_top_right = \
            self.corner_back_top_right, self.corner_back_bottom_left, self.corner_back_bottom_right, self.corner_back_top_left

        # Drehung der Kanten entsprechend einer B'-Drehung
        self.edge_back_bottom, self.edge_back_left, self.edge_back_right, self.edge_back_top = \
            self.edge_back_top, self.edge_back_bottom, self.edge_back_top, self.edge_back_right

    def move_l_clockwise(self):
        """
        Rotates the cube's left layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        self.corner_front_bottom_left, self.corner_back_bottom_left, self.corner_back_top_left, self.corner_front_top_left = \
            self.corner_back_bottom_left, self.corner_back_top_left, self.corner_front_top_left, self.corner_front_bottom_left

        self.edge_bottom_left, self.edge_back_left, self.edge_top_left, self.edge_front_left = \
            self.edge_back_left, self.edge_top_left, self.edge_front_left, self.edge_bottom_left

    def move_l_counter_clockwise(self):
        """
        Rotates the cube's left layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer L'-Drehung
        self.corner_front_bottom_left, self.corner_back_bottom_left, self.corner_back_top_left, self.corner_front_top_left = \
            self.corner_front_top_left, self.corner_front_bottom_left, self.corner_back_bottom

    def move_r_clockwise(self):
        """
        Rotates the cube's right layer clockwise.

        Updates the positions of corners and edges accordingly.
        """
        self.corner_front_bottom_right, self.corner_front_top_right, self.corner_back_top_right, self.corner_back_bottom_right = \
            self.corner_back_top_right, self.corner_front_bottom_right, self.corner_front_top_right, self.corner_back_bottom_right

        self.edge_front_right, self.edge_top_right, self.edge_back_right, self.edge_bottom_right = \
            self.edge_bottom_right, self.edge_front_right, self.edge_top_right, self.edge_back_right

    def move_r_counter_clockwise(self):
        """
        Rotates the cube's right layer counter-clockwise.

        Updates the positions of corners and edges accordingly.
        """
        # Drehung der Ecken entsprechend einer R'-Drehung
        self.corner_front_bottom_right, self.corner_back_bottom_right, self.corner_back_top_right, self.corner_front_top_right = \
            self.corner_front_top_right, self.corner_front_bottom_right, self.corner_back_bottom_right, self.corner_back_top_right

        # Drehung der Kanten entsprechend einer R'-Drehung
        self.edge_front_right, self.edge_back_right, self.edge_bottom_right, self.edge_top_right = \
            self.edge_top_right, self.edge_front_right, self.edge_back_right, self.edge_bottom_right

    def move(self, moves_to_execute):
        """
        Executes a sequence of cube moves.

        Args:
            moves_to_execute (list): List of cube moves to be executed.

        Raises:
            ValueError: If an invalid move is encountered.
        """
        move_mapping = {
            'U': self.move_u_clockwise,
            'U\'': self.move_u_counter_clockwise,
            'D': self.move_d_clockwise,
            'D\'': self.move_d_counter_clockwise,
            'F': self.move_f_clockwise,
            'F\'': self.move_f_counter_clockwise,
            'B': self.move_b_clockwise,
            'B\'': self.move_b_counter_clockwise,
            'L': self.move_l_clockwise,
            'L\'': self.move_l_counter_clockwise,
            'R': self.move_r_clockwise,
            'R\'': self.move_r_counter_clockwise
        }

        for move in moves_to_execute:
            if move == " ":
                continue
            try:
                move_function = move_mapping[move]
                move_function()
            except KeyError:
                print(f"Ungültiger Zug: {move}")
            except Exception as e:
                print(f"Fehler beim Ausführen des Zuges {move}: {e}")

    @staticmethod
    def choose_moves():
        """
        Prompts the user to input a sequence of cube moves.

        Returns:
            list: List of valid cube moves to be executed.

        Raises:
            ValueError: If no moves are provided by the user.
        """
        moves_to_execute = input("Welche Züge sollen gemacht werden? (Trennzeichen Komma (,)): ")

        if not moves_to_execute:
            raise ValueError("Bitte geben Sie mindestens einen Zug ein.")

        moves_to_execute = moves_to_execute.split(",")
        moves_to_execute = [move.upper() for move in moves_to_execute]

        valid_moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "L", "L'", "R", "R'"]
        invalid_moves = [move for move in moves_to_execute if move not in valid_moves]

        for invalid_move in invalid_moves:
            print(f"Ungültiger Zug: {invalid_move}")

        filtered_moves = [move for move in moves_to_execute if move in valid_moves]

        return filtered_moves

    def get_cube_state(self):
        """
        Returns the current state of the cube in terms of corner and edge positions.

        Returns:
            dict: Dictionary representing the cube state.
        """
        corner_state = {name: value for name, value in self.__dict__.items() if name.startswith("corner_")}
        edge_state = {name: value for name, value in self.__dict__.items() if name.startswith("edge_")}

        return {"corners": corner_state, "edges": edge_state}

    def get_cycles(self):
        """
        Determines the cycles in the corner and edge mappings of the cube.

        Returns:
            list: List of cycles in the cube's corner and edge mappings.
        """
        corner_mapping = {
            1: self.corner_front_bottom_left,
            2: self.corner_front_bottom_right,
            3: self.corner_front_top_left,
            4: self.corner_front_top_right,
            5: self.corner_back_bottom_left,
            6: self.corner_back_bottom_right,
            7: self.corner_back_top_left,
            8: self.corner_back_top_right
        }

        edge_mapping = {
            'a': self.edge_front_bottom,
            'b': self.edge_front_left,
            'c': self.edge_front_right,
            'd': self.edge_front_top,
            'e': self.edge_back_bottom,
            'f': self.edge_back_left,
            'g': self.edge_back_right,
            'h': self.edge_back_top,
            'i': self.edge_bottom_left,
            'j': self.edge_bottom_right,
            'k': self.edge_top_left,
            'l': self.edge_top_right
        }

        cycles = []

        @staticmethod
        def find_cycle(mapping):
            cycle = []
            visited = set()
            for start in mapping:
                if start not in visited:
                    current = start
                    while current not in visited:
                        visited.add(current)
                        cycle.append(current)
                        current = mapping[current]
                    if cycle:
                        cycles.append(cycle[:])
                    cycle.clear()

        find_cycle(corner_mapping)
        find_cycle(edge_mapping)

        return cycles

    def state(self):
        """
        Prints the current position and cycle representation of the cube.
        """
        cube_state = self.get_cube_state()
        print("Position:")
        for key, value in cube_state.items():
            print(f"{key}: {value}")

        current_cycles = self.get_cycles()
        print("Cycle display:")
        print(current_cycles)

    @staticmethod
    def draw_cube(ax, position):
        """
        Draws a single cube at the specified position in a 3D plot.

        Args:
            ax (matplotlib.axes._subplots.Axes3D): 3D plot axis.
            position (list): List representing the position of the cube.
        """
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]) + position

        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[7], vertices[6], vertices[2], vertices[3]],
            [vertices[0], vertices[4], vertices[7], vertices[3]],
            [vertices[1], vertices[5], vertices[6], vertices[2]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]
        ]

        cube = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.0)
        ax.add_collection3d(cube)

    def visualize_cube(self):
        """
        Visualizes the cube by drawing multiple cubes in a 3D plot.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        num_cubes = 3

        for x in range(num_cubes):
            for y in range(num_cubes):
                for z in range(num_cubes):
                    self.draw_cube(ax, position=[x, y, z])

        # Koordinaten der Ecken
        corners_coordinates = {
            self.corner_front_bottom_left: (0, 0, 0),
            self.corner_front_bottom_right: (3, 0, 0),
            self.corner_back_bottom_right: (3, 3, 0),
            self.corner_back_bottom_left: (0, 3, 0),
            self.corner_front_top_left: (0, 0, 3),
            self.corner_front_top_right: (3, 0, 3),
            self.corner_back_top_right: (3, 3, 3),
            self.corner_back_top_left: (0, 3, 3),
        }

        # Koordinaten der Kanten
        edges_coordinates = {
            self.edge_front_bottom: (1.5, 0, 0),
            self.edge_bottom_right: (3, 1.5, 0),
            self.edge_back_bottom: (1.5, 3, 0),
            self.edge_bottom_left: (0, 1.5, 0),
            self.edge_front_left: (0, 0, 1.5),
            self.edge_front_right: (3, 0, 1.5),
            self.edge_back_right: (3, 3, 1.5),
            self.edge_back_left: (0, 3, 1.5),
            self.edge_front_top: (1.5, 0, 3),
            self.edge_top_right: (3, 1.5, 3),
            self.edge_back_top: (1.5, 3, 3),
            self.edge_top_left: (0, 1.5, 3),
        }


        for corner, (x, y, z) in corners_coordinates.items():
            ax.text(x, y, z, str(corner), color='black', fontsize=22, ha='center', va='center')

        for edge, (x, y, z) in edges_coordinates.items():
            ax.text(x, y, z, str(edge), color='black', fontsize=20, ha='center', va='center')

        ax.set_xlim([0, num_cubes])
        ax.set_ylim([0, num_cubes])
        ax.set_zlim([0, num_cubes])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.axis('off')

        plt.show()

    def get_method_descriptions(self):
        """
        Retrieves method names, their docstrings, and the class description from the Cube class.

        Returns:
            tuple: A tuple containing the class description (str) and a list of tuples.
                Each tuple in the list represents a method with its name (str) and docstring (str).
        """
        class_description = self.__doc__.strip() if self.__doc__ else "No class description available."

        method_descriptions = []

        for method_name in dir(self):
            if callable(getattr(self, method_name)) and not method_name.startswith("__"):
                method = getattr(self, method_name)
                docstring = method.__doc__.strip() if method.__doc__ else "No description available."
                method_descriptions.append((method_name, docstring))

        return class_description, method_descriptions

    def description(self, method_name=None):
        """
        Prints the descriptions of Cube class and its methods.

        Parameters:
        - method_name (str): Optional. The name of the specific method for which the description is requested.

        If method_name is not provided, prints the description of the Cube class.
        If method_name is provided, prints the description of the specified method.

        """
        class_description, method_descriptions = self.get_method_descriptions()

        if method_name:
            # Print the description of the specified method
            for name, description in method_descriptions:
                if name == method_name:
                    print(f"{name}: {description}")
                    return
            print(f"Method '{method_name}' not found.")
        else:
            # Print the description of the Cube class
            print("Class description:")
            print(class_description)

            print("\nMethods description:")
            for name, description in method_descriptions:
                print(f"{name}: {description}")


def introduce_user():
    """
    Briefly introduces the user to the `cube.py` file.
    """

    print(f"""
    Welcome to the {os.path.basename(__file__)} file!

    This file contains a class called `Cube`, which represents a 3x3x3 cube.

    To create a new cube, use the following code:

    ```python
    cube = Cube()
    ```

    To get the description of all methods, use the following code:

    ```python
    cube.description()
    ```

    To display the current state of the cube, use the following code:

    ```python
    cube.state()
    ```

    Here are some examples of moves:

    ```python
    cube.move("F") # Rotates the top layer clockwise
    cube.move("R") # Rotates the right layer clockwise
    cube.move("U") # Rotates the top layer counterclockwise
    ```

    To visualize the cube, use the following code:

    ```python
    cube.visualize_cube()
    ```

    Where 'F' stands for a clockwise rotation of the upper layer.

    For more information on using the `cube.py` file, see the documentation.
    """)

if not __name__ == "__main__":
    introduce_user()

if __name__ == "__main__":
    introduce_user()
    cube = Cube()
    cube.description()
