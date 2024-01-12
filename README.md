#   Gerenciamento de cursos e aulas de uma escola de modalidade EAD

A linguagem utilizada foi Python e o framework Django, juntamente com o Django Rest Framework;  
A API foi criada utilizando o Banco de Dados Postgres

| Método HTTP | Caminho                                   | Responsabilidade                               | Permissão                                                               |
|-------------|-------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------|
| POST        | /api/accounts/                            | Criação de usuário                             | Livre                                                                   |
| POST        | /api/login/                               | Login do usuário                               | Livre                                                                   |
| POST        | /api/courses/                             | Criação de cursos                              | Somente super usuários                                                  |
| GET         | /api/courses/                             | Listagem de cursos                             | Somente usuários autenticados                                           |
| GET         | /api/courses/<course_id>/                 | Busca de curso por id                          | Acesso livre à administradores. Estudantes não podem acessar cursos que não participam |
| PATCH       | /api/courses/<course_id>/                 | Atualização somente dos dados de curso         | Somente super usuários                                                  |
| DELETE      | /api/courses/<course_id>/                 | Deleção de curso                               | Somente super usuários                                                  |
| POST        | /api/courses/<course_id>/contents/        | Criação de conteúdos e associação ao curso    | Somente super usuários                                                  |
| GET         | /api/courses/<course_id>/contents/<content_id>/ | Busca de conteúdo por id               | Super usuários têm acesso livre. Estudantes só podem acessar dos que participam |
| PATCH       | /api/courses/<course_id>/contents/<content_id>/| Atualização somente do conteúdo          | Somente super usuários                                                  |
| DELETE      | /api/courses/<course_id>/contents/<content_id>/| Deleção de conteúdos                    | Somente super usuários                                                  |
| PUT         | /api/courses/<course_id>/students/        | Adição de alunos ao curso                      | Somente super usuários                                                  |
| GET         | /api/courses/<course_id>/students/        | Listagem dos estudantes do curso               | Somente super usuários                                                  |
| GET         | /api/docs/                                | Visualização da documentação no formato Swagger ou Redoc | Acesso livre                                                     |

## Configuração do Ambiente Virtual (Opcional, mas recomendado)
### Crie um ambiente virtual
```
    python -m venv venv
```

### Ative o ambiente virtual
#### No Windows
```
    venv\Scripts\activate
```
#### No Linux/Mac
```
    source venv/bin/activate
```


## Instalar o Django:
```
    pip install django
```

## Instalação das Dependencias
```
    pip install -r requirements.txt
```


## Configuração do banco de dados:
1. Crie um banco de dados PostgreSQL.
2. Copie o arquivo .env.example para .env e configure as variáveis de ambiente relacionadas ao banco de dados.

## Migrações e Aplicações
### Execute as migrações
```
    python manage.py makemigrations
```
```
    python manage.py migrate
```

### Inicie o servidor de desenvolvimento
```
    python manage.py runserver
```




## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install model_bakery pytest-testdox pytest-django
```


## Execução dos testes:

Para rodar a bateria de todos os testes, utilize:
```shell
pytest --testdox -vvs
```
---

Caso você tenha interesse em rodar apenas um diretório de testes específico, utilize os comandos abaixo:

Accounts:
```python
pytest --testdox -vvs tests/accounts/
```

Contents:
```python
pytest --testdox -vvs tests/contents/
```

Courses:
```python
pytest --testdox -vvs tests/courses/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/accounts/tests_views.py::TestLoginAccountView::test_login_without_required_fields
```
