import carts_api, categories_api, products_api

while True:
    print ('Добро пожаловать на наш могозин')
    categories = categories_api.get_all_categories()
    formatted_categorits = '|' .join(categories_api.get_all_categories())
    print (f"Наши каатегори: {formatted_categorits}")
    print ('#'*30)
    
    print ('выберите действие:')
    print ('1. Получить продукты выбранной категории.')
    print ('2. Получить список всех товаров.')
    print ('3. Получить список всех корзин.')
    print ('4. Выход')

    choice = input('Выберити дейсивме: ')
    
    if choice == '1':
        categories_name = input('Введите категорию: ')
        products = categories_api.get_products_of_category(categories_name)
        
        for product in products:
               print(f'{product["id"]}. {product["title"]} Price: {product["price"]}')   
    elif choice == '2':
        products = products_api.get_all_products()
        
        if products:
            for product in products:
                print(f'{product["id"]}. {product["title"]} Prise: {product["price"]}')
        else:
            print ('Не удолосы получиты список всех товаров!')
    elif choice == '3':
        carts = carts_api.get_all_carts()
        
        if carts:
            for cart in carts:
                print (f'{cart["id"]}. {cart["date"]} {cart["products"]}')
        else:
             print ('Не удолосы получиты список всех корзин!')         
    elif choice == '4':
        print ('Желаем вам удачи)')
        break
    print("------------------------------------")
    print("------------------------------------")
    print("------------------------------------")
