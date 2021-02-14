
 CREATE TABLE Adress(
    id INTEGER PRIMARY KEY,
    street TEXT, 
    number REAL, 
    Settlement TEXT,
    town TEXT,
    state TEXT,
    country TEXT,
);


 CREATE TABLE house(
    id INTEGER PRIMARY KEY,
    price REAL, 
    FOREIGN KEY (address_id) REFERENCES address(id),
    description TEXT, 
    amenities TEXT,
    size REAL,
    first_picture BLOB,
);
