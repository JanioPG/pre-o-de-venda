from itertools import product
from decouple import config
from productsDB import ConnectDB
import mariadb


def request_from_user(text:str):
    while True:
        try:
            data = str(input(f"{text} ")).strip()
            if len(data) == 0:
                raise "length = 0"
            else:
                return data
        except:
            print("Error: empty information")
            

def get_user_data():
    # code
    code = request_from_user('Code: ')
    # name
    name = request_from_user('Name: ')
    # batch
    batch = request_from_user('Batch: ')
    # total_cost
    total_cost = request_from_user('Total cost: R$').replace(",", ".")
    # profit percentage
    profit = request_from_user('Profit percentage [%]:').replace(",", ".")
    sale_price = float(total_cost) / (1 - (float(profit)/100))
    return code, name, batch, round(float(total_cost), 2), round(float(profit), 2), round(sale_price, 2)


def insert(cur):
    try:
        query_sql = "INSERT INTO Products (code, name, batch, total_cost, profit_percentage, sale_price) VALUES (?, ?, ?, ?, ?, ?)"

        data = get_user_data()
        cur.execute(query_sql, (data[0], data[1], data[2], data[3], data[4], data[5]))

        return "Product registered successfully."

            
    except mariadb.Error as e: 
        return f"Error: {e}"


def query(cur, code: str = "", all = False):
    if all:
        cur.execute("SELECT * FROM Products")
    else:
        cur.execute("SELECT * FROM Products WHERE code=?", (code,))
    

    rows = cur.fetchall()

    return rows


def update(cur, id):
    try:
        cur.execute("SELECT * FROM Products WHERE id=?", (id,))
        product = cur.fetchall()
        print("Enter 0 to not update the field:")
        
        columns = get_user_data()
        code, name, batch, total_cost, profit_percentage, sale_price = columns
        to_update = {}
        # needed to update also sale_price
        if total_cost != float(0) or profit_percentage != float(0):
            if total_cost == float(0):
                total_cost = product[0][4]
            if profit_percentage == float(0):
                profit_percentage = product[0][5]
            sale_price = round(float(total_cost) / (1 - (float(profit_percentage)/100)), 2)

        else:
            pass

        # check fields to update
        for key, value in {"code": code, "name": name, "batch": batch, "total_cost": total_cost, "profit_percentage": profit_percentage, "sale_price": sale_price}.items():
            if value != float(0) and value != '0':
               to_update[key] = value
        
        combination = []
        for k in to_update.keys():
            combination.append(f"{k}=?")
        to_update_text = ", ".join(combination)

        # add ID to appear in tuple.
        to_update["id"] = id
        query_sql = f"UPDATE Products set {to_update_text} WHERE id=?"
        print(tuple(to_update.values()))
        cur.execute(query_sql, tuple(to_update.values()))
        
        return query_sql
        
    except:
        return "Error: Failed to update."
    

def delete(cur, id):
    try:
        cur.execute("DELETE FROM Products WHERE id=?", (id,))
        return True

    except:
        return False


def checker(cur, id):
    cur.execute("SELECT * FROM Products WHERE id=?", (id,))
    rows = cur.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def operation(option: str):
    try:
        myDB = ConnectDB(config("USERDB"),
                config("PASSWORD"),
                config("HOST"),
                config("PORT", cast=int),
                config("DB"))
        
        conn = myDB.make_connection()
        if conn:
            result = None
            # Get cursor
            cur = conn.cursor()

            if option == '1':
                result = insert(cur)
                
            elif option == '2':
                # see all products
                result = query(cur, all=True)
            elif option == '3':
                # see one product
                code = request_from_user('Code: ')
                result = query(cur, code)
            elif option == '4':
                # update
                id = request_from_user('Product ID: ')
                result = update(cur, id)                
            else:
                # delete a product record
                id = request_from_user('Product ID: ')
                check = checker(cur, id)
                if check:
                    command_delete = delete(cur, id)
                    
                    if command_delete:
                        result = f"Product ID {id} successfully deleted."
                    else:
                        result = "Error: Failed to delete the product."
                else:
                    return f"Product with ID {id} is not in the records."

            conn.commit()
            conn.close()
            cur.close()

            return result

    except mariadb.Error as e: 
        return f"Error: {e}"
