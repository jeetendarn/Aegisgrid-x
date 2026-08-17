from sqlalchemy import text

from app.db.engine import engine


SQL = """
INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Employee Workstation',
    'ENDPOINT',
    2,
    'active'
FROM devices
WHERE hostname LIKE '%WS-%';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Customer Portal',
    'APPLICATION',
    5,
    'active'
FROM devices
WHERE hostname='HQ-APP-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Enterprise PostgreSQL Database',
    'DATABASE',
    5,
    'active'
FROM devices
WHERE hostname='HQ-DB-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Identity Service',
    'IDENTITY',
    5,
    'active'
FROM devices
WHERE hostname='HQ-AD-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Video Surveillance Camera',
    'IOT',
    3,
    'active'
FROM devices
WHERE hostname LIKE 'EAST-CAM-%';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Environmental Sensor',
    'IOT',
    3,
    'active'
FROM devices
WHERE hostname='EAST-SENSOR-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Public Web Application',
    'WEB',
    5,
    'active'
FROM devices
WHERE hostname='WEST-WEB-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Intrusion Detection Sensor',
    'SECURITY',
    5,
    'active'
FROM devices
WHERE hostname='WEST-IDS-01';

INSERT INTO assets (id, device_id, name, asset_type, criticality, status)
SELECT
    gen_random_uuid(),
    id,
    'Remote Access Gateway',
    'VPN',
    5,
    'active'
FROM devices
WHERE hostname='WEST-VPN-01';
"""


with engine.begin() as connection:
    connection.execute(text(SQL))

print("Enterprise assets inserted.")
