DROP TABLE IF EXISTS ads;
CREATE TABLE ads (
  guid CHAR(100) PRIMARY KEY,
  title TEXT,
  description TEXT,
  url TEXT,
  media TEXT,
  location TEXT,
  latitude TEXT,
  longitude TEXT,
  price TEXT,
  period TEXT,
  source TEXT,
  category TEXT,
  subacategory TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;

