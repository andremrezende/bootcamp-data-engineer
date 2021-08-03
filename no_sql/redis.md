# Redis (Chave-Valor)
Utilizado sandbox https://try.redis.io/

## Comandos
* Criar valor para user1:
```
set user1:name "Bob Esponja"
```

* Obter valor
```
GET user1:name
```

* Adicionar valor para user:
```
SET user '{"name": "Patrick", "age": 31}'
```

* Obter novo valor inserido:
```
GET user
```

* Informar para expirar em segundos um registro:
```
set user2:name "Lula molusco" ex 10
```

* Informar para expirar em milisegundos um registro:
```
set user2:name "Fake" px 10
```

* Verificar se o registro existe:
```
EXISTS user1:name
```

* Inserir valor do tipo lista
```
LPUSH user1:hobbies 'Caçar agua viva'
```

* Acessar o dados do valor do tipo lista:
```
LINDEX user1:hobbies 0
```

* Acessar todos os valores do tipo lista:
```
LRANGE user1:hobbies 0 1
```

* Indentificar o tipo de chave:
```
TYPE user1:name

TYPE user1:hobbies
```

* Tempo de expiração:
```
TTL user1:name
```

* Remover o TTL de um valor:
```
SET user1:name "Fake" EX 30

TTL user1:name

PERSIST user1:name

TTL user1:name
```

* Remover uma chave:
```
DEL user1:name
```