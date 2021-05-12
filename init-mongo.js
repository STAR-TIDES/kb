db.auth('root', 'rootpassword')

db = db.getSiblingDB('star_tides')

db.createUser({
  user: 'evan',
  pwd: 'password',
  roles: [
    {
      role: 'root',
      db: 'admin',
    },
  ],
});