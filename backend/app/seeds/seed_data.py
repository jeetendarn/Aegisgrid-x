from sqlalchemy import text

from app.db.engine import engine


SEED_SQL = """
INSERT INTO branches (id,name,code,location)
VALUES
(gen_random_uuid(),'Headquarters','HQ','Bengaluru'),
(gen_random_uuid(),'Branch East','BE','Chennai'),
(gen_random_uuid(),'Branch West','BW','Mumbai')
ON CONFLICT DO NOTHING;

INSERT INTO roles (id,name,description)
VALUES
(gen_random_uuid(),'Administrator','Full access'),
(gen_random_uuid(),'SOC Analyst','Security analyst'),
(gen_random_uuid(),'Network Engineer','Network operations')
ON CONFLICT DO NOTHING;

INSERT INTO permissions (id,name,resource,action,description)
VALUES
(gen_random_uuid(),'user.read','user','read','Read users'),
(gen_random_uuid(),'user.write','user','write','Modify users'),
(gen_random_uuid(),'device.read','device','read','Read devices'),
(gen_random_uuid(),'incident.read','incident','read','Read incidents')
ON CONFLICT DO NOTHING;
"""


with engine.begin() as connection:
    connection.execute(text(SEED_SQL))

print("Seed data inserted.")
