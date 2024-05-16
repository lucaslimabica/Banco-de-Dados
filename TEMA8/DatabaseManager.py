import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(f"{database_name}.db")
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """Cria uma nova tabela no banco de dados."""
        query = f"CREATE TABLE {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, columns, data):
        """Insere dados em uma tabela existente."""
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({data})"
        self.cursor.execute(query)
        self.conn.commit()

    def select_data(self, table_name, columns):
        """Seleciona dados de uma tabela existente."""
        query = f"SELECT {columns} FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, set_column, set_data, where_column, where_data):
        """Atualiza dados em uma tabela existente."""
        query = f"UPDATE {table_name} SET {set_column} = {set_data} WHERE {where_column} = {where_data}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, where_column, where_data):
        """Deleta dados de uma tabela existente."""
        query = f"DELETE FROM {table_name} WHERE {where_column} = {where_data}"
        self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        """Fecha a conexão com o banco de dados quando a instância da classe é destruída."""
        self.conn.close()
