__WEBSITE = None

def initWEBSITE(name):
    global __WEBSITE
    if __WEBSITE is None:
        __WEBSITE = name
    else:
        raise RuntimeError("Website name has already been set.")

def visitWEBSITE():
    print("TODO, add code to query %s" % __WEBSITE)

def updateWEBSITE():
    print("TODO, add code to update %s" % __WEBSITE)


initWEBSITE("www.thebeatlesrock.co.uk")
visitWEBSITE()
updateWEBSITE()