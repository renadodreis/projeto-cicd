# Projeto Flask com CI/CD via GitHub Actions e Docker

Este projeto consiste em uma aplicação web simples feita com Flask, que utiliza um pipeline CI/CD completo com GitHub Actions, Docker e deploy automatizado para um servidor de produção.

## 🖥️ Aplicação

A aplicação Flask é simples e tem como objetivo demonstrar a automação completa desde testes, build, até deploy:

- **Framework:** Flask
- **Docker:** Imagem multi-arquitetura (amd64, arm64)
- **Deploy:** Automático via SSH e Docker Compose

## 🛠️ Estrutura do Projeto

```
flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
└── docker-compose.yml (no servidor remoto)
```

## 🔄 Arquitetura Simplificada (Pipeline CI/CD)

```
Git Push (main)
    │
    ├─── GitHub Actions Workflow
    │        ├── Build e Testes
    │        ├── Gera Artefato (ZIP)
    │        └── Cria Release no GitHub
    │
    ├─── Docker Build & Push
    │        └── Publica Imagem no GitHub Container Registry (GHCR)
    │
    └─── Deploy via SSH
             ├── Conecta no servidor remoto
             ├── Pull imagem Docker do GHCR
             └── Atualiza aplicação com Docker Compose
```

## 🚀 Pipeline CI/CD

O pipeline está configurado no GitHub Actions e possui as seguintes etapas:

- **Build e Testes:**
  - Configura ambiente Python.
  - Instala dependências.
  - Executa testes unitários com Pytest.
  - Gera e publica artefato (ZIP) no GitHub.

- **Docker Build e Push:**
  - Constrói imagem Docker compatível com múltiplas arquiteturas.
  - Publica a imagem no GitHub Container Registry.

- **Deploy em Produção:**
  - Atualiza automaticamente a aplicação no servidor remoto via SSH usando Docker Compose.

- **Notificação:**
  - Envia automaticamente um e-mail caso ocorra qualquer falha no pipeline.

## ⚙️ Workflow CI/CD

Veja o workflow completo em [`.github/workflows/ci-cd.yml`](./.github/workflows/ci-cd.yml)

## 🚦 Requisitos para Configuração

Para utilizar corretamente o pipeline, configure os seguintes secrets no GitHub:

| Secret               | Descrição                                 |
|----------------------|-------------------------------------------|
| `GHCR_PAT`           | Token GitHub para GitHub Container Registry|
| `SSH_HOST`           | Host/IP do servidor remoto                 |
| `SSH_USER`           | Usuário SSH do servidor remoto             |
| `SSH_PRIVATE_KEY`    | Chave SSH privada para acesso ao servidor  |
| `EMAIL_USERNAME`     | Usuário SMTP para notificações por e-mail  |
| `EMAIL_PASSWORD`     | Senha SMTP para notificações por e-mail    |

## 📌 Comandos úteis no servidor remoto

Para verificar logs da aplicação Docker no servidor remoto:

```bash
docker logs -f flask-app
```

Para acessar o container diretamente no servidor remoto:

```bash
docker exec -it flask-app sh
```

## 🌐 Endereço da Aplicação

- [https://cicd.renatodreis.com.br](https://cicd.renatodreis.com.br)

## 📝 Autor

- Renato Dreis - [renato@renatodreis.com.br](mailto:renato@renatodreis.com.br)

---

Esse documento oferece uma visão geral simples e direta, com informações essenciais para utilizar e compreender o funcionamento da aplicação e do pipeline CI/CD implementado.
