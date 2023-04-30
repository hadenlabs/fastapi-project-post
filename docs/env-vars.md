<!-- Space: Projects -->
<!-- Parent: FastApiProjectPost -->
<!-- Title: EnvVars FastApiProjectPost -->
<!-- Label: FastApiProjectPost -->
<!-- Label: Project -->
<!-- Label: EnvVars -->
<!-- Include: disclaimer.md -->
<!-- Include: ac:toc -->

---

## Env Vars

### Application

| Name | Description | default | sample | Required |
| --- | --- | --- | --- | :-: |
| APPLICATION_HOST | host application | 0.0.0.0 |  | yes |
| APPLICATION_PORT | port application | 3000 |  | yes |
| ACCESS_TOKEN_EXPIRE_MINUTES | minutes expire access token | 1440 |  | yes |
| SECRET_KEY | secret key | ed296226ec6de1cfe550fb2a979b6b71a80dfdb463398fc6 |  | yes |

### Database

| Name    | Description          | default | sample | Required |
| ------- | -------------------- | ------- | ------ | :------: |
| DB_NAME | name of database     | db_name |        |   yes    |
| DB_USER | user of database     |         |        |   yes    |
| DB_PASS | password of database |         |        |   yes    |
| DB_HOST | host of database     |         |        |   yes    |
| DB_PORT | port of database     | 5432    |        |   yes    |
