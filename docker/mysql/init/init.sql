CREATE TABLE IF NOT EXISTS 'logs' (
    'id' INT(11) NOT NULL AUTO_INCREMENT,
    'user_id' INT(11) NOT NULL,
    'date' DATE NOT NULL,
    'reporting' TIME NOT NULL,
    'leaving' TIME NOT NULL,
    PRIMARY KEY ('id')
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS 'cluster' (
    'id' INT(11) NOT NULL AUTO_INCREMENT,
    'date' DATE NOT NULL,
    'reporting' BOOLEAN NOT NULL,
    'average' float NOT NULL,
    'sd' float NOT NULL,
    PRIMARY KEY ('id')
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
