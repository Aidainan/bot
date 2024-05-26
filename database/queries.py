CREAT_REVIEW_TABLE='''
CREATE TABLE IF NOT EXISTS reviews (
id INTEGER PRIMARY KEY,
tg_id INTEGER,
firstname VARCHAR(255),
text TEXT)'''

INSERT_REVIEW='''
INSERT INTO reviews VALUES (?,?, ?, ?)'''

CREATE_CATEGORY_TABLE='''
CREATE TABLE IF NOT EXISTS categories (
id INTEGER PRIMARY KEY,
name VARCHAR(255),
UNIQUE(name))'''

CREATE_FOOD_TABLE='''
CREATE TABLE IF NOT EXISTS foods (
id INTEGER PRIMARY KEY,
namee VARCHAR(255),
price INTEGER,
photo TEXT,
category_id INTEGER,
FOREIGN KEY(category_id) REFERENCES categories(id),
UNIQUE(namee))'''

INSERT_CATEGORIES = """
INSERT OR IGNORE INTO categories (name) VALUES('food'),('drinks'),('salad')
"""

INSERT_FOOD = """INSERT OR IGNORE INTO foods (namee, price, photo,category_id) VALUES ('lagman',100,'media/images/kkk.jpg', 1),('cola', 12,'media/images/kkk.jpg', 2),('olivia',250, 'media/images/kkk.jpg', 3)"""

SELECT_FOOD='''
SELECT * FROM foods 
INNER JOIN categories ON foods.category_id=categories.id
WHERE categories.name=?'''