print("WELCOME TO DEVTESTER")
print("ENTER AT YOUR OWN RISK")

devs = ["Conrad", "Jim"]
stopped = False
while (stopped != True):
    developer = input('ENTER NAME:')
    print( "Hello " + developer)

        # loop through array of names
    devs_found = []
    for name in devs:
        if developer.lower() == name.lower():

            devs_found.append(developer)
    if (devs_found != []):
        print(devs_found[0] + ", you are indeed, a dev. welcome")
        stopped = True
    elif developer.lower() == "":
       print("You must input a name, restarting")
    else:
        print("We have no record of you being a dev.")
        stopped = True
        print("Is This an error? Y/N?")
        resp = input()
        if (resp == "Y"):
            print("TOO BAD SO SAD")
            admincheck = input()
            if (admincheck.lower() == "admin"):
                print("WELCOME TO TOP SECRET ADMIN MENU")
                admin_adduser = input("ADD A DEV: ")
                if (admin_adduser != ""):
                    devs.append(admin_adduser)
                    print("User Added, restarting")
                    stopped = False
        else:
            print("OK")

                # else:
        #     print("We have no record of you being a dev, if you are a dev and this is an error please add your name to our record")
        #     stopped = True

            # print(developer + ", you are a indeed, a Developer")
            # stopped = True
        # elif developer.lower() == "":
        #     print("You must input a name, restarting")