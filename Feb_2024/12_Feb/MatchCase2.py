browser = (input("Enter the browser name : "))
match browser:
    case 'chrome' :
        print("chrome code executed")
    case 'firefox':
        print("FF code executed")
    case _ :
        print("No browser found")