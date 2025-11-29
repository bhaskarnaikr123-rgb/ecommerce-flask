🛒 Flask E-Commerce Website



A fully functional beginner-friendly E-Commerce Web Application built using HTML, CSS, Python Flask, and MySQL.

The project includes Login/Signup, Dynamic product categories, Search functionality, and serves as a great starter full-stack project.



🚀 Features

👤 User Features



User Signup \& Login with MySQL database



Secure data storage



Session-based login system



🛍️ E-Commerce Features



Dynamic product listing from database



Category-based filtering



Product search bar



Clean UI made with HTML \& CSS



🗄 Backend Features



Flask routes \& controllers



MySQL database connectivity



Organized project structure



Ready for deployment \& containerization



//

🧱 Tech Stack

Layer	Technology

Frontend	HTML, CSS

Backend	Python (Flask)

Database	MySQL

Deployment (Upcoming)	Render / Railway / Docker / AWS

📁 Project Structure

ecommerce-flask/

│

├── static/

│   ├── css/

│   ├── images/

│

├── templates/

│   ├── index.html

│   ├── login.html

│   ├── signup.html

│   ├── products.html

│

├── app.py

├── config.py

├── requirements.txt

├── README.md

└── .gitignore



🗄️ Database Setup (MySQL)

1️⃣ Create the database

CREATE DATABASE ecommerce;

USE ecommerce;



2️⃣ Create Users table

CREATE TABLE users (

&nbsp;   id INT AUTO\_INCREMENT PRIMARY KEY,

&nbsp;   name VARCHAR(100),

&nbsp;   email VARCHAR(100),

&nbsp;   password VARCHAR(255)

);



3️⃣ Create Products table

CREATE TABLE products (

&nbsp;   id INT AUTO\_INCREMENT PRIMARY KEY,

&nbsp;   name VARCHAR(100),

&nbsp;   price INT,

&nbsp;   category VARCHAR(50),

&nbsp;   image VARCHAR(255)

);



4️⃣ Update config.py with your own credentials

MYSQL\_HOST = "localhost"

MYSQL\_USER = "root"

MYSQL\_PASSWORD = "yourpassword"

MYSQL\_DB = "ecommerce"



▶️ Running the Project Locally

1️⃣ Install required dependencies

pip install -r requirements.txt



2️⃣ Run the Flask app

python app.py



3️⃣ Open the app

http://127.0.0.1:5000/

