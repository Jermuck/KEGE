alf = "0123456789ABCDEF";
alf_chet = "12468ACE";

# asfa
def f(x):
    N16 = hex(x)[2:];
    NW16 = N16.replace("A", "1")
    print(NW16)