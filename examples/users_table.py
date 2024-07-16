from pg_table_builder import Table, Column, Serial, Varchar, Text

Table(
    "users",
    Column("id", Serial(primary_key=True, not_null=True)),
    Column("username", Varchar(limit_size=10, not_null=True)),
    Column("description", Text(default_expression="'It''s your description'"))
)
