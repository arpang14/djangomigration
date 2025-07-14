**Rollback All Migrations for an App**
If you want to roll back all migrations for an app (resetting it to an unmigrated state), specify zero as the migration name:


python manage.py migrate app_name zero
In Django, you can execute custom Python code during a migration by using the RunPython operation. This allows you to write Python code that runs as part of the migration process, such as data migrations or other custom logic.
