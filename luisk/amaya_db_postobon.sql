USE db_postobon;


-- Ejercicio 1: Cree la tabla empleados con sus restricciones
CREATE TABLE empleados (
    id INT AUTO_INCREMENT,
    sede_id INT NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(12, 2) NOT NULL,
    fecha_ingreso DATE,
    CONSTRAINT pk_empleados PRIMARY KEY (id),
    CONSTRAINT fk_empleados_sedes FOREIGN KEY (sede_id) REFERENCES sedes(id),
    CONSTRAINT chk_empleados_salario CHECK (salario > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Ejercicio 2: Crear índice para búsquedas por cargo y mostrar definición de la tabla
CREATE INDEX idx_empleados_cargo ON empleados(cargo);
SHOW CREATE TABLE empleados;




-- Ejercicio 3: Cargue en empleados los 22 registros
INSERT INTO empleados (sede_id, nombre, cargo, salario, fecha_ingreso) VALUES
(1, 'Carlos Pinto', 'Jefe de sede', 5200000.00, '2018-03-12'),
(1, 'Marta Gómez', 'Operario de planta', 2100000.00, '2021-07-05'),
(1, 'Luis Brito', 'Conductor', 2400000.00, '2022-01-17'),
(1, 'Ana Redondo', 'Auxiliar administrativo', 1900000.00, '2023-02-20'),
(2, 'Jorge Iguarán', 'Jefe de sede', 5000000.00, '2017-09-01'),
(2, 'Elena Epieyú', 'Operario de planta', 2050000.00, '2022-05-09'),
(2, 'Pedro Uriana', 'Vendedor', 2300000.00, '2023-08-14'),
(4, 'Sofía Valdés', 'Jefe de sede', 5600000.00, '2016-11-22'),
(4, 'Camilo Barrios', 'Supervisor', 3400000.00, '2019-04-15'),
(4, 'Laura Mendoza', 'Analista de calidad', 3800000.00, '2020-10-03'),
(4, 'Andrés Pacheco', 'Operario de planta', 2150000.00, '2024-01-08'),
(5, 'Diana Rojas', 'Jefe de sede', 6100000.00, '2015-06-30'),
(5, 'Felipe Cárdenas', 'Supervisor', 3600000.00, '2018-12-10'),
(5, 'Natalia Soto', 'Vendedor', 2500000.00, '2023-03-27'),
(6, 'Ricardo Zapata', 'Jefe de sede', 5800000.00, '2016-02-18'),
(6, 'Paula Giraldo', 'Analista de calidad', 4000000.00, '2021-09-13'),
(6, 'Mateo Osorio', 'Conductor', 2450000.00, '2024-06-01'),
(7, 'Valentina Ríos', 'Supervisor', 3500000.00, '2020-01-27'),
(8, 'Héctor Cubillos', 'Jefe de sede', 5400000.00, '2017-05-16'),
(8, 'Isabel Moreno', 'Operario de planta', 2200000.00, '2022-11-21'),
(8, 'Julián Torres', 'Conductor', 2350000.00, '2023-10-02'),
(8, 'Camila Vargas', 'Auxiliar administrativo', 1950000.00, '2025-02-10');

-- Ejercicio 4: Registre los 3 empleados adicionales en una sola sentencia y compruebe total
INSERT INTO empleados (sede_id, nombre, cargo, salario, fecha_ingreso) VALUES
(2, 'Rosa Fince', 'Operario de planta', 2100000.00, '2025-03-03'),
(5, 'Tomás Herrera', 'Conductor', 2400000.00, '2025-04-21'),
(8, 'Gloria Páez', 'Vendedor', 2550000.00, '2025-05-12');

SELECT COUNT(*) AS total_empleados FROM empleados;



-- Ejercicio 5: Registre los 4 departamentos nuevos en este orden
INSERT INTO departamento (nombre) VALUES
('Antioquia'),
('Valle del Cauca'),
('Cundinamarca'),
('Santander');

-- Ejercicio 6: Registre las 4 sedes nuevas averiguando el id del departamento
INSERT INTO sedes (id_departamento, nombre) VALUES
((SELECT id FROM departamento WHERE nombre = 'Antioquia'), 'Itagüí'),
((SELECT id FROM departamento WHERE nombre = 'Antioquia'), 'Bello'),
((SELECT id FROM departamento WHERE nombre = 'Valle del Cauca'), 'Palmira'),
(NULL, 'Sede Móvil');

-- Ejercicio 7: Cambiar nombre de sedes de prueba y reubicar sedes mal clasificadas
UPDATE sedes SET nombre = 'Acacías' WHERE nombre = 'dos';
UPDATE sedes SET nombre = 'Granada' WHERE nombre = 'tres';
UPDATE sedes SET nombre = 'Puerto López' WHERE nombre = 'cuatro';
UPDATE sedes SET nombre = 'Cumaral' WHERE nombre = 'cinco';
UPDATE sedes SET nombre = 'Restrepo' WHERE nombre = 'seis';
UPDATE sedes SET nombre = 'San Martín' WHERE nombre = 'siete';
UPDATE sedes SET nombre = 'Puerto Gaitán' WHERE nombre = 'ocho';
UPDATE sedes SET nombre = 'Mesetas' WHERE nombre = 'nueve';
UPDATE sedes SET nombre = 'La Macarena' WHERE nombre = 'diez';

UPDATE sedes 
SET id_departamento = (SELECT id FROM departamento WHERE nombre = 'Cundinamarca') 
WHERE nombre = 'Bogota';

UPDATE sedes 
SET id_departamento = (SELECT id FROM departamento WHERE nombre = 'Antioquia') 
WHERE nombre = 'Medellin';

UPDATE sedes 
SET id_departamento = (SELECT id FROM departamento WHERE nombre = 'Valle del Cauca') 
WHERE nombre = 'Cali';

UPDATE sedes 
SET id_departamento = (SELECT id FROM departamento WHERE nombre = 'Guajira') 
WHERE nombre = 'San Juan';



-- Ejercicio 8: Total de sedes y total de empleados
SELECT 
    (SELECT COUNT(*) FROM sedes) AS total_sedes,
    (SELECT COUNT(*) FROM empleados) AS total_empleados;

-- Ejercicio 9: Salario más alto (mayor), más bajo (menor) y promedio redondeado a 2 decimales (promedio)
SELECT 
    MAX(salario) AS mayor,
    MIN(salario) AS menor,
    ROUND(AVG(salario), 2) AS promedio
FROM empleados;

-- Ejercicio 10: Nómina total de la empresa
SELECT SUM(salario) AS nomina_total 
FROM empleados;

-- Ejercicio 11: Fecha de ingreso más reciente
SELECT MAX(fecha_ingreso) AS ingreso_mas_reciente 
FROM empleados;





-- Ejercicio 12: Cada empleado con el nombre de su sede (nombre, cargo, sede)
SELECT 
    e.nombre AS nombre,
    e.cargo AS cargo,
    s.nombre AS sede
FROM empleados e
INNER JOIN sedes s ON e.sede_id = s.id;

-- Ejercicio 13: Cada empleado con su sede y departamento (nombre, cargo, sede, departamento)
SELECT 
    e.nombre AS nombre,
    e.cargo AS cargo,
    s.nombre AS sede,
    d.nombre AS departamento
FROM empleados e
INNER JOIN sedes s ON e.sede_id = s.id
INNER JOIN departamento d ON s.id_departamento = d.id;

-- Ejercicio 14: Todas las sedes con sus empleados, ordenadas por id de sede
SELECT 
    s.nombre AS sede,
    e.nombre AS empleado
FROM sedes s
LEFT JOIN empleados e ON s.id = e.sede_id
ORDER BY s.id;

-- Ejercicio 15: Todos los departamentos con sus sedes (incluye departamentos sin sedes)
SELECT 
    d.nombre AS departamento,
    s.nombre AS sede
FROM departamento d
LEFT JOIN sedes s ON d.id = s.id_departamento;

-- Ejercicio 16: Mismo resultado del ejercicio 14 pero listando primero empleados y luego sedes
SELECT 
    s.nombre AS sede,
    e.nombre AS empleado
FROM empleados e
RIGHT JOIN sedes s ON e.sede_id = s.id
ORDER BY s.id;

-- Ejercicio 17: Sedes que no tienen ningún empleado (id, sede)
SELECT 
    s.id AS id,
    s.nombre AS sede
FROM sedes s
LEFT JOIN empleados e ON s.id = e.sede_id
WHERE e.id IS NULL;


-- Agrupar y resumir

-- Ejercicio 18: Sedes por departamento, incluyendo los que tienen cero sedes (departamento, total_sedes)
SELECT 
    d.nombre AS departamento,
    COUNT(s.id) AS total_sedes
FROM departamento d
LEFT JOIN sedes s ON d.id = s.id_departamento
GROUP BY d.id, d.nombre;

-- Ejercicio 19: Cuánto suma la nómina de cada sede (sede, nomina)
SELECT 
    s.nombre AS sede,
    SUM(e.salario) AS nomina
FROM sedes s
INNER JOIN empleados e ON s.id = e.sede_id
GROUP BY s.id, s.nombre;

-- Ejercicio 20: Salario más alto de cada departamento (departamento, salario_maximo)
SELECT 
    d.nombre AS departamento,
    MAX(e.salario) AS salario_maximo
FROM departamento d
INNER JOIN sedes s ON d.id = s.id_departamento
INNER JOIN empleados e ON s.id = e.sede_id
GROUP BY d.id, d.nombre;


-- Filtrar y ordenar

-- Ejercicio 21: Empleados que ganan más de 3.000.000 ordenados de mayor a menor salario
SELECT 
    nombre,
    cargo,
    salario
FROM empleados
WHERE salario > 3000000
ORDER BY salario DESC;

-- Ejercicio 22: Departamentos que tienen más de 2 sedes (departamento, total_sedes)
SELECT 
    d.nombre AS departamento,
    COUNT(s.id) AS total_sedes
FROM departamento d
INNER JOIN sedes s ON d.id = s.id_departamento
GROUP BY d.id, d.nombre
HAVING COUNT(s.id) > 2;

-- Ejercicio 23: Sedes con nómina superior a 12.000.000 ordenadas de mayor a menor (sede, nomina)
SELECT 
    s.nombre AS sede,
    SUM(e.salario) AS nomina
FROM sedes s
INNER JOIN empleados e ON s.id = e.sede_id
GROUP BY s.id, s.nombre
HAVING SUM(e.salario) > 12000000
ORDER BY nomina DESC;


-- Reto final

-- Ejercicio 24: Resumen de departamentos para ingresos desde 2022-01-01 y nómina > 8.000.000
SELECT 
    d.nombre AS departamento,
    COUNT(DISTINCT s.id) AS sedes_con_personal,
    COUNT(e.id) AS empleados,
    SUM(e.salario) AS nomina
FROM departamento d
INNER JOIN sedes s ON d.id = s.id_departamento
INNER JOIN empleados e ON s.id = e.sede_id
WHERE e.fecha_ingreso >= '2022-01-01'
GROUP BY d.id, d.nombre
HAVING SUM(e.salario) > 8000000
ORDER BY nomina DESC;