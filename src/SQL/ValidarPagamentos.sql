
-- -----------------------------------------------------
-- Procedure: ValidarPagamentos
-- -----------------------------------------------------
DELIMITER //

CREATE PROCEDURE ValidarPagamentos()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE idReserva INT;
    DECLARE idAssento INT;
    DECLARE precoReserva DECIMAL(10,2);
    DECLARE precoAdicional DECIMAL(10,2);
    DECLARE valorPago DECIMAL(10,2);
    DECLARE precoTotalReserva DECIMAL(10,2);

    -- Cursor para buscar as reservas pendentes de validação
    DECLARE cursor_reservas CURSOR FOR 
        SELECT r.ID_RESERVA, r.ID_ASSENTO, r.PRECO, c.PRECO_ADICIONAL
        FROM reserva r
        JOIN assento a ON r.ID_ASSENTO = a.ID_ASSENTO
        JOIN classe c ON a.ID_CLASSE = c.ID_CLASSE
        WHERE r.STATUS = 1;

    -- Handler para o fim do cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Criação de uma tabela temporária para armazenar as mensagens
    CREATE TEMPORARY TABLE IF NOT EXISTS mensagens_pagamento_insuficiente (
        mensagem VARCHAR(255)
    );

    OPEN cursor_reservas;

    read_loop: LOOP
        FETCH cursor_reservas INTO idReserva, idAssento, precoReserva, precoAdicional;

        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calcula o preço total da reserva
        SET precoTotalReserva = precoReserva + precoAdicional;

        -- Soma o valor pago para a reserva
        SELECT COALESCE(SUM(p.VALOR), 0) INTO valorPago
        FROM pagamento p
        WHERE p.ID_RESERVA = idReserva AND p.STATUS = 1;

        -- Verifica se o valor pago é suficiente
        IF valorPago < precoTotalReserva THEN
            INSERT INTO mensagens_pagamento_insuficiente (mensagem)
            VALUES (CONCAT('Pagamento insuficiente para reserva ID ', idReserva, 
                           '. Valor necessário: ', precoTotalReserva, 
                           '. Valor pago: ', valorPago));
        ELSE
            -- Cria o ticket caso o pagamento seja suficiente
            INSERT INTO ticket (ID_RESERVA, DATA_EMISSAO, PRECO_FINAL, STATUS)
            VALUES (idReserva, NOW(), precoTotalReserva, 1);
        END IF;
    END LOOP;

    CLOSE cursor_reservas;

    -- Retorna todas as mensagens como uma tabela
    SELECT * FROM mensagens_pagamento_insuficiente;

    -- Limpa a tabela temporária (opcional)
    DROP TEMPORARY TABLE mensagens_pagamento_insuficiente;
END //

DELIMITER ;