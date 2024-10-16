#ex: verify whether the value of different types of variables passed to a function get modified in the main program, if they are changed inside the function.

def mod_int(n):
    n=n+1
   
def mod_float(n) :
    n=n+1.
    
def mod_complex(n) :
    n=n+1.
    
def mod_bool(x) :
    if x == True :
       x = False
    if x == False :
       x = True

def mod_str(s) :
    s = 'moficicated'
     
i = 1
f = 1.
c = 1 + 1j
b = True
s = 'original'

mod_int(i)
mod_float(f)
mod_complex(c)
mod_bool(b)
mod_str(s)

print (i)
print (f)
print (c)
print (b)
print (s)
