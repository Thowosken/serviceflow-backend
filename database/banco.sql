CREATE TABLE perfis (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    perfil_id INT REFERENCES perfis(id),
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE servicos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    cliente_id INT REFERENCES clientes(id),
    categoria_id INT REFERENCES categorias(id),
    criado_por INT REFERENCES usuarios(id),
    tecnico_id INT REFERENCES usuarios(id),
    prioridade VARCHAR(20),
    status VARCHAR(20) DEFAULT 'ABERTO',
    data_abertura DATE DEFAULT CURRENT_DATE
);

CREATE TABLE observacoes (
    id SERIAL PRIMARY KEY,
    servico_id INT REFERENCES servicos(id),
    usuario_id INT REFERENCES usuarios(id),
    texto TEXT,
    data_registro DATE DEFAULT CURRENT_DATE
);

INSERT INTO perfis (nome) VALUES ('Admin'), ('Atendente'), ('Tecnico');

INSERT INTO usuarios (perfil_id, nome, email, senha) VALUES 
(1, 'Admin', 'admin@email.com', '123456'),
(1, 'Eduardo', 'eduardo@email.com', '123456'),
(1, 'Matheus', 'matheus@email.com', '123456'),
(2, 'Gabi', 'gabi@email.com', '123456'),
(3, 'Vitor', 'vitor@email.com', '123456');

INSERT INTO clientes (nome, email, telefone) VALUES 
('Empresa A', 'contato@empresa.com', '71999999999');

INSERT INTO categorias (nome) VALUES ('Hardware'), ('Rede'), ('Software');

INSERT INTO servicos (titulo, descricao, cliente_id, categoria_id, criado_por, tecnico_id, prioridade, status) VALUES 
('Trocar Roteador', 'Roteador queimou', 1, 2, 4, 5, 'Alta', 'EM ANDAMENTO');