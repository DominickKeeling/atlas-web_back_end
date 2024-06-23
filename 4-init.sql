-- write a sql script that creates a trigger
-- decreases item quantity
DELLIMITER //

CREATE TRIGGER decrease_item_quanitity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
