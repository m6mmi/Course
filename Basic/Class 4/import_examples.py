# Option 1
import main_functions
main_functions.greet("Janek")

# Option 2
from main_functions import get_action
get_action()

# Option 3
import main_functions as fns
fns.greet("Riina")

# Option 4
from main_functions import greet, get_action
greet("Riina")
get_action()

# Option 5
from main_functions import *
greet("Maiken")
get_action()
get_entry_details()

