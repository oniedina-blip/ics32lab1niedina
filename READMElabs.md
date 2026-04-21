lab2: what was wrong with lab2: 
use int(a) so it crashes on 5.0
divide without checking so it crashes on / 0
no error handling so program stops instead of continuing

what I did with lab2:
try: for risky code
except ValueError: catches bad inputs 
except ZeroDivisionError: catches / 0
while True + continue (restarts cleanly)

lab4:
what was required for lab4:

REQ-1:
test is_int using assert with different inputs (valid and invalid)

REQ-2:
check that remove_note raises FileNotFoundError when file is missing

REQ-3:
modify remove_note so it raises error instead of returning


what I did:

REQ-1:
used assert statements with numbers, strings, and invalid values

REQ-2:
deleted pynote.txt and used try/except to confirm FileNotFoundError is raised

REQ-3:
changed remove_note to raise FileNotFoundError instead of returning
and left instructions as comments as required
