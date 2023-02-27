import inkex
import sys

def check(expression, error_message):
    '''If 'expression' is False, display 'error_message' and abort.'''
    if not expression:
        inkex.errormsg(error_message)
        sys.exit(1)

def log(*messages):
    '''Display 'messages'.'''
    print(' '.join([str(message) for message in messages]), file=sys.stderr)
