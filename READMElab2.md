what was wrong with lab2: 
use int(a) so it crashes on 5.0
divide without checking so it crashes on / 0
no error handling so program stops instead of continuing

what I did with lab2:
try: for risky code
except ValueError: catches bad inputs 
except ZeroDivisionError: catches / 0
while True + continue (restarts cleanly)
