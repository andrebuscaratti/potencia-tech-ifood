use padaria;

-- Quais pedidos foram feitos? (recuperação simples com SELECT)
select *
from pedidos;

-- Quais clientes moram na rua Tiradentes? (filtro com WHERE)
select *
from clientes
where rua = 'Rua Tiradentes';

-- Qual o preço por kg dos produtos? (expressão atributo derivado)
select nome, round(1000 / peso * preco, 2) as preco_kg
from produtos;

-- Quais ruas tem mais de 1 cliente? (agrupamento, condição, ordenação)
select rua, count(nome) as clientes
from clientes
group by rua
having clientes > 1
order by clientes desc;

-- Qual a quantidade em estoque de cada produto? (junção)
select p.nome, e.quantidade
from produtos p
inner join estoque e
on p.id_produto = e.id_estoque_produto;

-- Qual o valor total dos itens do pedido de José Andrade em 21/08/2023?
select round(sum(pro.preco), 2) as preco
from pedidos pe
inner join clientes c
on pe.id_pedido_cliente = c.id_cliente
inner join itens i
on pe.id_pedido = i.id_item_pedido
inner join produtos pro
on i.id_item_produto = pro.id_produto
where c.nome = 'José Andrade' and pe.data_pedido = '2023-08-21';