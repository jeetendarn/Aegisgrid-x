from sqlalchemy import text

from app.db.engine import engine

SQL = """
INSERT INTO applications
(id, asset_id, name, application_type, environment, status)

SELECT
gen_random_uuid(),
id,
'Customer Portal',
'WEB_APPLICATION',
'production',
'active'
FROM assets
WHERE name = 'Customer Portal'

UNION ALL

SELECT
gen_random_uuid(),
id,
'Identity Management',
'IAM',
'production',
'active'
FROM assets
WHERE name = 'Identity Service'

UNION ALL

SELECT
gen_random_uuid(),
id,
'PostgreSQL Enterprise Database',
'DATABASE',
'production',
'active'
FROM assets
WHERE name = 'Enterprise PostgreSQL Database'

UNION ALL

SELECT
gen_random_uuid(),
id,
'Public Website',
'WEB_SERVER',
'production',
'active'
FROM assets
WHERE name = 'Public Web Application'

ON CONFLICT DO NOTHING;
"""

with engine.begin() as connection:
    connection.execute(text(SQL))

print("Enterprise applications inserted.")