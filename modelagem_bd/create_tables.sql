-- Criando schema da padaria
-- drop database padaria;
create database if not exists padaria;
use padaria;

-- Criando tabela clientes
create table if not exists clientes (
	id_cliente int auto_increment primary key,
	nome varchar(50) not null,
	rua varchar(50) not null,
	numero_casa varchar(10) not null);

-- Criando tabela produtos
create table if not exists produtos (
  id_produto int auto_increment primary key,
  nome varchar(50) not null,
  peso float default 0,
  preco float default 0);

-- Criando tabela estoque
create table if not exists estoque (
  id_estoque int auto_increment primary key,
  id_estoque_produto int,
  quantidade int,
  constraint fk_estoque_produto foreign key(id_estoque_produto) references produtos(id_produto));

-- Criando tabela pedidos
create table if not exists pedidos (
  id_pedido int auto_increment primary key,
  id_pedido_cliente int,
  data_pedido date,
  descricao varchar(255),
  constraint fk_pedido_cliente foreign key(id_pedido_cliente) references clientes(id_cliente)
  on delete no action
  on update no action);

-- Criando tabela itens
create table if not exists itens (
	id_item int auto_increment primary key,
    id_item_pedido int,
    id_item_produto int,
    quantidade int,
    constraint fk_item_pedido foreign key(id_item_pedido) references pedidos(id_pedido),
    constraint fk_item_produto foreign key(id_item_produto) references produtos(id_produto));