from sqlalchemy import text

from app.db.engine import engine


SQL = """
INSERT INTO devices
(id, network_id, hostname, device_type, operating_system, status)

SELECT
gen_random_uuid(),
id,
'HQ-WS-01',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='HQ-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'HQ-WS-02',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='HQ-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'HQ-WS-03',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='HQ-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'HQ-APP-01',
'APPLICATION_SERVER',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='HQ-SERVER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'HQ-DB-01',
'DATABASE_SERVER',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='HQ-SERVER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'HQ-AD-01',
'IDENTITY_SERVER',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='HQ-SERVER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-WS-01',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='EAST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-WS-02',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='EAST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-WS-03',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='EAST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-CAM-01',
'IP_CAMERA',
'Embedded Linux',
'active'
FROM networks
WHERE name='EAST-IOT-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-CAM-02',
'IP_CAMERA',
'Embedded Linux',
'active'
FROM networks
WHERE name='EAST-IOT-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'EAST-SENSOR-01',
'IOT_SENSOR',
'Embedded Linux',
'active'
FROM networks
WHERE name='EAST-IOT-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-WS-01',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='WEST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-WS-02',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='WEST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-WS-03',
'WORKSTATION',
'Ubuntu 26.04',
'active'
FROM networks
WHERE name='WEST-USER-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-WEB-01',
'WEB_SERVER',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='WEST-DMZ-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-IDS-01',
'IDS_SENSOR',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='WEST-DMZ-NET';

INSERT INTO devices
SELECT
gen_random_uuid(),
id,
'WEST-VPN-01',
'VPN_GATEWAY',
'Ubuntu Server 26.04',
'active'
FROM networks
WHERE name='WEST-DMZ-NET';
"""


with engine.begin() as connection:
    connection.execute(text(SQL))

print("Enterprise devices inserted.")
