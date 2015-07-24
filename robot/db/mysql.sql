DROP TABLE IF EXISTS ads;
CREATE TABLE ads (
  guid CHAR(100) PRIMARY KEY,
  title VARCHAR(251),
  description TEXT,
  url TEXT,
  media TEXT,
  location TEXT,
  latitude TEXT,
  longitude TEXT,
  price TEXT,
  currency TEXT,
  period TEXT,
  source TEXT,
  category TEXT,
  subcategory TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;

