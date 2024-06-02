import sys

# Constants
TOTAL_ROUNDS = 200

# Read command-line arguments
round_no = int(sys.argv[1])
prev_res = sys.argv[2] if len(sys.argv) > 2 else "NONE"

# Determine the current response based on the strategy
if round_no == 1:
    # Start by saying "YES" in the first round
    my_res = "YES"
elif round_no == TOTAL_ROUNDS:
    # Always say "NO" in the 200th round
    my_res = "NO"
else:
    # For all other rounds, copy the opponent's previous response
    my_res = prev_res if prev_res != "NONE" else "YES"

# Print the current response
print(my_res)