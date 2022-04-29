import json
import datetime
from json.decoder import JSONDecodeError

#  ---------User registration------------

def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "password": password,
        "age": age,
        "phone number": phn,
        "order history": {}
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except json.JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

#print(register_user('user.json',"Aman",79456,22,8574129623))


# -------------Admin Registration--------------

def admin_user(admin_json, name, password):
    admin = {
        "id": 1,
        "name": name,
        "password": password
    }
    try:
        file = open(admin_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["password"] == password:
                file.close()
                return "User already Exists"
        else:
            admin["id"] = len(content) + 1
            content.append(admin)
    except json.JSONDecodeError:
        content = []
        content.append(admin)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

#print(admin_user('admin.json',"Akash",785556))


# ---------------User_order history----------------

def user_order_history(user_json, user_id):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            print("Order History")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    file.close()
    return False
#print(user_order_history('user.json',3))

# ----------------add_food----------------

def add_food(food_json,food_name,price,no_plates=1):
    food={
        'id':1,
        'name':food_name,
        "no of plates":no_plates,
        "price":price
    }
    try:
        file=open(food_json,"r+")
        content=json.load(file)
        for i in range(len(content)):
            if content[i]['name']==food_name:
                file.close()
                return 'food already exist'
        else:
            food['id']=len(content)+1
            content.append(food)
    except JSONDecodeError:
        content=[]
        content.append(food)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"
#print(add_food('food.json','Tandori Roti',25,40))

# ----------------Update_food-------------- 

def update_food(food_json,food_id,no_plates=1):
    file = open(food_json, "r+")
    content = json.load(file)
    
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no of plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success" 
#print(update_food('food.json',3,6))

# ----------------Update user profile---------------

def update_profile(user_json,user_id,name,phn):
    file = open(user_json, "r+")
    content = json.load(file)
    
    for i in range(len(content)):
        if (content[i]["id"] == user_id):
            content[i]["name"] = name
            content[i]["phone number"] = phn
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close() 
    return "Your profile has been updated successfully"
#print(update_profile('user.json',2,'Akash',652143987))

# -------------------remove_food-------------------

def remove_food(food_json, food_id):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "success"
    return "Pls Enter Valid ID"
#print(remove_food('food.json',5))

# -------------------read_food----------

def read_food(food_json):
    file=open(food_json,"r+")
    content=json.load(file)
    for i in range(len(content)):
        print("Id: ",content[i]['id'])
        print("food_name: ",content[i]['name'])
        print("no of plates: ",content[i]['no of plates'])
        print("Price: ",content[i]["price"])
    file.close()
    return True
#print(read_food('food.json'))


# ------------order_placing-------------

def user_place_order(user_json, food_json, user_id, food_name, quantity):
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    file = open(user_json, "r+")
    content = json.load(file)
    file1 = open(food_json, "r+")
    content1 = json.load(file1)
    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no of plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no of plates"]-=quantity
                        if date not in content[j]["order history"]:
                            content[j]["order history"][date] = [content1[i]["name"]]
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
            '''else:
                print("Pls Enter less quantity")
                #break    
        else:
            print("Food Not Available")
            #break'''
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    
    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()
    
    return "Order Placed"
#print(user_place_order('user.json','food.json',1,"Paneer_Tikka",1))


# ---------------Discount--------------

def discount_bill(food_json,food_id, no_plates):
    file=open(food_json,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            Bill= no_plates * content[i]["price"]
            if Bill < 200:
                discount = Bill * .20
                Bill = Bill - discount
                print("Discount:",0)
                print("Amount payable: ",Bill)
                break
                      
            if Bill >=200 or Bill <= 300:
                discount = Bill * .20
                Bill = Bill - discount
                print("Discount:",discount)
                print("Amount payable: ",Bill)
                break
                
            elif Bill >300 or Bill <=400:
                discount = Bill * .30
                Bill = Bill - discount
                print("Amount payable: ",Bill)
                break
            else:
                discount = Bill *.80
                Bill = Bill - discount
                print("Amount payable: ",Bill)
                break
            
    file.close()
    return True        
    return "Thanks for coming"
#print(discount_bill("food.json",2,2))
                
    
# -----------------Menu------------------

val = input("Do you Want to order Food Y/n: ")
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = input("Choose one value from the above: ")
    if val1 == "1":
#--------------Register----------------#
        print("1)user")
        print("2)admin")
        x=input("choose from above option: ")
        if x == "1":
            print()
            name = input("Enter the name: ")
            password = int(input("Enter the password: "))
            age = int(input("Enter your Age: "))
            phn = input("Enter the Phn number: ")
            register_user("user.json", name, password, age, phn)
        elif x=="2":
            print()
            name = input("Enter the name: ")
            password = int(input("Enter the password: "))
            admin_user("admin.json", name, password)
    elif val1 == "2":
        print()
        while True:
            print("1)user")
            print("2)Admin")
            print("3)Exit")
            val2=input("choose the value from obove Option : ")
            
            if val2 == "1":
                print("---------USER--------")
                user =input("Enter name:")
                password=int(input("Enter password:"))
                file = open('user.json', "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3=input("Choose value from above option: ")
                                if val3 == "1":
                                    read_food("food.json")
                                elif val3 == "2":
                                    user_id=int(input("Enter user id: "))
                                    name=input("Enter Food name: ")
                                    quantity=int(input("Enter quantity: "))
                                    user_place_order('user.json', 'food.json', user_id, name, quantity)
                                
                                elif val3 == "3":
                                    user_id=int(input("Enter user id: "))
                                    user_order_history('user.json', user_id)
                                
                                elif val3 =="4":
                                    x=input("Do you want to update the profile 'y/n': ")
                                    if x.lower()=="y":
                                        user_id=int(input("Enter user id:"))
                                        name=input("Enter User name to update:")
                                        phn=input("Enter mobile num. to update:")
                                        update_profile('user.json',user_id,name,phn)
                                    else:
                                        break
                                else:
                                    print("Thanks for Visit")
                                    
                        else:
                            print("Wrong Password")
                            
                    else:
                        print("Wrong Username")
                        
                        
            elif val2 =="2":
                name=input("Enter Admin name:")
                password=int(input("Enter Password:"))
                file=open('admin.json',"r+")
                content=json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == name:
                        if content[i]["password"] == password:
                            #while True:
                                print()
                                print("1) Add New Food")
                                print("2) Edit Food")
                                print("3) View Food")
                                print("4) Remove Food")
                                print("5) Bill_generation")
                                print("6) Exit")
                                
                                val3=input("choose value from above option:")
                                
                                if val3=="1":
                                    fname=input("Enter food name to add: ")
                                    no_plates=int(input("Enter number of plates to add: "))
                                    price=int(input("Enter price: "))
                                    add_food('food.json',fname,price,no_plates)
                                
                                elif val3 == "2":
                                    food_id=int(input("Enter food Id: "))
                                    no_plates=int(input("Enter no of plates to update: "))
                                    update_food('food.json',food_id,no_plates)
                                
                                elif val3 == "3":
                                    read_food("food.json")
                                
                                elif val3 == "4":
                                    food_id=int(input("Enter food_id: "))
                                    remove_food('food.json',food_id)
                                    
                                elif val3 == "5":
                                    food_id =int(input("Enter food id: "))
                                    no_plates =int(input("Enter no of plates: "))
                                    discount_bill("food.json",food_id,no_plates)
                                    
                                
                                else:
                                    print("-----'Bye', HAve a nice day------")
                                    break
                                    
                        else:
                            print("Please Enter valid Password:")
                            break
                    else:
                        print("Please Enter valid admin name:")
                        
    
                                    
    else:
        #--------------Exit--------------------#
        print("Not a Problem,Come again")
        print("Thanks to visit my Restaurant")
        
                                    
                                    
                
                