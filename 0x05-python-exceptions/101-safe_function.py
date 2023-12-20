#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        sys.stderr.write("Exception:{}\n".format(e))
        return None
