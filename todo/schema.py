instructions = [               # indicamos las instrucciones en lenguaje sql
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
    CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(200) NOT NULL
        )
    """,   # con las triple comilla doble indicamos que todo ese comando va en una sola linea
    """
    CREATE TABLE todo (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        );
    """
]
