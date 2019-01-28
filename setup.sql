-- Describe TEST_SUITE
CREATE TABLE "test_suite" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "state" BLOB NOT NULL,
    "config" INTEGER,
    "setup" INTEGER,
    "test" TEXT
);


-- Describe TEST_CASE
CREATE TABLE "test_case" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "type" INTEGER NOT NULL,
    "state" INTEGER NOT NULL,
    "url" TEXT,
    "method" INTEGER,
    "headers" TEXT,
    "variables" TEXT,
    "date" TEXT,
    "extract" TEXT,
    "output" TEXT
);

-- Describe TEST_DATA
CREATE TABLE "test_data" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "case_id" INTEGER,
    "type" INTEGER,
    "key" TEXT,
    "value" TEXT,
    "assert" TEXT
);



