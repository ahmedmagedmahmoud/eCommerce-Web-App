from .base import *

from .production import *

# from .local import *

# Ordering is important: The last import will overwrite previous ones
# for any local setting we should put it in a try block; so if there are problems
# they will be ignored in live production
# but when working locally , remove try block
try:
    from .local import *
except:
    pass
