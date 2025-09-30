#dominos clone
import random
class dominos:
    menu={
        "veg":{"margerita":129,"cheese_and_corn":189,"pepper_paneer":260,"veg loaded":300,"tomato tangi":170},
        "non veg":{"pepper barbeque":199,"chicken roll":340,"chicken biriyani":200,"non veg loaded":300},
        "snacks":{"garlic bread":200,"chicken 65":100,"chicken cheese balls":230},
        "desserts":{"choco lava cake":290,"mousse":200,"zingy":290},
        "drinks":{"coca_cola":90,"sprite":60,"pepsi":40}
    }
    def __init__(self,name,email,phnno):
        self.name=name
        self.email=email
        self.phnno=phnno
        self.login_status=False#to validate login status
        self.cart={}#to store orders
        #main program
        while True:
            if not self.login_status:
                print("-------welcome to dominos app------------")
                print("login")
                ch=input("do you want to login(y/n):").lower()
                if ch=='y':
                    self.login()
            if self.login_status:
                print("user:",self.name)
                print("enter 1:order")
                print("enter 2:show cart")
                print("enetr 3:logout")
                choice=int(input("enter choice:"))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.cart()
                elif choice==3:
                    self.logout()
                else:
                    print("invalid")
    @staticmethod
    def validate_otp(value):
        while True:
            og_otp = random.randint(1000,9999)
            print(f"an otp ha sbeen send to {value}")
            print(f"your dominos otp is:{og_otp}")
            otp=int(input("enter otp:"))
            if otp == og_otp:
                print("login successfully")
                return True
            print("incorrect otp enter correct otp")


    def login(self):
        print("enter1:login with phnno")
        print("enter2:login with email")
        ch=int(input("enter choice:"))
        if ch==1:
            pass
        elif ch==2:
            pass
        else:
            print("invalid choice")
        if ch==1:
            #phno validation
            phnno=int(input("enter phnno:"))
            if phnno==self.phnno:
                state=self.validate_otp(phnno)
                self.login_status=state
            else:
                print("incorrect phnno")
        elif ch==2:
            #email validation
             email=input("enter email:")
             if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
             else:
                print("incorrect email")
        else:
            print("invalid choice🙁")
    def order(self):
        print("-----dominos menu--------")
        for category in dominos.menu:
            print(category)
        cat=input("enter category:")
        if cat in dominos.menu:
            d=dominos.menu[cat]
            for item in d:
                print(item,'rs.',d[item])
            item=input("enter item:")
            if item in d:
                q=int(input("enter quantity:"))
                if item in self.cart:
                    self.cart[item]+=d[item]*q
                else:
                    self.cart[item]=d[item]*q
                print(f"{item} added in cart")
                print(self.cart)
            else:
                print(f"{item} is not available")
        else:
            print(f"{cat} is not available")
    
    
    def show_cart(self):
        print("-----dominos cart-----")
        if self.cart!={}:
            total_bill=0
            for item in self.cart:
                print({item},'...rs', self.cart[item])
                total_bill+=self.cart[item]
            print(f"total amount:",total_bill)
        else:
            print("cart is empty plz order")
        ch=input("do you want to place the order(y/n):").lower()
        if ch=='y':
            print("thank you for placing the order ")
            print("your order is on the way")
            self.cart={}
    def logout(self):
        ch=input("do you want to logout?(y/n):").lower()
        if ch=='y':
            self.login_status=False
            print("logged out") 
ob=dominos("karthika","karthi@com",1234)