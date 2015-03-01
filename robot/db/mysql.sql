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
  price_unit TEXT,
  period TEXT,
  source TEXT,
  category TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;

