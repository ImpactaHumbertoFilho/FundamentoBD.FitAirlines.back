CREATE DEFINER = CURRENT_USER TRIGGER `FITAIRLINES`.`RESERVA_BAGAGEM_AFTER_DELETE` AFTER DELETE ON `RESERVA_BAGAGEM` FOR EACH ROW
BEGIN
    DECLARE preco_total DECIMAL(10, 2);
    SELECT preco + IFNULL(
                (SELECT SUM(b.preco_adicional) 
                 FROM BAGAGEM b
                 JOIN RESERVA_BAGAGEM rb ON b.id_bagagem = rb.id_bagagem
                 WHERE rb.id_reserva = OLD.id_reserva), 0) 
           + IFNULL(
                (SELECT SUM(a.preco_adicional) 
                 FROM ASSENTO a
                 JOIN RESERVA_DE_ASSENTO_VOO rsv ON a.id_assento = rsv.id_assento
                 WHERE rsv.id_reserva = OLD.id_reserva), 0)
    INTO preco_total
    FROM RESERVA r
    WHERE r.id_reserva = OLD.id_reserva;
    UPDATE RESERVA
    SET preco_total = preco_total
    WHERE id_reserva = OLD.id_reserva;
END
