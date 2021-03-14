class Router1:
    def db_for_read(self, model, **hints):
        return 'mysql'

    def db_for_write(self, model, **hints):
        return 'default'
