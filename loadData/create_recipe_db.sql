DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ingredient_list;
DROP TABLE IF EXISTS recipe_nutrition;
DROP TABLE IF EXISTS ingredient_information;

CREATE TABLE recipes(
recipe_key			INT				PRIMARY KEY		AUTO_INCREMENT,
url					VARCHAR(80)		NOT NULL,
title 				VARCHAR(80)		NOT NULL,
serving_size 		DECIMAL(5, 2)		NOT NULL,
category			VARCHAR(45)		NOT NULL,
total_time_minutes 	INT		NOT NULL
);

CREATE TABLE users(
user_key		INT				PRIMARY KEY		AUTO_INCREMENT,
recipe_key	INT		NOT NULL,
CONSTRAINT fk_recipe_key_users FOREIGN KEY (recipe_key) 
	REFERENCES recipes (recipe_key), 
vegetarian 		BOOL		NOT NULL,
vegan 	    	BOOL		NOT NULL,
gluten_free 	BOOL		NOT NULL,
dairy_free 	    BOOL		NOT NULL
);

CREATE TABLE ingredient_information(
ingredient_key		INT	 PRIMARY KEY		AUTO_INCREMENT,
ingredient_name 	VARCHAR(80)			NOT NULL,
category 	    	VARCHAR(80)			NOT NULL,
price 	   			DECIMAL(5, 2)		NOT NULL
);

CREATE TABLE ingredient_list(
list_key		INT		PRIMARY KEY		AUTO_INCREMENT,
recipe_key		INT		NOT NULL,
ingredient_key	INT		NOT NULL,
CONSTRAINT fk_recipe_key_ingredient_list FOREIGN KEY (recipe_key) 
	REFERENCES recipes (recipe_key), 
CONSTRAINT fk_ingredient_key_ingredient_list FOREIGN KEY (ingredient_key) 
	REFERENCES ingredient_information (ingredient_key),
amount  		DECIMAL(6, 2)   NOT NULL,
unit  	    	VARCHAR(20)		NOT NULL
);

CREATE TABLE recipe_nutrition(
recipe_nutrition_key	INT	 	PRIMARY KEY		AUTO_INCREMENT,
recipe_key				INT		NOT NULL,
CONSTRAINT fk_recipe_key_recipe_nutrition FOREIGN KEY (recipe_key) 
	REFERENCES recipes (recipe_key), 
fats 			DECIMAL(5, 2)	    NOT NULL,
saturated_fats 	DECIMAL(5, 2)		NOT NULL,
protein 		DECIMAL(5, 2)		NOT NULL,
cholesterol 	DECIMAL(5, 2)		NOT NULL,
sugar 	    	DECIMAL(5, 2)		NOT NULL,
sodium 			DECIMAL(5, 2)		NOT NULL
);

