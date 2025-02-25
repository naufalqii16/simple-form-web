CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    student_id VARCHAR(100) UNIQUE NOT NULL,
    subject VARCHAR(100) NOT NULL,
    major VARCHAR(100) NOT NULL
);

INSERT INTO attendance (name, student_id, subject, major) 
VALUES ('John Doe', '123456', 'Math', 'Computer Science'),
    ('Alice Johnson', '112233', 'Math', 'Mathematics'),
    ('Bob Brown', '223344', 'Physics', 'Physics'),
    ('Charlie Davis', '334455', 'Chemistry', 'Chemistry'),
    ('Diana Evans', '445566', 'Biology', 'Biology');