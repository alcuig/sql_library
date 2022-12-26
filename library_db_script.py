#DESCRIPTION : SQL commands to create tables in a library database for books, loans, and people making loans
#TO IMPROVE: make process scalable by transforming into Python script with psql wrapper 

create table books (
    book_id varchar(50) primary key,
    title varchar(50),
    author varchar(50),
    publisher varchar(50),
    publication_date varchar(50),
    isbn varchar(50)
);

create table patrons (
    patron_id varchar(50) primary key,
    name varchar(50),
    telephone_number varchar(50),
    email_address varchar(50),
    notes varchar(50) 
);

create table loans (
    book_id varchar(50),
    patron_id varchar(50),
    foreign key(book_id) REFERENCES library.public.books(book_id),
    foreign key (patron_id) REFERENCES library.public.patrons(patron_id),
    loan_date varchar(50),
    return_date varchar(50)
);

#write a set of SQL queries to :
#1/ insert new records

INSERT INTO library.public.books(book_id, title, author, publisher, publication_date, isbn) VALUES 
    ('000542','The cat is black','Avery Good Author','Avery Good Publisher','1952/02/01','ISBN 0001'),
    ('000642','The dog is white','The Best Author','The Best Publisher','19532/12/08','ISBN 0000');

INSERT INTO library.public.patrons(patron_id, name, telephone_number, email_address, notes) VALUES 
('P001', 'Geralt Something', '+4456789087', 'geralt.something@gmail.com', 'Forgot library card on Jan 07 2021.'),
('P002', 'Darwinia Nothing', '07467567890', 'darwinianothing@yahoo.com', 'N/A');

insert into library.public.loans(book_id, patron_id, loan_date, return_date) VALUES
('000542', 'P001', '2021/09/19', '2021/10/19'),
('000642', 'P002', '2021/09/03', '2021/10/03');


#2/ select data from the tables
SELECT book_id, loans.patron_id, name, telephone_number, return_date
FROM loans 
INNER JOIN patrons
ON loans.patron_id = patrons.patron_id; 

INSERT INTO library.public.patrons(patron_id, name, telephone_number, email_address, notes) VALUES 
('P003', 'Mike Myers', '0789654567', 'mmyers@aol.com', 'N/A');

SELECT book_id, patrons.patron_id, name, telephone_number, return_date
FROM patrons 
LEFT JOIN loans
ON loans.patron_id = patrons.patron_id; #will reveal patrons that do not have loans alongside patrons that do

#3/ update existing records
UPDATE library.public.loans
SET return_date = '2021/11/19'
WHERE book_id = '000542';

UPDATE library.public.loans
SET return_date = '2021/12/03'
WHERE patron_id = 'P002';

#4/ delete records
DELETE FROM patrons 
WHERE name = 'Mike Myers';
