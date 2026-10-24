# GPU fault drill

Card start limit 400 W; step 60 s; commit e3b05dc.

PASS  crash: the governor killed outright, the watchdog handed the card back (limit 400 W, start 400 W)
PASS  switch: the master switch pulled, the governor handed back and exited (limit 400 W)
PASS  switch: while OFF, a governor refuses to start
PASS  blind: the response-time feed stopped, the governor failed up (ceiling to the top, the lid to the start)
PASS  end: the card at its own start limit (400 W)

Passed 5 of 5.
