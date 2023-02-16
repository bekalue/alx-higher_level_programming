-- converts hbtn_0c_0 database, first_name table and name field to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
UPDATE first_table CONVERT name TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
