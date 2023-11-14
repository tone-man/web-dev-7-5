INSERT INTO Books (title) VALUES 
("Owen's Toes"),
("Danny of Dublin"),
("Antonio in America"),
("Derek Drive to Dorado"),
("Bree's Flying Lessons"),
("Web Development Basics"),
("How to Teach"),
("Tips to Success - Two Crew");

INSERT INTO Genre (genre) VALUES
("Fiction"),
("Non-Fiction"),
("Business"),
("History"),
("Flight"),
("Computer Science"),
("Travel");

INSERT INTO Author (author) VALUES
("Owen"),
("Danny"),
("Antonio"),
("Derek"),
("Bree"),
("Stuetzle"),
("Kissel");

INSERT INTO BooksGenreMapping (book_id, genre_id) VALUES 
(1,1),
(2,1),
(3,2),
(4,2),
(5,1),
(6,2),
(7,2),
(8,2);

INSERT INTO BooksAuthorMapping (book_id, author_id) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,6),
(7,7),
(8,5),
(8,3);
