# ProjetoCompanhiaDeVoo-Docker-sql-flask-python-aplicação de gerenciamento de voos

Bem-vindo ao nosso projeto de aviação!

Este projeto tem como objetivo criar uma plataforma completa e intuitiva para a gestão de voos e aeroportos. A aplicação permite aos usuários visualizar e agendar voos, gerenciar aeroportos e destinos, bem como acompanhar o desempenho financeiro da empresa.

## Requisitos
Docker
Docker Compose
Instalação


## Para instalar o projeto, siga os seguintes passos:

Clone o repositório do Github

Acesse o diretório do projeto

Construa as imagens Docker usando o comando:


docker-compose build

Inicie os containers usando o comando:


docker-compose up

Configure o banco de dados executando os scripts SQL necessários.

Inicie a aplicação web usando o arquivo "app.py".

Teste a aplicação para garantir que todas as rotas e endpoints estejam funcionando corretamente.
Uso

Uma vez instalado, acesse a aplicação através de um navegador na seguinte URL:

http://localhost:5000

A partir daí, você poderá visualizar e agendar voos, gerenciar aeroportos e destinos, bem como acompanhar o desempenho financeiro da empresa.

Contribuição

# Funcionalidades

x------------------------------------------------------------x

| Número | Serviço            | Descrição                        |

x------------------------------------------------------------x

| 1      | Efetuar login      | Permite efetuar e recuperar a chave de sessão utilizada para validação em cada solicitação |

| 2      | Efetuar Logout     | Permite encerrar sessão atual                                                        |

| 3      | Validar sessão     | Permite verificar se sessão atual não expirou e se pode ser acessada pelo IP que está tentando efetuar o acesso |

| 4      | Retornar aeroportos | Retoma a lista dos aeroportos oferecidos pela companhia aérea                     |

| 5      | Retornar aeroportos por origem | Retoma a lista dos aeroportos de destino de acordo com o aeroporto de origem informado |

| 6      | Retornar voos      | Retoma a lista dos voos oferecidos pela companhia aérea para a data informada       |

| 7      | Pesquisar voos     | Efetua a pesquisa de voos e retorna uma lista de voos com a menor tarifa disponível no momento para o número de passageiros informados|

| 8      | Efetuar compra     | Efetua a reserva e a compra dos voos e tarifas selecionados e retorna o localizador da reserva e o números dos e-tickets |


x------------------------------------------------------------x


# Como funciona

Este conjunto de arquivos representa uma aplicação de gerenciamento de voos. O arquivo docker-compose.yml define dois serviços: db (banco de dados PostgreSQL) e web (aplicação Flask). O arquivo Dockerfile descreve como construir a imagem da aplicação Flask a partir da imagem Python e inclui informações sobre dependências, variáveis de ambiente, portas e comandos para iniciar a aplicação. O arquivo Dockerfile-db descreve como construir a imagem do banco de dados a partir da imagem PostgreSQL e inclui informações sobre variáveis de ambiente e portas. O arquivo requirements.txt lista as dependências da aplicação Flask e o arquivo init.sql contém scripts SQL para inicializar as tabelas do banco de dados com dados de exemplo.
