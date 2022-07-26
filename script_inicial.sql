-- insert pais
INSERT INTO ubc_pais (id_pais, descripcion, prefijo_cel)VALUES(1, 'ECUADOR', '+593')
INSERT INTO ubc_pais (id_pais, descripcion, prefijo_cel)VALUES(2, 'COLOMBIA', '+593')



-- insert estado
INSERT INTO ubc_pais (id_pais, estado_id, descripcion, prefijo_cel)VALUES(1, 1, 'ECUADOR', '+593')
INSERT INTO ubc_pais (id_pais, estado_id, descripcion, prefijo_cel)VALUES(2, 1, 'COLOMBIA', '+593')


-- insert group
INSERT INTO auth_group (id, name)VALUES(1, 'ADMINISTRADOR')

-- insert roles
INSERT INTO usr_roles  (fecha_creacion,
                        usuario_crea,
                        fecha_modificacion,
                        usuario_modifica,
                        id_rol,
                        descripcion,
                        grupo_id,
                        estado_id)
VALUES
(CURDATE(), 1, CURDATE(), 1, 1, 'ADMINISTRADOR', 1, 1);


-- permisos a asignar al perfilde administrador de sistema



-- tipo personal
INSERT INTO personal_tipopersonal (id_tipo, descripcion, estado_id)VALUES(1, 'INTERNO', 1);
INSERT INTO personal_tipopersonal (id_tipo, descripcion, estado_id)VALUES(2, 'EXTERNO', 1);

-- Categoria Personal
INSERT INTO personal_categoriapersonal(id_categoria, descripcion, estado_id)VALUE(1, 'Siembra', 1)

-- empleados


-- permiso de rol administrador

INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_rol'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_rol'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_rol'));

INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_categoria_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_categoria_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_categoria_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_tipo_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_tipo_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_tipo_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_personal'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_pais'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_pais'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_pais'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_ciudades'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_ciudades'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_ciudades'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_sectores'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_sectores'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_sectores'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_lotes'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_lotes'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_lotes'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_usuarios'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_usuarios'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_usuarios'));


INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'ver_orden_ingreso'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_orden_ingreso'));



INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_orden_produccion'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_orden_produccion'));

INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'crear_orden_proveedor'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'ver_ordenes_proveedor'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'ver_orden_salida'));


INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'actualizar_ordenes_proveedor'));
INSERT INTO auth_group_permissions(GROUP_ID, PERMISSION_ID) VALUES ((select id from auth_group where name = 'ADMINISTRADOR'), (select id from auth_permission where codename = 'editar_ordenes_proveedor'));


