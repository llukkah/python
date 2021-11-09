Relational Databases

CREATE
	Create a table:
	  	CREATE TABLE instructors (
		     id SERIAL PRIMARY KEY NOT NULL,
		     name TEXT NOT NULL,
		     experience INT NOT NULL,
		     website VARCHAR(50)
		     );
		
		Insert Data into a table:
			INSERT INTO students VALUES (DEFAULT, 'Jack Sparrow', 28, '50 Main St, New York, NY');

READ - SYNTAX - SELECT column1, column2, column3 FROM table_name;
			* - will return the whole table
		
		EX: SELECT * FROM students
			-- select every column from the students table
		EX: SELECT name, age FROM students;
			-- specify to return only name and age
		EX: SELECT name FROM students WHERE age < 100;
			-- specify name of students who’s age is <= 100
		EX: SELECT name, age FROM students ORDER BY age;
		EX: SELECT name, age FROM students ORDER BY age DESC;
			-- DESC - descending ASC - ascending
		EX: SELECT * FROM students WHERE address LIKE '%Fivetowns%';
			-- specify to return address who only lives in specific city
		EX: SELECT * FROM students WHERE address LIKE ‘%Fivetowns%’ OR address LIKE ‘%soho%’;

            JOIN - To select information on two or more tables at once. 
				This will produce rows that contain information from both tables.
				When joining two or more tables, we have to tell the database how to match up the rows. 		(e.g. to make sure the author information is correct for each book).
			ON - This is done using the ON clause, which specifies which properties to match.
			LIMIT - limit the amount of queries to return.

			EX: SELECT * FROM artists
			EX: JOIN tracks ON tracks.artist_id = artists.id
			EX: LIMIT 3;

			EX: SELECT artists.name, tracks.name FROM artists
			EX: JOIN tracks ON tracks.artist_id = artists.id
			EX: WHERE artists.name LIKE 'Beyonc%';


    UPDATE - best to update via ID, if not get as specific as possible
		UPDATE students SET address = '100 Main St., New York, NY' WHERE address = 'asdfasdfasdf';
	
	DELETE
		DELETE FROM students WHERE name = 'Miss Take';


Foreign Keys - instruct the database to ensure that the relationships between tables are valid, and that new records cannot be inserted that break these constraints. 
	In other words, the referential integrity of our data is maintained.
	By using the REFERENCES keyword, foreign key constraints can be added to the schema.
	says this will reference this specific table and column
		CREATE TABLE tracks(
		  name VARCHAR(255),
		  artist_id VARCHAR(255) REFERENCES artists(id),
		  album_id VARCHAR(255) REFERENCES albums(id),
		  disc_number INTEGER,
		  popularity INTEGER,
		  id VARCHAR(255) PRIMARY KEY
		);




MULTI-JOINS - JOIN statements can also be linked together to query data across several tables.

		SELECT albums.name
		FROM albums
		JOIN tracks ON tracks.album_id = albums.id
		JOIN artist ON tracks.artist_id = artists.id
		WHERE artists.name LIKE 'Beyonc%';

		output: 		name
		--------------------------------------
		I AM...SASHA FIERCE THE BONUS TRACKS
		Dangerously In Love
		BEYONCÉ [Platinum Edition]
		BEYONCÉ [Platinum Edition]
		I AM...SASHA FIERCE



Join tables > Many-to-Many Relations
	Join Tables - a table that is specifically and only used to join two other tables and create a many-to-many relationship typically consist of at minimum, two foreign keys and possibly other metadata. 
	
	CREATE TABLE spotify_users(		  
		id SERIAL PRIMARY KEY,		  
		name VARCHAR(255)		
		);
	CREATE TABLE likes(
		  user_id SERIAL REFERENCES spotify_users(id),
		  track_id VARCHAR(255) REFERENCES tracks(id)
		);

	AS - used to give more descriptive names to the values returned by join clauses.														        																SELECT artists.name AS artist_name, tracks.name AS track_name
		FROM artists
		JOIN tracks ON artists.id = tracks.artist_id
		WHERE artists.name LIKE 'Beyonc%';
