# Introdução ao Cassandra (Colunar)

## Comandos
**Site para sandbox do Cassandra:**
https://katacoda.com/datastax/courses/cassandra-try-it-out/try-cql

* Criar uma nova KeySpace (DB):
```
create keyspace fenda_biquini with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
```

* Utilizar a KeySpace criada anteriormente:
```
use fenda_biquini;
```

* Criar uma nova ColumnFamily (Table):
```
create columnfamily clients (name TEXT PRIMARY KEY, age int);
```

* Verificar valores:
```
select * from clients;
```

* Inserir um novo valor na columnfamily:
```
insert into clients (name, age) values('teste', 10);
```

* Inserir um novo valor na ColumnFamily como JSON:
```
insert into clients JSON '{"name": "Patolino"}';
```

* Listar valor age com respectivo data da alteração:
```
select age, writetime(age) from clients;
```

* Filtrando valores:
```
select * from clients where name = 'teste';
```

* Filtrando valores e exibindo como JSON:
```
select JSON * from clients where name = 'teste';
```

* Adicionar um novo tipo a ColumnFamily:
```
alter columnfamily clients add hobby text;
```

* Alterar valor hobby apartir de um filtro:
```
update clients set hobby = 'basketball' where name = 'Patolino';
```

* Verificar data de alteração dos valores do comando acima:
```
select age, writetime(age), hobby, writetime(hobby) from clients where name = 'Patolino';
```