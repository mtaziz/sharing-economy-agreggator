DROP TABLE IF EXISTS ads;
CREATE TABLE ads (
  guid CHAR(32) PRIMARY KEY,
  name TEXT,
  description TEXT,
  url TEXT,
  title TEXT,
  media TEXT,
  location TEXT,
  price TEXT,
  period TEXT,
  source TEXT,
  category TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;
