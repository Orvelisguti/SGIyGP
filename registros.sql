CREATE TABLE IF NOT EXISTS `Usuario` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`email` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Ingreso` (
	`id` integer primary key NOT NULL UNIQUE,
	`descripción` TEXT NOT NULL,
	`monto` REAL NOT NULL,
	`fecha` REAL NOT NULL,
	`usuario_id` INTEGER NOT NULL,
FOREIGN KEY(`usuario_id`) REFERENCES `Usuario`(`id`)
);
CREATE TABLE IF NOT EXISTS `Gasto` (
	`id` integer primary key NOT NULL UNIQUE,
	`descripcion` TEXT NOT NULL,
	`monto` REAL NOT NULL,
	`fecha` REAL NOT NULL,
	`usuario_id` INTEGER NOT NULL,
FOREIGN KEY(`usuario_id`) REFERENCES `Usuario`(`id`)
);

FOREIGN KEY(`usuario_id`) REFERENCES `Usuario`(`id`)
FOREIGN KEY(`usuario_id`) REFERENCES `Usuario`(`id`)