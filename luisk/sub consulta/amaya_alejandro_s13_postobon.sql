USE db_postobon;


-- Ejercicio 1: Salarios sobre el promedio general

SELECT
id,
nombre,
sede_id,
salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados)
ORDER BY salario DESC, id ASC;


-- Ejercicio 2: Empleados de Guajira
SELECT
id,
nombre,
sede_id
FROM empleados
WHERE sede_id IN (
SELECT id
FROM sedes
WHERE id_departamento = 1
)
ORDER BY id ASC;

-- Ejercicio 3: Sedes sin empleados

-
SELECT
s.id AS sede_id,
s.nombre AS sede
FROM sedes s
WHERE NOT EXISTS (
SELECT 1
FROM empleados e
WHERE e.sede_id = s.id
)
ORDER BY sede_id ASC;


-- Ejercicio 4: Salarios sobre el promedio de su sede

SELECT
e1.id,
e1.nombre,
e1.sede_id,
e1.salario,
ROUND((SELECT AVG(salario) FROM empleados e2 WHERE e2.sede_id = e1.sede_id), 2) AS promedio_sede
FROM empleados e1
WHERE e1.salario > (
SELECT AVG(salario)
FROM empleados e3
WHERE e3.sede_id = e1.sede_id
)
ORDER BY e1.sede_id ASC, e1.id ASC;

-- Ejercicio 5: Nómina sobre el promedio de las sedes

SELECT
sede_id,
nomina
FROM (
SELECT sede_id, SUM(salario) AS nomina
FROM empleados
GROUP BY sede_id
) AS nominas_por_sede
WHERE nomina > (
SELECT AVG(nomina)
FROM (
SELECT SUM(salario) AS nomina
FROM empleados
GROUP BY sede_id
) AS promedios_nominas
)
ORDER BY nomina DESC, sede_id ASC;




-- ==============================================================================
-- Preguntas de reflexión
-- ==============================================================================

/*

¿Por qué NOT IN (SELECT id_departamento FROM sedes) no permite encontrar los
departamentos sin sedes en este dump? Explique el papel de NULL y describa
una solución segura.
Respuesta: Si la subconsulta de un NOT IN retorna al menos un valor NULL,
toda la evaluación resulta en UNKNOWN y la consulta principal no devuelve nada.
La solución segura es usar NOT IN (SELECT id_departamento FROM sedes
WHERE id_departamento IS NOT NULL) o preferir NOT EXISTS.

¿Por qué el ejercicio 4 usa un promedio distinto para cada sede y el
ejercicio 5 promedia nóminas en lugar de salarios? Indique qué población
utiliza cada cálculo.
Respuesta: El ejercicio 4 compara a un empleado contra el grupo de sus "pares
de sede" (población: empleados de una sede). El ejercicio 5 compara
la "nómina total de una sede" contra otras sedes (población: agrupaciones
de sedes con empleados).

¿Qué permanece después de ejecutar una sentencia: una vista, una tabla derivada
o una CTE? Explique la diferencia.
Respuesta: Solo la VISTA permanece como objeto en la base de datos.
Las tablas derivadas y las CTE son temporales y se destruyen en memoria
en cuanto finaliza el SELECT que las invoca.
/*