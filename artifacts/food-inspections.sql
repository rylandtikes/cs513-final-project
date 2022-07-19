create table food_inspections
(
    inspection_id   INTEGER not null
        primary key
        unique,
    dba_name        TEXT,
    aka_name        TEXT,
    license_number  INTEGER,
    facility_type   TEXT,
    risk            TEXT,
    address         TEXT,
    city            TEXT,
    state           STRING,
    zip             INTEGER,
    inspection_date DATE,
    inspection_type TEXT,
    results         TEXT,
    violations      TEXT,
    latitude        NUMERIC,
    longitude       NUMERIC,
    location        TEXT
);