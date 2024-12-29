class start_shopping:
    #Generic states:
    shop_name='Sandy_Mobile_zone'
    address='Chennai'
    mobile=9360280482
    owner='Santhosh'
    #available_products={'products name':[Qty,price ,per product]}
    available_products={'realme':[10,20000],
                        'samsung':[5,120000],
                        'iphone':[7,150000],
                        'vivo':[6,12000],
                        'oppo':[8,25000]
                        }

    def display_products(self):
        print(f"\nProducts availble in {s1.shop_name}")
        print('--------------------------------------')
        print("Products : [Quantity  ,  Price]")
        print("------------------------------------")
        for products,likes in self.available_products.items():
            print(f"{products}  :  {likes}")
        print('-----------------------------------')

    #customer cart details:
    def customer_cart(self):
        print("Products Available in your cart :")
        if self.cart=={}:
            print('-------------------------------')
            print("____Your cart is empty !!_____")
        else:
            print('---------------------------------')
            for products in self.cart.items():
                print(f"{products}")
            print('---------------------------------')
            sum=0
            for fly,flys in self.cart.items():
                sum=sum+flys[1]
            print(f"Total Cart Price : {sum}")
            print('----------------------------------')
    
    #object specific states:
    def __init__(self,name,mobile,location,cart):
        self.name=name
        self.mobile=mobile
        self.location=location
        self.cart=cart

    def customer_details(self):
        print("\nName:",self.name)
        print("Mobile:",self.mobile)
        print("location:",self.location)
        if self.cart=={}:
            print('\n----products Available in your cart----')
            print('--------------------------------')
            print("____Your cart is Empty!!_____")
        else:
            print('\n---Products Available in your cart----')
            print('----------------------------------------')
            print("Products  :  [Quantity , Price]")
            print('----------------------------------------')
            for product,likes in self.cart.items():
                print(f"{product}  :  {likes}")
            print('----------------------------------------')
            sum=0
            for fun,funs in self.cart.items():
                sum=sum+funs[1]
            print(f"Total Cart price : {sum}")
            print('---------------------------------------')
            

    #class method:
    @classmethod
    def change_pro(cls,new,Enter_product):
        cls.available_products[Enter_product][0]=new
                

    #Ending msg in static method:
    @staticmethod
    def end_msg():
        print("\n!!____Thanks For Shopping_____!!")

    # update generic cart details :
    @classmethod
    def cart_change(cls,added,enter_product):
        cls.available_products[enter_product][0]=added

    def welcome_start_shopping(self):
        while True:
            print("\n1. Display products Available in shop")
            print("2. Display customer details and cart details")
            print("3. Add product to cart")
            print("4. Remove product from cart")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
         #on click:
            if choice==1:
                self.display_products()

            elif choice==2:
                #Name=input("Enter your name:")
                #if Name==self.name:
                    self.customer_details()  
                #else:
                    #print("\n__Customer not found__")

            elif choice==3:
                self.display_products()
                Enter_product=input("Enter your product name:")
                if Enter_product in self.available_products:
                    Enter_quantity=int(input("Enter Quantity:"))
                    if Enter_quantity in range (self.available_products[Enter_product][0]+1):
                        if Enter_product  not in self.cart:
                            total_productprice=Enter_quantity*(self.available_products[Enter_product][1])
                            self.cart[Enter_product]=[Enter_quantity,total_productprice]
                        else:
                            life=(self.cart[Enter_product][0])+Enter_quantity
                            total=life*(self.available_products[Enter_product][1])
                            self.cart[Enter_product]=[life,total]
                        print("\n_____Product added to cart succesfully_____")
                        new=self.available_products[Enter_product][0]-Enter_quantity
                        start_shopping.change_pro(new,Enter_product)
                    else:
                        print("\n_____Stock not available______")
                else:
                    print("\n_____Product not Available_____")

            elif choice==4:
                self.customer_cart()
                enter_product=input("\nEnter product name:")
                if enter_product in self.cart:
                    enter_Quantity=int(input("Enter your quantity:"))
                    if enter_Quantity in range (self.cart[enter_product][0]+1):
                        news=self.cart[enter_product][0]-enter_Quantity
                        total_cartprice=news*(self.available_products[enter_product][1])
                        if news==0 or total_cartprice==0:
                            self.cart.pop(enter_product)
                        else:
                            self.cart[enter_product]=[news,total_cartprice]
                        added=(self.available_products[enter_product][0])+enter_Quantity
                        start_shopping.cart_change(added,enter_product)
                        print("\n_____Product Removed successfully______")
                    else:
                        print("\n___Entered Quantity is out of range___")
                else:
                    print("\n____product not available in your cart____")
                
            elif choice==5:
                #return print("\n_____Thanks For Shopping ______")
                #Thanks for shopping vist again
                return start_shopping.end_msg()
                 

#passing customer details:
s1=start_shopping('sandy',9360280482,'chennai',cart={})
s2=start_shopping('ashok',2454615215,'salem',cart={})
s1.welcome_start_shopping()
#s2.welcome_start_shopping()
