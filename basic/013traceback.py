import traceback
def l(): return a()
def a(): traceback.print_stack()
l()