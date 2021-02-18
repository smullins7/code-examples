DROP TABLE IF EXISTS comments;

CREATE TABLE comments (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       post_id INTEGER NOT NULL,
                       created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                       content TEXT NOT NULL
);



INSERT INTO comments (post_id, content) VALUES (3, 'an anonymous comment');
INSERT INTO comments (post_id, content) VALUES (3, 'yet another comment');
