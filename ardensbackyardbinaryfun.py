args,commands,variables="",["variables[args[0:4]]=args[4:8]","print((chr(stb(variables[args[1:5]])))if'1'==args[0]else chr(stb(args[1:5])),end='')",'variables[args[0:4]]=input("? ")',"variables[args[0:4]]=bin(stb(variables[args[0:4]])+(stb(variables[args[0:4]])if args[0:4]in variables else stb(args[0:4]))).removeprefix('0b')"],{}
def stb(a):return eval("0b"+str(a))
while 1:
    inpt=input("] ")
    args=inpt[2:10]
    try:exec(commands[stb(inpt[0:2])])
    except SyntaxError:print("ur stupid, learn binary.")
    except KeyError:print("ur stupid, no forget about deta")
    except:print("ur stupid")