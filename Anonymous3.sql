DROP SCHEMA IF EXISTS restaurant_chain;
CREATE SCHEMA restaurant_chain;

USE restaurant_chain;

CREATE TABLE restaurant(Location_of_Restaurant varchar(20) PRIMARY KEY,
                        Name_of_Restaurant varchar(20) NOT NULL,
                        number_of_tables int NOT NULL,
                        pre_booking int NOT NULL,
                        on_spot_reservation int NOT NULL,
                        advertising int NOT NULL,
                        salaries int NOT NULL,
                        furniture int NOT NULL,
                        raw_materials int NOT NULL
                       );

CREATE TABLE food_items(item_number int PRIMARY KEY,
                        Descript varchar(100),
                        rating int,
                        price float NOT NULL
                       );

CREATE TABLE employee(employee_id int PRIMARY KEY,
                      profession varchar(20) NOT NULL REFERENCES Profession.Profession,
                      restaurant_location varchar(20) NOT NULL REFERENCES restaurant.Location_of_Restaurant,
                      Employee_name varchar(20) NOT NULL,
                      Restaurant_name varchar(20) NOT NULL,
                      PF_amount float,
                      Month_of_joining int,
                      Year_of_joining int,
                      Date_of_joining int
                     );

CREATE TABLE Ordered_items(Order_id int REFERENCES Orders.Order_number,
                           Ordered_item_number int REFERENCES food_items.item_number,
                           CONSTRAINT pk_Order_item PRIMARY KEY(Order_id, Ordered_item_number),
                           Number_of_Items int
                          );

CREATE TABLE Orders(Order_number int PRIMARY KEY,
                    Order_time timestamp,
                    Order_status char NOT NULL,
                    Order_amount int NOT NULL,
                    Order_type char NOT NULL,
                    restaurant_location varchar(20) REFERENCES restaurant.Location_of_Restaurant,
                    Customer_ID int REFERENCES Customer.Phone_number
                   );

CREATE TABLE Profession(Profession varchar(20) PRIMARY KEY,
                        Salary int NOT NULL,
                        Employee_Working_Hours int NOT NULL,
                        PF_Percentage int
                       );

CREATE TABLE Customer(Phone_number int PRIMARY KEY,
                      user_name varchar(20),
                      Email varchar(30) UNIQUE,
                      Amount_Recieved bool,
                      Name varchar(20),
                      Order_number int REFERENCES Orders.Order_number
                     );

CREATE TABLE Online_delivery(Delivery_id varchar(20) PRIMARY KEY,
                             Location varchar(20) REFERENCES restaurant.Location_of_Restaurant,
                             Order_number int REFERENCES Orders.Order_number,
                             Customer_Id int REFERENCES Customer.Phone_number
                            );

CREATE TABLE Educational_Qualification(Employee_id int REFERENCES employee.employee_id,
                                       Educational_qualification varchar(20) NOT NULL,
                                       PRIMARY KEY(Employee_id, Educational_qualification)
                                      );
CREATE TABLE Tables(location varchar(20) REFERENCES restaurant.Location_of_Restaurant,
                    Table_no int NOT NULL,
                    number_of_seats int NOT NULL,
                    Cost_Of_Table int NOT NULL,
                    CONSTRAINT pk_table PRIMARY KEY(location, Table_no)
                   );

CREATE TABLE delivery_apps(Delivery_Id int REFERENCES Online_delivery.Delivery_id,
                           Name_of_DeliveryApp VARCHAR(20) NOT NULL
                          );


CREATE TABLE menu(location varchar(20) REFERENCES restaurant.Location_of_Restaurant,
                  item_num int NOT NULL, 
                  CONSTRAINT PK_menu PRIMARY KEY (location,item_num)
                 );


CREATE TABLE tablesbooked(phone_num int REFERENCES Customer.Phone_number,
                          table_num int NOT NULL,
                          CONSTRAINT PK_tablesbooked PRIMARY KEY (phone_num,table_num)
                         );
CREATE TABLE ingredients(item_num int REFERENCES food_items.item_number,
                         ingredient varchar(30) NOT NULL,
                         CONSTRAINT PK_ingredients PRIMARY KEY (item_num,ingredient)
                        );
                        
LOCK TABLES restaurant WRITE;

INSERT INTO restaurant VALUES ("Hyderabad", "BlueStar", 100, 10000, 900000, 10000, 100000, 50000, 10000);
INSERT INTO restaurant VALUES ("Mumbai", "CoffeeShop", 110, 11000, 910000, 11000, 110000, 51000, 11000);
INSERT INTO restaurant VALUES ("Delhi", "GrandInn", 120, 12000, 920000, 12000, 120000, 50000, 12000);
INSERT INTO restaurant VALUES ("Chennai", "BlueStar", 130, 13000, 930000, 13000, 130000, 53000, 13000);

UNLOCK TABLES;

LOCK TABLES food_items WRITE;

INSERT INTO food_items VALUES (1, "Biryani", 3, 150.15);
INSERT INTO food_items VALUES (2, "Kheema Masala", 2, 160);
INSERT INTO food_items VALUES (3, "Mushroom Pasta", 3, 100);
INSERT INTO food_items VALUES (4, "Vegetable Salad", 5, 1000);
INSERT INTO food_items VALUES (5, "Pigeon Curry", 0, 10);
INSERT INTO food_items VALUES (6, "My head", 5, 100000);

UNLOCK TABLES;

LOCK TABLES employee WRITE;

INSERT INTO employee VALUES (1, "Manager", "Hyderabad", "Gokul", "BlueStar", 12000, 12, 12, 12);
INSERT INTO employee VALUES (2, "Manager", "Hyderabad", "Srija", "BlueStar", 12000, 1, 01, 23);
INSERT INTO employee VALUES (3, "Waiter", "Hyderabad", "Anamika", "BlueStar", 0, 1, 02, 1);
INSERT INTO employee VALUES (4, "Waiter", "Hyderabad", "Kalyan", "BlueStar", 0, 11, 21, 21);
INSERT INTO employee VALUES (5, "Waiter", "Hyderabad", "Anand", "BlueStar", 0, 10, 12, 12);
INSERT INTO employee VALUES (6, "Receptionist", "Hyderabad", "Idiot", "BlueStar", 1200, 1, 2, 2);
INSERT INTO employee VALUES (7, "Cleaner", "Hyderabad", "Ghost", "BlueStar", 0, 12, 12, 12);
INSERT INTO employee VALUES (8, "Cleaner", "Hyderabad", "Kanchana", "BlueStar", 0, 12, 12, 12);
INSERT INTO employee VALUES (9, "Chef", "Hyderabad", "Conjuring", "BlueStar", 12000, 12, 12, 12);
INSERT INTO employee VALUES (10, "Chef", "Hyderabad", "Anabelle", "BlueStar", 12000, 1, 12, 12);

INSERT INTO employee VALUES (11, "Manager", "Mumbai", "Gokul", "CoffeeShop", 12000, 12, 12, 12);
INSERT INTO employee VALUES (12, "Manager", "Mumbai", "Srija", "CoffeeShop", 12000, 1, 01, 23);
INSERT INTO employee VALUES (13, "Waiter", "Mumbai", "Anamika", "CoffeeShop", 0, 1, 02, 1);
INSERT INTO employee VALUES (14, "Waiter", "Mumbai", "Kalyan", "CoffeeShop", 0, 11, 21, 21);
INSERT INTO employee VALUES (15, "Waiter", "Mumbai", "Anand", "CoffeeShop", 0, 10, 12, 12);
INSERT INTO employee VALUES (16, "Receptionist", "Mumbai", "Idiot", "CoffeeShop", 1200, 1, 2, 2);
INSERT INTO employee VALUES (17, "Cleaner", "Mumbai", "Ghost", "CoffeeShop", 0, 12, 12, 12);
INSERT INTO employee VALUES (18, "Cleaner", "Mumbai", "Kanchana", "CoffeeShop", 0, 12, 12, 12);
INSERT INTO employee VALUES (19, "Chef", "Mumbai", "Conjuring", "CoffeeShop", 12000, 12, 12, 12);
INSERT INTO employee VALUES (20, "Chef", "Mumbai", "Anabelle", "CoffeeShop", 12000, 1, 12, 12);

INSERT INTO employee VALUES (21, "Manager", "Delhi", "Gokul", "GrandInn", 12000, 12, 12, 12);
INSERT INTO employee VALUES (22, "Manager", "Delhi", "Srija", "GrandInn", 12000, 1, 01, 23);
INSERT INTO employee VALUES (23, "Waiter", "Delhi", "Anamika", "GrandInn", 0, 1, 02, 1);
INSERT INTO employee VALUES (24, "Waiter", "Delhi", "Kalyan", "GrandInn", 0, 11, 21, 21);
INSERT INTO employee VALUES (25, "Waiter", "Delhi", "Anand", "GrandInn", 0, 10, 12, 12);
INSERT INTO employee VALUES (26, "Receptionist", "Delhi", "Idiot", "GrandInn", 1200, 1, 2, 2);
INSERT INTO employee VALUES (27, "Cleaner", "Delhi", "Ghost", "GrandInn", 0, 12, 12, 12);
INSERT INTO employee VALUES (28, "Cleaner", "Delhi", "Kanchana", "GrandInn", 0, 12, 12, 12);
INSERT INTO employee VALUES (29, "Chef", "Delhi", "Conjuring", "GrandInn", 12000, 12, 12, 12);
INSERT INTO employee VALUES (30, "Chef", "Delhi", "Anabelle", "GrandInn", 12000, 1, 12, 12);

INSERT INTO employee VALUES (31, "Manager", "Banglore", "Gokul", "BlueStar", 12000, 12, 12, 12);
INSERT INTO employee VALUES (32, "Manager", "Banglore", "Srija", "BlueStar", 12000, 1, 01, 23);
INSERT INTO employee VALUES (33, "Waiter", "Banglore", "Anamika", "BlueStar", 0, 1, 02, 1);
INSERT INTO employee VALUES (34, "Waiter", "Banglore", "Kalyan", "BlueStar", 0, 11, 21, 21);
INSERT INTO employee VALUES (35, "Waiter", "Banglore", "Anand", "BlueStar", 0, 10, 12, 12);
INSERT INTO employee VALUES (36, "Receptionist", "Banglore", "Idiot", "BlueStar", 1200, 1, 2, 2);
INSERT INTO employee VALUES (37, "Cleaner", "Banglore", "Ghost", "BlueStar", 0, 12, 12, 12);
INSERT INTO employee VALUES (38, "Cleaner", "Banglore", "Kanchana", "BlueStar", 0, 12, 12, 12);
INSERT INTO employee VALUES (39, "Chef", "Banglore", "Conjuring", "BlueStar", 12000, 12, 12, 12);
INSERT INTO employee VALUES (40, "Chef", "Banglore", "Anabelle", "BlueStar", 12000, 1, 12, 12);

UNLOCK TABLES;

LOCK TABLES Customer WRITE;

INSERT INTO Customer VALUES (100, "Police", "police@gmail.com", TRUE, "Police", NULL);
INSERT INTO Customer VALUES (108, "Ambulance", "ambulance@gmail.com", TRUE, "Ambulance", NULL);
INSERT INTO Customer VALUES (104, "Fire", "fire@gmail.com", FALSE, "Fire", 3);
INSERT INTO Customer VALUES (110, "Postal", "postal@gmail.com", FALSE, "Postal", NULL);
INSERT INTO Customer VALUES (101, "lies", "lies@gmail.com", TRUE, "lies", NULL);

UNLOCK TABLES;

LOCK TABLES Profession WRITE;

INSERT INTO Profession VALUES ("Manager", 120000, 14, 12);
INSERT INTO Profession VALUES ("Waiter", 12000, 14, 0);
INSERT INTO Profession VALUES ("Cleaner", 1200, 6, 0);
INSERT INTO Profession VALUES ("Chef", 120000, 14, 12);

UNLOCK TABLES;

LOCK TABLES Ordered_items WRITE;

INSERT INTO Ordered_items VALUES (1, 2, 5);
INSERT INTO Ordered_items VALUES (1, 3, 5);
INSERT INTO Ordered_items VALUES (2, 4, 5);
INSERT INTO Ordered_items VALUES (3, 3, 1);
INSERT INTO Ordered_items VALUES (4, 5, 1);

UNLOCK TABLES;

LOCK TABLES Orders WRITE;

INSERT INTO Orders(Order_number, Order_status, Order_amount, Order_type, restaurant_location, Customer_ID) VALUES (1, "D", 1300, "F", "Hyderabad", 100);
INSERT INTO Orders(Order_number, Order_status, Order_amount, Order_type, restaurant_location, Customer_ID) VALUES (2, "P", 1300, "N", "Hyderabad", 108);
INSERT INTO Orders(Order_number, Order_status, Order_amount, Order_type, restaurant_location, Customer_ID) VALUES (3, "D", 1300, "F", "Hyderabad", 104);
INSERT INTO Orders(Order_number, Order_status, Order_amount, Order_type, restaurant_location, Customer_ID) VALUES (4, "P", 1300, "F", "Hyderabad", 110);

UNLOCK TABLES;

LOCK TABLES Online_delivery WRITE;

INSERT INTO Online_delivery VALUES (1, "Hyderabad", 2, 108);

UNLOCK TABLES;

LOCK TABLES Educational_Qualification WRITE;

INSERT INTO Educational_Qualification VALUES (1, "MBA");
INSERT INTO Educational_Qualification VALUES (2, "MBA");
INSERT INTO Educational_Qualification VALUES (11, "MBA");
INSERT INTO Educational_Qualification VALUES (12, "MBA");
INSERT INTO Educational_Qualification VALUES (21, "MBA");
INSERT INTO Educational_Qualification VALUES (22, "MBA");
INSERT INTO Educational_Qualification VALUES (31, "MBA");
INSERT INTO Educational_Qualification VALUES (32, "MBA");

UNLOCK TABLES;

LOCK TABLES Tables WRITE;

INSERT INTO Tables VALUES ("Hyderabad", 2, 4, 150);
INSERT INTO Tables VALUES ("Hyderabad", 1, 6, 100);
INSERT INTO Tables VALUES ("Hyderabad", 3, 6, 200);
INSERT INTO Tables VALUES ("Hyderabad", 4, 5, 30);
INSERT INTO Tables VALUES ("Hyderabad", 5, 2, 50);

UNLOCK TABLES;

LOCK TABLES delivery_apps WRITE;

INSERT INTO delivery_apps VALUES (1,"Swiggy");

UNLOCK TABLES;

LOCK TABLES menu WRITE;

INSERT INTO menu VALUES ("Hyderabad", 1);
INSERT INTO menu VALUES ("Hyderabad", 2);
INSERT INTO menu VALUES ("Hyderabad", 3);
INSERT INTO menu VALUES ("Hyderabad", 4);
INSERT INTO menu VALUES ("Hyderabad", 5);

UNLOCK TABLES;

LOCK TABLES tablesbooked WRITE;

INSERT INTO tablesbooked VALUES (100, 1);
INSERT INTO tablesbooked VALUES (104, 4);
INSERT INTO tablesbooked VALUES (110, 3);

UNLOCK TABLES;

LOCK TABLES ingredients WRITE;

INSERT INTO ingredients VALUES (1, "Chicken");
INSERT INTO ingredients VALUES (1, "Rice");
INSERT INTO ingredients VALUES (2, "Masala");
INSERT INTO ingredients VALUES (4, "Pigeon");
INSERT INTO ingredients VALUES (5, "My brain");
INSERT INTO ingredients VALUES (3, "Something");

UNLOCK TABLES;
