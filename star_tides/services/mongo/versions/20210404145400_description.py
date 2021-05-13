''' Mongodb migration. May not be used.
'''
# pragma pylint: disable=invalid-name
from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.test_collection.save({"new_column": "value"})

    def downgrade(self):
        self.db.drop_collection()
