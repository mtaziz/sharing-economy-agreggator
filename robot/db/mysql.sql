DROP TABLE IF EXISTS ads;
CREATE TABLE ads (
  guid CHAR(100) PRIMARY KEY,
  title VARCHAR(251),
  description VARCHAR(300),
  url VARCHAR(300),
  media VARCHAR(251),
  location VARCHAR(100),
  postal_code MEDIUMINT(128) DEFAULT '0',
  latitude FLOAT,
  longitude FLOAT,
  price FLOAT(6) NOT NULL,
  currency VARCHAR(3),
  period VARCHAR(100),
  source VARCHAR(100),
  category CHAR(100),
  subcategory CHAR(100),
  updated DATETIME
) DEFAULT CHARSET=utf8;

