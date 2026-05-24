# Sistema de Oficina Mecânica - Cadastro de Mecânicos (Entrega - Versão Completa)

Projeto Spring Boot 3 + Java 17 que implementa uma API REST para gerenciar mecânicos.
Inclui: CRUD, validação, filtro por nome, paginação, tratamento de exceções e H2 in-memory.

## Requisitos
- Java 17+
- Maven
- IDE (IntelliJ / VSCode)

## Como rodar
1. Abra o projeto na sua IDE (ou terminal).
2. Rodar com Maven:
   - `mvn clean package`
   - `mvn spring-boot:run`
   OU
   - `java -jar target/oficina-0.0.1-SNAPSHOT.jar`

3. Endpoints base: `http://localhost:8080/api/mecanicos`

## H2 Console
- URL: `http://localhost:8080/h2-console`
- JDBC URL: `jdbc:h2:mem:oficina`
- User: `sa`
- Password: (vazio)

## Exemplos (curl)
- Criar:
  ```bash
  curl -X POST http://localhost:8080/api/mecanicos \
   -H "Content-Type: application/json" \
   -d '{"nome":"João Silva","email":"joao@example.com","especialidade":"Freios"}'
  ```
- Listar (paginado):
  ```bash
  curl "http://localhost:8080/api/mecanicos?page=0&size=10"
  ```
- Filtrar por nome:
  ```bash
  curl "http://localhost:8080/api/mecanicos?nome=joao"
  ```
- Atualizar:
  ```bash
  curl -X PUT http://localhost:8080/api/mecanicos/1 \
   -H "Content-Type: application/json" \
   -d '{"nome":"João S.","email":"joao.novo@example.com","especialidade":"Motor"}'
  ```
- Excluir:
  ```bash
  curl -X DELETE http://localhost:8080/api/mecanicos/1
  ```

## Observações
- Email é único (validado em nível de serviço e com constraint na tabela).
- Validações retornam 400 com mensagens de campo.
- Melhorias sugeridas: testes unitários, Swagger/OpenAPI, tratamento de concorrência para unique constraint.