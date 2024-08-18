# Relatório do Servidor Web Simples
## Objetivo

Servidor web em Python para servir arquivos estáticos e retornar erro 404 para arquivos inexistentes.
Cabeçalhos HTTP

    Requisição: Host, User-Agent, Accept
    Resposta: Content-Type, Content-Length, Connection

## Tipos de Solicitação

    GET: Para obter arquivos (ex: GET /index.html HTTP/1.1).

## Códigos de Status

    200 OK: Recurso encontrado.
    404 Not Found: Recurso não encontrado.

## Observações

    Serviu HTML e imagens corretamente.
    Retornou erro 404 quando o arquivo não foi encontrado.
    Usou Connection: close para encerrar conexões.
