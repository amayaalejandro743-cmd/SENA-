-- 1. RETO 1: Consulta SELECT con JOINs (Modelo OLTP)
SELECT 
    cl.ciudad,
    cat.nombre_categoria,
    SUM(vd.cantidad * p.precio) AS total_ingresos
FROM ventas_detalle vd
INNER JOIN ventas_cabecera vc ON vd.id_venta = vc.id_venta
INNER JOIN clientes cl ON vc.id_cliente = cl.id_cliente
INNER JOIN productos p ON vd.id_producto = p.id_producto
INNER JOIN categorias cat ON p.id_categoria = cat.id_categoria
GROUP BY cl.ciudad, cat.nombre_categoria;


-- 2. RETO 2: Creacion de tablas del modelo OLAP (Esquema Estrella)
CREATE TABLE dim_clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(50),
    ciudad VARCHAR(50)
);

CREATE TABLE dim_productos (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(50),
    nombre_categoria VARCHAR(50),
    precio DECIMAL(10,2)
);

CREATE TABLE fact_ventas (
    id_detalle INT PRIMARY KEY,
    id_venta INT,
    id_cliente INT,
    id_producto INT,
    fecha DATE,
    cantidad INT,
    ingreso_total DECIMAL(12,2),
    FOREIGN KEY (id_cliente) REFERENCES dim_clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES dim_productos(id_producto)
);


-- 3. RETO 3: Migracion de datos (ETL con INSERT INTO ... SELECT)
INSERT INTO dim_clientes (id_cliente, nombre, ciudad)
SELECT id_cliente, nombre, ciudad 
FROM clientes;

INSERT INTO dim_productos (id_producto, nombre_producto, nombre_categoria, precio)
SELECT p.id_producto, p.nombre_producto, c.nombre_categoria, p.precio
FROM productos p
INNER JOIN categorias c ON p.id_categoria = c.id_categoria;

INSERT INTO fact_ventas (id_detalle, id_venta, id_cliente, id_producto, fecha, cantidad, ingreso_total)
SELECT 
    vd.id_detalle,
    vd.id_venta,
    vc.id_cliente,
    vd.id_producto,
    vc.fecha,
    vd.cantidad,
    (vd.cantidad * p.precio)
FROM ventas_detalle vd
INNER JOIN ventas_cabecera vc ON vd.id_venta = vc.id_venta
INNER JOIN productos p ON vd.id_producto = p.id_producto;


-- 4. Explicacion de ventajas del nuevo modelo
/*

La ventaja principal de pasar al modelo OLAP (estrella) es que todo queda mas directo y rapido para sacar reportes. 

En el modelo original (OLTP) tocaba unir las 5 tablas con 4 JOINs y poner a la base de datos a multiplicar cantidad por precio fila por fila cada vez que se hacia la consulta. Si hubiera 10 millones de ventas al dia, hacer esa consulta pondria super lento el servidor y bloquearia las cajas registradoras.

En cambio, en el nuevo modelo OLAP unimos productos con categorias en una sola tabla (dim_productos) y en la tabla de hechos (fact_ventas) ya dejamos guardado el resultado de la multiplicacion (ingreso_total). Asi el motor hace menos cruces de tablas, solo tiene que sumar esa columna y no afecta el trabajo de las cajas registradoras.
*/
