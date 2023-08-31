INSERT INTO clientes (nome, rua, numero_casa) VALUES
('Manoel Oliveira', 'Rua São Jorge',  '12'),
('José Andrade',    'Rua Brasil',     '23'),
('Marcos Silva',    'Rua Tiradentes', '45'),
('Maria Silva',     'Rua Tiradentes', '56'),
('Rafael Junior',   'Rua Brasil',     '67'),
('João Silva',      'Rua Tiradentes', '87');

INSERT INTO produtos (nome, peso, preco) VALUES
('pão', 500, 8.5),
('bolo', 1000, 14.35),
('bolacha', 300, 6.85);

INSERT INTO estoque (id_estoque_produto, quantidade) VALUES
(1, 50),
(2, 20),
(3, 40);

INSERT INTO pedidos (id_pedido_cliente, data_pedido, descricao) VALUES
(1, '2023-08-20', 'Lanche'),
(2, '2023-08-21', 'Café da Manhã'),
(3, '2023-08-22', 'Jantar');

INSERT INTO itens (id_item_pedido, id_item_produto, quantidade) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 2),
(2, 3, 3),
(2, 1, 2),
(3, 2, 1),
(3, 1, 2);