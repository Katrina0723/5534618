def login(self):
    name = input('please ')
    password = input('code')
    
    for customer in self.customers:
        if customer['name'] == name and customer['password'] == password:
            print('success')
            self.current_user = customer
            return
    
    print()






