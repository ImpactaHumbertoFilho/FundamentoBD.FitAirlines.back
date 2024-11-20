CREATE DEFINER = CURRENT_USER TRIGGER `FITAIRLINES`.`RESERVA_BEFORE_INSERT` BEFORE INSERT ON `RESERVA` FOR EACH ROW
BEGIN
	DECLARE preco_base DECIMAL(10, 2);
    DECLARE preco_adicional DECIMAL(10, 2);

    SELECT v.PRECO_BASE INTO preco_base
    FROM VOO v
    JOIN RESERVA_DE_ASSENTO_VOO rav ON v.ID_VOO = rav.ID_VOO
    WHERE rav.ID_RESERVA = NEW.ID_RESERVA LIMIT 1;

    SELECT c.PRECO_ADICIONAL INTO preco_adicional
    FROM CLASSE c
    JOIN ASSENTO a ON c.ID_CLASSE = a.ID_CLASSE
    JOIN RESERVA_DE_ASSENTO_VOO rav ON a.ID_ASSENTO = rav.ID_ASSENTO
    WHERE rav.ID_RESERVA = NEW.ID_RESERVA LIMIT 1;

    SET NEW.PRECO = preco_base + preco_adicional;
END
