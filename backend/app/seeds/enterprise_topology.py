from sqlalchemy import text

from app.db.engine import engine


SQL = """
INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'HQ-USER-NET',
'10.1.10.0/24',
'USER',
id
FROM branches
WHERE code='HQ';

INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'HQ-SERVER-NET',
'10.1.20.0/24',
'SERVER',
id
FROM branches
WHERE code='HQ';

INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'EAST-USER-NET',
'10.2.10.0/24',
'USER',
id
FROM branches
WHERE code='BE';

INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'EAST-IOT-NET',
'10.2.20.0/24',
'IOT',
id
FROM branches
WHERE code='BE';

INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'WEST-USER-NET',
'10.3.10.0/24',
'USER',
id
FROM branches
WHERE code='BW';

INSERT INTO networks (id,name,cidr,zone,branch_id)
SELECT
gen_random_uuid(),
'WEST-DMZ-NET',
'10.3.20.0/24',
'DMZ',
id
FROM branches
WHERE code='BW';
"""


with engine.begin() as connection:
    connection.execute(text(SQL))

print("Enterprise networks inserted.")
